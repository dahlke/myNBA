import pyMyNBA.db_api.memsql_conn as memsql


def check_game_header_exists(game_date):
    num_game_header_matches = 0
    game_date_db_fmt = game_date.strftime('%Y-%m-%d')

    with memsql.get_connection() as conn:
        num_game_header_matches = len(
            conn.query('SELECT * FROM game_header WHERE game_date = "%s"' % game_date_db_fmt)
        )
    return num_game_header_matches > 0


def insert_game_header(team_row):
    team_id = team_row[0]

    insert_query = '''
        INSERT INTO game_header VALUES (
        );
    ''' % (
    )

    with memsql.get_connection() as conn:
        try:
            # conn.execute(insert_query)
            # print('New team (%s) saved.' % team_name)
            pass
        except Exception as e:
            print e
