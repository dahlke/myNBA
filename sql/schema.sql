CREATE DATABASE IF NOT EXISTS nba;

CREATE TABLE IF NOT EXISTS nba.team (
	team_id int,
    season_yr varchar(16),
	city varchar(32),
	name varchar(32),
	abbreviation varchar(3),
    conference varchar(8),
    division varchar(16),
    wins int,
    losses int,
    conference_rank int,
    division_rank int,
    min_year int,
    max_year int,
    /* raw_data json, */
    primary key (team_id)
);

CREATE TABLE IF NOT EXISTS nba.player (
	player_id int,
	first_name varchar(32),
	last_name varchar(32),
	team_id int,
	birth_date varchar(32),
	school varchar(32),
	country varchar(3),
	last_affiliation varchar(32),
	height varchar(5),
	weight int,
	season_exp smallint,
	jersey smallint,
	position varchar(8),
	from_year int,
	to_year int,
	d_league bool,
	draft_year int,
	draft_round int,
	draft_number int,
    /* raw_data json, */
    primary key (player_id)
);

CREATE TABLE IF NOT EXISTS nba.game_header (
    game_id int,
    game_date date,
    home_team_id int,
    visitor_team_id int,
    natl_tv_broadcaster varchar(16),
    /* raw_data json, */
    primary key(game_id)
);

CREATE TABLE IF NOT EXISTS nba.game_team_line_score (
    game_id int,
    team_id int,
    points_q1 int,
    points_q2 int,
    points_q3 int,
    points_q4 int,
    points_ot1 int,
    points_ot2 int,
    points_ot3 int,
    points_ot4 int,
    points_ot5 int,
    points_ot6 int,
    points_ot7 int,
    points_ot8 int,
    points_ot9 int,
    points_ot10 int,
    points int,
    fg_pct float,
    fg3_pct float,
    ft_pct float,
    assists int,
    rebounds int,
    turnovers int,
    primary key(game_id, team_id)
);
