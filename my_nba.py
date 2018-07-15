#! /usr/local/bin/python3
from my_nba.client import NBAClient
from my_nba.downloaders.player import PlayerDownloader
from my_nba.downloaders.team import TeamDownloader
from my_nba.downloaders.scoreboard import ScoreboardDownloader
import logging
import argparse

logging.basicConfig(filename='my_nba.log', level=logging.INFO)


class MyNBA():

    def __init__(self, argparse_args):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.info("Initializing MyNBA program...")
        self._logger.debug('NBA client methods: %s' % dir(NBAClient()))

        # Schedule jobs instead of doing this
        if argparse_args.players:
            self._logger.info('Downloading players...')
            player_downloader = PlayerDownloader()
            player_downloader.download()
            self._logger.info('Players downloaded.')

        if argparse_args.teams:
            self._logger.info('Downloading teams...')
            team_downloader = TeamDownloader()
            team_downloader.download()
            self._logger.info('Teams downloaded.')

        if argparse_args.scoreboards:
            self._logger.info('Downloading scoreboards...')
            scoreboard_downloader = ScoreboardDownloader()
            scoreboard_downloader.download()
            self._logger.info('Scoreboards downloaded.')

        self._logger.info("MyNBA program terminating.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download NBA data for analysis"
    )
    parser.add_argument(
        "-p", "--players",
        action="store_true",
        help="Download NBA player data"
    )
    parser.add_argument(
        "-t", "--teams",
        action="store_true",
        help="Download NBA team data"
    )
    parser.add_argument(
        "-s", "--scoreboards",
        action="store_true", help="Download NBA scoreboard data"
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true", help="Print debug information"
    )
    args = parser.parse_args()
    prog = MyNBA(args)