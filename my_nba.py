#! /usr/local/bin/python3
from my_nba.client import NBAClient
from my_nba.downloaders.player import PlayerDownloader
from my_nba.downloaders.team import TeamDownloader
from my_nba.downloaders.scoreboard import ScoreboardDownloader
import logging
import argparse


class MyNBA():

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)

        self._logger.info("Initializing MyNBA program.")

        self._player_downloader = PlayerDownloader()
        self._team_downloader = TeamDownloader()
        self._scoreboard_downloader = ScoreboardDownloader()

        client = NBAClient()
        self._logger.debug('NBA client methods:', dir(client))

    def get_players(self):
        self._player_downloader.download()

    def get_teams(self):
        self._team_downloader.download()

    def get_scoreboards(self):
        self._scoreboard_downloader.download()


if __name__ == "__main__":
    prog = MyNBA()

    parser = argparse.ArgumentParser(description="Download NBA data for analysis")
    parser.add_argument("-p", "--players", action="store_true", help="Download NBA player data")
    parser.add_argument("-t", "--teams", action="store_true", help="Download NBA team data")
    parser.add_argument("-s", "--scoreboards", action="store_true", help="Download NBA scoreboard data")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information")

    args = parser.parse_args()


    if args.players:
        prog.get_players()

    if args.teams:
        prog.get_teams()

    if args.scoreboards:
        prog.get_scoreboards()
