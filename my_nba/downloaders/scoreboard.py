from my_nba.client import NBAClient
from my_nba.db_api import scoreboard_api, box_score_api
from datetime import datetime, timedelta
import json
import time

API_DATE_FMT = '%m/%d/%Y'
NBA_MODERN_ERA_DATE = '01/01/2017'


class ScoreboardDownloader():

    def __init__(self):
            self._client = NBAClient()
            pass

    def download(self):
        nba_founded_datetime = datetime.strptime(NBA_MODERN_ERA_DATE, API_DATE_FMT)
        game_date = nba_founded_datetime

        while game_date < datetime.now():
            game_date_exists = scoreboard_api.check_game_header_exists(game_date)
            game_date_api_fmt = game_date.strftime(API_DATE_FMT)

            if game_date_exists is False:
                try:
                    print("Getting scoreboards for date %s" % game_date_api_fmt)
                    result_sets = json.loads(
                            self._client.scoreboard({"gameDate": game_date_api_fmt})
                    )["resultSets"]
                    game_header_row_set = result_sets[0]["rowSet"]
                    line_score_row_set = result_sets[1]["rowSet"]

                    for game_header_row in game_header_row_set:
                        game_id = game_header_row[2]
                        scoreboard_api.insert_game_header(game_header_row)

                        try:
                            print("Getting boxscores for Game ID %s" % game_id)
                            box_score_row_set = json.loads(
                                    self._client.box_score({"GameID": game_id})
                            )["resultSets"][0]["rowSet"]

                            for box_score_row in box_score_row_set:
                                box_score_api.insert_box_score(box_score_row)

                        except Exception as e:
                            print(e)

                        break

                    for line_score_row in line_score_row_set:
                        scoreboard_api.insert_line_score(line_score_row)
                        break

                except Exception as e:
                        print(e)
            else:
                print("Score data exists for %s" % game_date_api_fmt)

            game_date += timedelta(days=1)
            time.sleep(1)
