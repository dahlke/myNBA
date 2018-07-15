from my_nba.downloaders.base import BaseDownloader
from my_nba.client import NBAClient
from my_nba.db_api.team import TeamApi
import json


class TeamDownloader(BaseDownloader):

    def __init__(self):
        super().__init__()
        self._client = NBAClient()
        self._team_api = TeamApi()

    def download(self):
        team_rows = json.loads(self._client.team_years({}))['resultSets'][0]['rowSet']

        for team_row in team_rows:
            team_id = team_row[1]
            team_exists = self._team_api.check_team_exists(team_id)

            if team_exists is False:
                result_sets = json.loads(
                        self._client.team_info_common({'TeamID': team_id})
                    )['resultSets'][0]
                row_set = result_sets['rowSet']

                if len(row_set) > 0:
                    team_info_common = row_set[0]
                    self._team_api.insert_team(team_info_common)
                    self._logger.debug('Team ID: %d saved' % team_id)
                else:
                    self._logger.debug('No common data available for team ID: %d' % team_id)