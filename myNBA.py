#! /usr/local/bin/python

from pyMyNBA.client import NBAClient
from pyMyNBA.db_api import team_api, player_api, scoreboard_api, box_score_api
from datetime import datetime, timedelta
import json
import time


API_DATE_FMT = '%m/%d/%Y'
NBA_MODERN_ERA_DATE = '01/01/2017'

client = NBAClient()
print dir(client)


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
                print('No player info available for player ID: %d' % player_id)


def get_games():
    nba_founded_datetime = datetime.strptime(NBA_MODERN_ERA_DATE, API_DATE_FMT)
    game_date = nba_founded_datetime

    while game_date < datetime.now():
        game_date_exists = scoreboard_api.check_game_header_exists(game_date)
        game_date_api_fmt = game_date.strftime(API_DATE_FMT)

        if game_date_exists is False:
            try:
                print 'Getting scoreboards for date %s' % game_date_api_fmt
                result_sets = json.loads(
                    client.scoreboard({'gameDate': game_date_api_fmt})
                )['resultSets']
                game_header_row_set = result_sets[0]['rowSet']
                line_score_row_set = result_sets[1]['rowSet']

                for game_header_row in game_header_row_set:
                    game_id = game_header_row[2]
                    scoreboard_api.insert_game_header(game_header_row)

                    try:
                        print 'Getting boxscores for Game ID %s' % game_id
                        box_score_row_set = json.loads(
                            client.box_score({'GameID': game_id})
                        )['resultSets'][0]['rowSet']

                        for box_score_row in box_score_row_set:
                            box_score_api.insert_box_score(box_score_row)

                    except Exception as e:
                        print e

                    break

                for line_score_row in line_score_row_set:
                    scoreboard_api.insert_game_line_score(line_score_row)
                    break


            except Exception as e:
                print e
        else:
            print 'Score data exists for %s' % game_date_api_fmt

        game_date += timedelta(days=1)
        time.sleep(1)



if __name__ == '__main__':
    # get_teams()
    # get_players()
    get_games()
