from my_nba.downloaders.base import BaseDownloader
from my_nba.db_api.player import PlayerApi
import json


class PlayerDownloader(BaseDownloader):

    def __init__(self):
        super().__init__()
        self._player_api = PlayerApi()

    def download(self):
        player_rows = json.loads(
            self._client.players_info({})
        )['resultSets'][0]['rowSet']

        for player_row in player_rows:
            player_id = player_row[0]
            player_exists = self._player_api.check_player_exists(player_id)

            if player_exists is False:
                result_sets = json.loads(
                        self._client.player_info({'PlayerID': player_id})
                    )['resultSets'][0]
                row_set = result_sets['rowSet']

                if len(row_set) > 0:
                    player_info = row_set[0]
                    self._player_api.insert_player(player_info)
                    self._logger.debug(
                        'Player ID: %d saved' %
                        player_id
                    )
                else:
                    self._logger.info(
                        'Player ID: %d unavailable' %
                        player_id
                    )
            else:
                self._logger.debug(
                    'Player ID: %d already exists' %
                    player_id
                )