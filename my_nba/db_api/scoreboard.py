import my_nba.util.memsql_conn as memsql
from my_nba.db_api.base import BaseApi


class ScoreboardApi(BaseApi):

    def get_max_date_saved(self):
        max_date = None

        with memsql.get_connection() as conn:
            max_game_date_rows = conn.query('SELECT MAX(game_date) max_date FROM game_header')
            max_date = max_game_date_rows[0]['max_date']

        return max_date

    def check_game_header_exists(self, game_date):
        num_game_header_matches = 0
        game_date_db_fmt = game_date.strftime('%Y-%m-%d')

        with memsql.get_connection() as conn:
            num_game_header_matches = len(
                conn.query('SELECT * FROM game_header WHERE game_date = "%s"' % game_date_db_fmt)
            )
        return num_game_header_matches > 0


    def insert_game_header(self, game_header_row):
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
                %s, "%s", %s, %s,
                "%s"
            );
        ''' % (
            game_id, game_date, game_home_team_id, game_away_team_id,
            natl_tv_broadcaster_abbreviation
        )

        with memsql.get_connection() as conn:
            try:
                conn.execute(insert_query)
                self._logger.debug('Game Header for Game ID %s saved.' % (game_id))
            except Exception as e:
                self._logger.debug('Game Header insert query:', insert_query)
                self._logger.error(e)
                raise(e)

    def insert_line_score(self, line_score_row):
        # game_date = line_score_row[0]
        # game_sequence = line_score_row[1]
        game_id = line_score_row[2]
        team_id = line_score_row[3]
        # team_abbreviation = line_score_row[4]
        # team_city_name = line_score_row[5]
        # team_wins_losses = line_score_row[6]
        pts_qtr1 = line_score_row[7] if line_score_row[7] is not None else 0
        pts_qtr2 = line_score_row[8] if line_score_row[8] is not None else 0
        pts_qtr3 = line_score_row[9] if line_score_row[9] is not None else 0
        pts_qtr4 = line_score_row[10] if line_score_row[10] is not None else 0
        pts_ot1 = line_score_row[11] if line_score_row[11] is not None else 0
        pts_ot2 = line_score_row[12] if line_score_row[12] is not None else 0
        pts_ot3 = line_score_row[13] if line_score_row[13] is not None else 0
        pts_ot4 = line_score_row[14] if line_score_row[14] is not None else 0
        pts_ot5 = line_score_row[15] if line_score_row[15] is not None else 0
        pts_ot6 = line_score_row[16] if line_score_row[16] is not None else 0
        pts_ot7 = line_score_row[17] if line_score_row[17] is not None else 0
        pts_ot8 = line_score_row[18] if line_score_row[18] is not None else 0
        pts_ot9 = line_score_row[19] if line_score_row[19] is not None else 0
        pts_ot10 = line_score_row[20] if line_score_row[20] is not None else 0
        pts = line_score_row[21] if line_score_row[21] is not None else 0
        fg_pct = line_score_row[22] if line_score_row[22] is not None else 0
        ft_pct = line_score_row[23] if line_score_row[23] is not None else 0
        pg3_pct = line_score_row[24] if line_score_row[24] is not None else 0
        ast = line_score_row[25] if line_score_row[25] is not None else 0
        reb = line_score_row[26] if line_score_row[26] is not None else 0
        tov = line_score_row[27] if line_score_row[27] is not None else 0

        insert_query = '''
            INSERT INTO line_score VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s
            );
        ''' % (
            game_id, team_id, pts_qtr1, pts_qtr2,
            pts_qtr3, pts_qtr4, pts_ot1, pts_ot2,
            pts_ot3, pts_ot4, pts_ot5, pts_ot6,
            pts_ot7, pts_ot8, pts_ot9, pts_ot10,
            pts, fg_pct, pg3_pct, ft_pct,
            ast, reb, tov
        )

        with memsql.get_connection() as conn:
            try:
                conn.execute(insert_query)
                self._logger.debug('Line Score for Game ID %s saved.' % (game_id))
            except Exception as e:
                print(insert_query)
                self._logger.debug('Line Score insert query:', insert_query)
                self._logger.error(e)
                raise(e)
