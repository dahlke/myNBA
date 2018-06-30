import os
import json
import urllib2
import re
import requests


# HELPER FUNCTIONS
# wtf python?  http://stackoverflow.com/a/13105359
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# CLIENT FUNCTIONS
# acquire api info from json file
path = os.path.join(os.path.dirname(__file__), 'json/nba_api_endpoints.json')
data = byteify(json.loads(open(path).read()))

parameters = {}
for item in data["parameters"]:
    parameters[item["name"]] = item


class NBAClient(object):
    pass


# make a function that gets data from NBA endpoint with default params
def make_endpoint(name, endpoint):
    def func(params):
        all_params = dict()

        for param in endpoint["parameters"]:
            value = params.get(param, parameters[param]["default"])
            all_params[param] = value

        query = []
        for param, value in all_params.iteritems():
            query.append(urllib2.quote(param) + '=' + urllib2.quote(str(value)))

        query_str = '?' + '&'.join(query)

        url = endpoint['url'] + query_str
        headers = {
            "host": "stats.nba.com",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "accept-encoding": "Accepflate, sdch",
            "accept-language": "he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        return response.text

    func.__name__ = name
    return func


# iterate through the endpoints and create a method for each one
for endpoint in data['stats_endpoints']:
    func = make_endpoint(endpoint["name"], endpoint)
    setattr(NBAClient, snake(endpoint["name"]), staticmethod(func))
