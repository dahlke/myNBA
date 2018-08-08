from my_nba.downloaders.base import BaseDownloader
from my_nba.db_api.box_score import BoxScoreApi
from my_nba.db_api.scoreboard import ScoreboardApi
from my_nba.util.util import progress
from datetime import datetime, timedelta
import json
import time

API_DATE_FMT = '%m/%d/%Y'
# TODO: take in years as an argument instead
NBA_17_18_SEASON_START_DATE = '09/17/1979'


class ScoreboardDownloader(BaseDownloader):

    def __init__(self):
        super().__init__()
        self._box_score_api = BoxScoreApi()
        self._scoreboard_api = ScoreboardApi()

    def download(self):
        nba_founded_datetime = datetime.strptime(NBA_17_18_SEASON_START_DATE, API_DATE_FMT)
        # TODO: we want one day less than the max day so we don't lose games
        max_date_saved = self._scoreboard_api.get_max_date_saved()
        # game_date = datetime.strptime(
        #        max_date_saved.strftime(API_DATE_FMT), API_DATE_FMT
        #    ) if max_date_saved is not None else nba_founded_datetime
        game_date = nba_founded_datetime
        days_processed = 0

        now_date = datetime.now().date()
        dates_timedelta = now_date - max_date_saved \
                if max_date_saved is not None \
                else now_date - nba_founded_datetime.date()

        while game_date < datetime.now():
            days_processed += 1
            # TODO: This does not work, using wrong dates_timedelta I think
            progress(days_processed, dates_timedelta.days, "Downloading scoreboards...")
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
                                self._logger.info("Getting boxscores for Game ID %s..." % game_id)
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
                time.sleep(.2)

            game_date += timedelta(days=1)
