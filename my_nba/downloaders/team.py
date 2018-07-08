from my_nba.client import NBAClient
from my_nba.db_api import team_api
import json


class TeamDownloader():

	def __init__(self):
		self._client = NBAClient()
		pass

	def download(self):
		team_rows = json.loads(self._client.team_years({}))['resultSets'][0]['rowSet']

		for team_row in team_rows:
			team_id = team_row[1]
			team_exists = team_api.check_team_exists(team_id)
			if team_exists is False:
				result_sets = json.loads(
					self._client.team_info_common({'TeamID': team_id})
				)['resultSets'][0]
				row_set = result_sets['rowSet']

				if len(row_set) > 0:
					team_info_common = row_set[0]
					team_api.insert_team(team_info_common)
				else:
					print('No common data available for team ID: %d' % team_id)
