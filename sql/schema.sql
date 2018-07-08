CREATE DATABASE IF NOT EXISTS nba;

CREATE TABLE IF NOT EXISTS nba.team (
	id int,
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
    primary key (id)
);

CREATE TABLE IF NOT EXISTS nba.player (
	id int,
	first_name varchar(32),
	last_name varchar(32),
	team_id int,
	birth_date varchar(32),
	school varchar(32),
	country varchar(3),
	last_affiliation varchar(32),
	height int,
	weight int,
	season_exp smallint,
	jersey smallint,
	position varchar(8),
	from_year int,
	to_year int,
	d_league bool,
	draft_year varchar(8),
	draft_round varchar(8),
	draft_number varchar(8),
    /* raw_data json, */
    primary key (id)
);

CREATE TABLE IF NOT EXISTS nba.game_header (
    game_id int,
    game_date date,
    home_team_id int,
    away_team_id int,
    natl_tv_broadcaster varchar(16),
    /* raw_data json, */
    primary key(game_id)
);

CREATE TABLE IF NOT EXISTS nba.line_score (
    game_id int,
    team_id int,
    pts_q1 int,
    pts_q2 int,
    pts_q3 int,
    pts_q4 int,
    pts_ot1 int,
    pts_ot2 int,
    pts_ot3 int,
    pts_ot4 int,
    pts_ot5 int,
    pts_ot6 int,
    pts_ot7 int,
    pts_ot8 int,
    pts_ot9 int,
    pts_ot10 int,
    pts int,
    fg_pct float,
    fg3_pct float,
    ft_pct float,
    ast int,
    reb int,
    tov int,
    primary key(game_id, team_id)
);


CREATE TABLE IF NOT EXISTS nba.box_score (
    game_id int,
    team_id int,
    team_abbreviation varchar(16),
    team_city varchar(32),
    player_id int,
    player_name varchar(64),
    start_position varchar(32),
    comment varchar(128),
    minutes int,
    fgm int,
    fga int,
    fg_pct int,
    fg3m int,
    fg3a int,
    fg3_pct int,
    ftm int,
    fta int,
    ft_pct int,
    oreb int,
    dreb int,
    reb int,
    ast int,
    stl int,
    blk int,
    tov int,
    pf int,
    pts int,
    plus_minus int,
    primary key(game_id, team_id, player_id)
);

/*
CREATE TABLE IF NOT EXISTS nba.box_score_summary (

);
*/
