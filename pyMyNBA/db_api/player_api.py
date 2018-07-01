import pyMyNBA.db_api.memsql_conn as memsql


def check_player_exists(player_id):
    num_player_matches = 0
    with memsql.get_connection() as conn:
        num_player_matches = len(
            conn.query('SELECT * FROM player WHERE id = %d' % player_id)
        )
    return num_player_matches > 0


def insert_team(player_row):
    team_id = player_row[0]
    season_year = player_row[1]
    team_city = player_row[2]
    team_name = player_row[3]
    team_abbreviation = player_row[4]
    team_conference = player_row[5]
    team_division = player_row[6]
    # team_code = player_row[7]
    team_wins = player_row[8]
    team_losses = player_row[9]
    # team_pct = player_row[10]
    team_conf_rank = player_row[11]
    team_div_rank = player_row[12]
    team_min_year = int(player_row[13])
    team_max_year = int(player_row[14])

    insert_query = '''
        INSERT INTO team VALUES (
            "%s",
            "%s",
            "%s",
            "%s",
            "%s",
            "%s",
            "%s",
            %d,
            %d,
            %d,
            %d,
            %d,
            %d
        );
    ''' % (
        team_id,
        season_year,
        team_city,
        team_name,
        team_abbreviation,
        team_conference,
        team_division,
        team_wins,
        team_losses,
        team_conf_rank,
        team_div_rank,
        team_min_year,
        team_max_year
    )

    with memsql.get_connection() as conn:
        try:
            conn.execute(insert_query)
            print('New team (%s) saved.' % team_name)
        except Exception as e:
            print e
