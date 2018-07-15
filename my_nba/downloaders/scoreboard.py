from my_nba.client import NBAClient
from my_nba.db_api.box_score import BoxScoreApi
from my_nba.db_api.scoreboard import ScoreboardApi
from datetime import datetime, timedelta
import json
import time

API_DATE_FMT = '%m/%d/%Y'
NBA_MODERN_ERA_DATE = '01/01/2017'

class ScoreboardDownloader():

    def __init__(self):
        super().__init__()
        self._box_score_api = BoxScoreApi()
        self._scoreboard_api = ScoreboardApi()

    def download(self):
        nba_founded_datetime = datetime.strptime(NBA_MODERN_ERA_DATE, API_DATE_FMT)
        game_date = nba_founded_datetime
        # TODO: get max date in there already

        while game_date < datetime.now():
            game_date_exists = self._scoreboard_api.check_game_header_exists(game_date)
            game_date_api_fmt = game_date.strftime(API_DATE_FMT)

            if game_date_exists is False:
                try:
                    self._logger.info("Getting scoreboards for date %s..." % game_date_api_fmt)
                    result = json.loads(
                        self._client.scoreboard({"gameDate": game_date_api_fmt})
                    )
                    if "resultSets" in result:
                        result_sets = result["resultSets"]
                        game_header_row_set = result_sets[0]["rowSet"]
                        line_score_row_set = result_sets[1]["rowSet"]

                        for game_header_row in game_header_row_set:
                            game_id = game_header_row[2]
                            self._scoreboard_api.insert_game_header(game_header_row)

                            try:
                                self._logger.debug("Getting boxscores for Game ID %s" % game_id)
                                box_score_row_set = json.loads(
                                        self._client.box_score({"GameID": game_id})
                                )["resultSets"][0]["rowSet"]

                                for box_score_row in box_score_row_set:
                                    self._box_score_api.insert_box_score(box_score_row)

                            except Exception as e:
                                self._logger.error(e)

                        for line_score_row in line_score_row_set:
                            self._scoreboard_api.insert_line_score(line_score_row)

                except Exception as e:
                    raise(e)
            else:
                self._logger.info("Scoreboard data exists for %s" % game_date_api_fmt)

            game_date += timedelta(days=1)
            time.sleep(.5)
