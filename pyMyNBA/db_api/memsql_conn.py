from memsql.common import database

HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASSWORD = ""
DATABASE = "nba"


def get_connection():
    """ Returns a new connection to the database. """
    return database.connect(
        host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE
    )
