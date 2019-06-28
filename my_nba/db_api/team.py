from my_nba.db_api.base import BaseApi


class TeamApi(BaseApi):


    def check_team_exists(self, team_id):
        num_team_matches = 0
        return num_team_matches > 0


    def insert_team(self, team_row):
        team_id = team_row[0]
        season_year = team_row[1]
        team_city = team_row[2]
        team_name = team_row[3]
        team_abbreviation = team_row[4]
        team_conference = team_row[5]
        team_division = team_row[6]
        # team_code = team_row[7]
        team_wins = team_row[8]
        team_losses = team_row[9]
        # team_pct = team_row[10]
        team_conf_rank = team_row[11]
        team_div_rank = team_row[12]
        team_min_year = int(team_row[13])
        team_max_year = int(team_row[14])

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
