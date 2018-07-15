import my_nba.util.memsql_conn as memsql
from my_nba.db_api.base import BaseApi


class PlayerApi(BaseApi):


    def check_player_exists(self, player_id):
        num_player_matches = 0
        with memsql.get_connection() as conn:
            num_player_matches = len(
                conn.query('SELECT * FROM player WHERE id = %d' % player_id)
            )
        return num_player_matches > 0


    def insert_player(self, player_row):
        player_id = player_row[0]
        player_first_name = player_row[1]
        player_last_name = player_row[2]
        # player_display_first_initial_last = player_row[3]
        # player_display_last_comma_first = player_row[4]
        # player_display_first_last = player_row[5]
        player_birthdate = player_row[6]
        player_school = player_row[7]
        player_country = player_row[8]
        player_last_affiliation = player_row[9]
        player_height = player_row[10] if player_row[11] != "" else 'NULL'
        player_weight = player_row[11] if player_row[11] != "" else 'NULL'
        player_season_exp = player_row[12] \
            if player_row[12] is not None else 'NULL'
        player_jersey = player_row[13] if player_row[13] != "" else 'NULL'
        player_position = player_row[14]
        # player_roster_status = player_row[15]
        player_team_id = player_row[16]
        # player_team_name = player_row[17]
        # player_team_abbreviation = player_row[18]
        # player_team_code = player_row[19] # player_team_city = player_row[20]
        # player_player_code = player_row[21]
        player_from_year = player_row[22]
        player_to_year = player_row[23]
        player_dleague_flag = player_row[24]
        # player_games_played_flag = player_row[25]
        player_draft_year = player_row[26]
        player_draft_round = player_row[27]
        player_draft_number = player_row[28]

        insert_query = '''
            INSERT INTO player VALUES (
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
                "%s",
                %s,
                %s,
                "%s",
                "%s",
                "%s",
                "%s"
            );
        ''' % (
            player_id,
            player_first_name,
            player_last_name,
            player_team_id,
            player_birthdate,
            player_school,
            player_country,
            player_last_affiliation,
            player_height,
            player_weight,
            player_season_exp,
            player_jersey,
            player_position,
            player_from_year,
            player_to_year,
            player_dleague_flag,
            player_draft_year,
            player_draft_round,
            player_draft_number
        )

        with memsql.get_connection() as conn:
            try:
                conn.execute(insert_query)
                self._logger.info(
                    "%s %s saved." %
                    (player_first_name, player_last_name)
                )
            except Exception as e:
                self._logger.error(insert_query)
                raise(e)
