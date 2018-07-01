import pyMyNBA.db_api.memsql_conn as memsql


def check_game_header_exists(game_date):
    num_game_header_matches = 0
    game_date_db_fmt = game_date.strftime('%Y-%m-%d')

    with memsql.get_connection() as conn:
        num_game_header_matches = len(
            conn.query('SELECT * FROM game_header WHERE game_date = "%s"' % game_date_db_fmt)
        )
    return num_game_header_matches > 0


def insert_game_header(game_header_row):
    game_date = game_header_row[0]
    # game_sequence = game_header_row[1]
    game_id = game_header_row[2]
    # game_status_id = game_header_row[3]
    # game_status_text = game_header_row[4]
    # game_code = game_header_row[5]
    game_home_team_id = game_header_row[6]
    game_away_team_id = game_header_row[7]
    # season = game_header_row[8]
    # live_period = game_header_row[9]
    # live_pc_time = game_header_row[10]
    natl_tv_broadcaster_abbreviation = game_header_row[11]
    # live_period_time_bcast = game_header_row[12]
    # wh_status = game_header_row[13]

    insert_query = '''
        INSERT INTO game_header VALUES (
            %s,
            "%s",
            %s,
            %s,
            "%s"
        );
    ''' % (
        game_id,
        game_date,
        game_home_team_id,
        game_away_team_id,
        natl_tv_broadcaster_abbreviation
    )

    with memsql.get_connection() as conn:
        try:
            print insert_query
            conn.execute(insert_query)
            print('Game ID (%s) saved from day %s.' % (game_id, game_date))
        except Exception as e:
            print e

def insert_game_line_score(game_line_score_row):
    game_date = game_line_score_row[0]
    game_sequence = game_line_score_row[1]
    game_id = game_line_score_row[2]
    team_id = game_line_score_row[3]
    team_abbreviation = game_line_score_row[4]
    team_city_name = game_line_score_row[5]
    team_wins_losses = game_line_score_row[6]
    pts_qtr1 = game_line_score_row[7]
    pts_qtr2 = game_line_score_row[8]
    pts_qtr3 = game_line_score_row[9]
    pts_qtr4 = game_line_score_row[10]
    pts_ot1 = game_line_score_row[11]
    pts_ot2 = game_line_score_row[12]
    pts_ot3 = game_line_score_row[13]
    pts_ot4 = game_line_score_row[14]
    pts_ot5 = game_line_score_row[15]
    pts_ot6 = game_line_score_row[16]
    pts_ot7 = game_line_score_row[17]
    pts_ot8 = game_line_score_row[18]
    pts_ot9 = game_line_score_row[19]
    pts_ot10 = game_line_score_row[20]
    pts = game_line_score_row[21]
    fg_pct = game_line_score_row[22]
    ft_pct = game_line_score_row[23]
    pg3_pct = game_line_score_row[24]
    ast = game_line_score_row[25]
    reb = game_line_score_row[26]
    tov = game_line_score_row[27]

    insert_query = '''
        INSERT INTO game_team_line_score VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        );
    ''' % (
        game_id,
        team_id,
        pts_qtr1,
        pts_qtr2,
        pts_qtr3,
        pts_qtr4,
        pts_ot1,
        pts_ot2,
        pts_ot3,
        pts_ot4,
        pts_ot5,
        pts_ot6,
        pts_ot7,
        pts_ot8,
        pts_ot9,
        pts_ot10,
        pts,
        fg_pct,
        pg3_pct,
        ft_pct,
        ast,
        reb,
        tov
    )

    with memsql.get_connection() as conn:
        try:
            print insert_query
            conn.execute(insert_query)
            print('Game Line Score for Game (%s) saved from day %s.' % (game_id, game_date))
        except Exception as e:
            print e
