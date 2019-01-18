from my_nba.downloaders.base import BaseDownloader
from my_nba.client import NBAClient
from my_nba.db_api.team import TeamApi
from my_nba.util.util import progress
import json


class TeamDownloader(BaseDownloader):

    def __init__(self):
        super().__init__()
        self._client = NBAClient()
        self._team_api = TeamApi()

    def download(self):
        print("neilio 1")
        team_rows = json.loads(self._client.team_years({}))["resultSets"][0]["rowSet"]
        print("neilio 2")

        print(team_rows)
        for i, team_row in enumerate(team_rows):
            print("neil", team_row)
            progress(i, len(team_rows), "Downloading teams...")
            team_id = team_row[1]
            team_exists = self._team_api.check_team_exists(team_id)

            if team_exists is False:
                result_sets = json.loads(
                        self._client.team_info_common({"TeamID": team_id})
                    )["resultSets"][0]
                row_set = result_sets["rowSet"]

                if len(row_set) > 0:
                    team_info_common = row_set[0]
                    self._team_api.insert_team(team_info_common)
                    self._logger.debug("Team ID: %d saved" % team_id)
                else:
                    self._logger.debug("No data for Team ID: %d" % team_id)
        self._logger.info("All teams downloaded.")
