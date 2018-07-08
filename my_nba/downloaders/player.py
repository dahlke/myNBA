from my_nba.client import NBAClient
from my_nba.db_api import player_api
import json


class PlayerDownloader():

	def __init__(self):
		self._client = NBAClient()
		pass

	def download(self):
		player_rows = json.loads(self._client.players_info({}))['resultSets'][0]['rowSet']

		for player_row in player_rows:
			player_id = player_row[0]
			player_exists = player_api.check_player_exists(player_id)

			if player_exists is False:
				result_sets = json.loads(
					self._client.player_info({'PlayerID': player_id})
				)['resultSets'][0]
				row_set = result_sets['rowSet']

				"""
				TODO: logger.debug
				print(json.loads(
					self._client.player_info({'PlayerID': player_id})
				)['resultSets'][0]['headers'])
				"""

				if len(row_set) > 0:
					player_info = row_set[0]
					player_api.insert_player(player_info)
					break
				else:
					print('No player info available for player ID: %d' % player_id)
