from pyMyNBA.client import NBAClient
import pyMyNBA.db_api.team_api as team_api
import pyMyNBA.db_api.player_api as player_api
import json

# Get the date
# Get every game played that day
# Get the results of each game
# Get the teams in each game
# Get the players in each game
# Get the box scores of each game

client = NBAClient()
print dir(client)
# print client.player_profile({ 'PlayerID': 201939 })


def get_teams():
    team_rows = json.loads(client.team_years({}))['resultSets'][0]['rowSet']

    for team_row in team_rows:
        team_id = team_row[1]
        team_exists = team_api.check_team_exists(team_id)
        if team_exists is False:
            result_sets = json.loads(
                client.team_info_common({'TeamID': team_id})
            )['resultSets'][0]
            row_set = result_sets['rowSet']

            if len(row_set) > 0:
                team_info_common = row_set[0]
                team_api.insert_team(team_info_common)
            else:
                print('No common data available for team ID: %d' % team_id)


def get_players():
    player_rows = json.loads(client.players_info({}))['resultSets'][0]['rowSet']

    for player_row in player_rows:
        player_id = player_row[0]
        player_exists = player_api.check_player_exists(player_id)

        if player_exists is False:
            result_sets = json.loads(
                client.player_info({'PlayerID': player_id})
            )['resultSets'][0]
            row_set = result_sets['rowSet']

            print json.loads(
                client.player_info({'PlayerID': player_id})
            )['resultSets'][0]['headers']

            if len(row_set) > 0:
                player_info = row_set[0]
                player_api.insert_player(player_info)
                break
            else:
                print('No player info available for player ID: %d' % team_id)
    pass


if __name__ == '__main__':
    # get_teams()
    get_players()
