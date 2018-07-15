from my_nba.client import NBAClient
import logging


class BaseDownloader():

    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._client = NBAClient()