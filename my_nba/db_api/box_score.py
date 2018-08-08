import my_nba.util.memsql_conn as memsql
from my_nba.db_api.base import BaseApi


class BoxScoreApi(BaseApi):

    def insert_box_score(self, box_score_row):
        game_id = box_score_row[0]
        team_id = box_score_row[1]
        team_abbreviation = box_score_row[2]
        team_city = box_score_row[3]
        player_id = box_score_row[4]
        player_name = box_score_row[5]
        start_position = box_score_row[6]
        comment = box_score_row[7]
        minutes = box_score_row[8] if box_score_row[8] is not None else "NULL"
        fgm = box_score_row[9] if box_score_row[9] is not None else "NULL"
        fga = box_score_row[10] if box_score_row[10] is not None else "NULL"
        fg_pct = box_score_row[11] if box_score_row[11] is not None else "NULL"
        fg3m = box_score_row[12] if box_score_row[12] is not None else "NULL"
        fg3a = box_score_row[13] if box_score_row[13] is not None else "NULL"
        fg3_pct = box_score_row[14] if box_score_row[14] is not None else "NULL"
        ftm = box_score_row[15] if box_score_row[15] is not None else "NULL"
        fta = box_score_row[16] if box_score_row[16] is not None else "NULL"
        ft_pct = box_score_row[17] if box_score_row[17] is not None else "NULL"
        oreb = box_score_row[18] if box_score_row[18] is not None else "NULL"
        dreb = box_score_row[19] if box_score_row[19] is not None else "NULL"
        reb = box_score_row[20] if box_score_row[20] is not None else "NULL"
        ast = box_score_row[21] if box_score_row[21] is not None else "NULL"
        stl = box_score_row[22] if box_score_row[22] is not None else "NULL"
        blk = box_score_row[23] if box_score_row[23] is not None else "NULL"
        to = box_score_row[24] if box_score_row[24] is not None else "NULL"
        pf = box_score_row[25] if box_score_row[25] is not None else "NULL"
        pts = box_score_row[26] if box_score_row[26] is not None else "NULL"
        plus_minus = box_score_row[27] if box_score_row[27] is not None else "NULL"

        insert_query = '''
            INSERT INTO box_score VALUES (
                %s,
                %s,
                "%s",
                "%s",
                %s,
                "%s",
                "%s",
                "%s",
                "%s",
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
            team_abbreviation,
            team_city,
            player_id,
            player_name,
            start_position,
            comment,
            minutes,
            fgm,
            fga,
            fg_pct,
            fg3m,
            fg3a,
            fg3_pct,
            ftm,
            fta,
            ft_pct,
            oreb,
            dreb,
            reb,
            ast,
            stl,
            blk,
            to,
            pf,
            pts,
            plus_minus
        )

        with memsql.get_connection() as conn:
            try:
                conn.execute(insert_query)
                self._logger.debug("Box Score for Game ID %s, Team ID %s saved" % (game_id, team_id))
            except Exception as e:
                self._logger.debug("Box Score Insert Query: ", insert_query)
                self._logger.error(e)