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


CREATE TABLE nba.season (
    id bigint auto_increment,
    regular_season_start date,
    regular_season_end date,
    playoffs_start date,
    playoffs_end date,
    finals_start date,
    finals_end date,
    primary key (id)
);

INSERT INTO nba.season VALUES
    (1, "1979-10-12", "1980-03-30", "1980-04-02", "1980-04-30", "1980-05-04", "1980-06-16"),
    (2, "1980-10-10", "1981-03-29", "1981-03-31", "1981-05-03", "1981-05-05", "1981-06-14"),
    (3, "1981-10-30", "1982-04-18", "1982-04-20", "1982-05-23", "1982-05-27", "1982-06-08"),
    (4, "1982-10-29", "1983-04-17", "1983-04-19", "1983-05-20", "1983-05-22", "1983-05-30"),
    (5, "1983-10-28", "1984-04-15", "1984-04-17", "1984-05-25", "1984-05-27", "1984-06-12"),
    (6, "1984-10-26", "1985-04-14", "1985-04-17", "1985-05-22", "1985-05-27", "1985-06-09"),
    (7, "1985-10-25", "1986-04-13", "1986-04-17", "1986-05-21", "1986-05-26", "1986-06-08"),
    (8, "1986-10-31", "1987-04-19", "1987-04-23", "1987-05-30", "1987-06-02", "1987-06-14"),
    (9, "1987-11-06", "1988-04-24", "1988-04-28", "1988-06-04", "1988-06-07", "1988-06-21");

INSERT INTO nba.season VALUES
    (10, "1988-11-04", "1989-04-23", "1989-04-27", "1989-06-02", "1989-06-06", "1989-06-13"),
    (11, "1989-11-03", "1990-04-22", "1990-04-26", "1990-06-03", "1990-06-05", "1990-06-14"),
    (12, "1990-11-02", "1991-04-21", "1991-04-25", "1991-05-30", "1991-06-02", "1991-06-12"),
    (13, "1991-11-01", "1992-04-19", "1992-04-23", "1992-05-29", "1992-06-03", "1992-06-14"),
    (14, "1992-11-06", "1993-04-25", "1993-04-29", "1993-06-05", "1993-06-09", "1993-06-20"),
    (15, "1993-11-05", "1994-04-24", "1994-04-28", "1994-06-05", "1994-06-08", "1994-06-22"),
    (16, "1994-11-04", "1995-04-23", "1995-04-27", "1995-06-04", "1995-06-07", "1995-06-14"),
    (17, "1995-11-03", "1996-04-21", "1996-04-25", "1996-06-02", "1996-06-05", "1996-06-16"),
    (18, "1996-11-01", "1997-04-20", "1997-04-24", "1997-05-29", "1997-06-01", "1997-06-13"),
    (19, "1997-10-31", "1998-04-19", "1998-04-23", "1998-05-31", "1998-06-03", "1998-06-14");

INSERT INTO nba.season VALUES
    (20, "1998-02-05", "1999-05-05", "1999-05-08", "1999-06-11", "1999-06-16", "1999-06-25"),
    (21, "1999-11-02", "2000-04-19", "2000-04-22", "2000-06-04", "2000-06-07", "2000-06-19"),
    (22, "2000-10-31", "2001-04-18", "2001-04-21", "2001-06-03", "2001-06-06", "2001-06-15"),
    (23, "2001-10-30", "2002-04-17", "2002-04-20", "2002-06-02", "2002-06-05", "2002-06-12"),
    (24, "2002-10-29", "2003-04-16", "2003-04-19", "2003-05-29", "2003-06-04", "2003-06-15"),
    (25, "2003-10-28", "2004-04-14", "2004-04-17", "2004-06-01", "2004-06-06", "2004-06-15"),
    (26, "2004-11-02", "2005-04-20", "2005-04-23", "2005-06-06", "2005-06-09", "2005-06-23"),
    (27, "2005-11-01", "2006-04-19", "2006-04-22", "2006-06-03", "2006-06-08", "2006-06-20"),
    (28, "2006-10-31", "2007-04-18", "2007-04-21", "2007-06-02", "2007-06-07", "2007-06-14"),
    (29, "2007-10-30", "2008-04-16", "2008-04-19", "2008-05-30", "2008-06-05", "2008-06-17");

INSERT INTO nba.season VALUES
    (30, "2009-10-27", "2010-04-14", "2010-04-17", "2010-05-29", "2010-06-03", "2010-06-17"),
    (31, "2010-10-26", "2011-04-13", "2011-04-16", "2011-05-26", "2011-05-31", "2011-06-12"),
    (32, "2011-12-25", "2012-04-26", "2012-04-28", "2012-06-09", "2012-06-12", "2012-06-21"),
    (33, "2012-10-30", "2013-04-17", "2013-04-20", "2013-06-03", "2013-06-06", "2013-06-20"),
    (34, "2013-10-29", "2014-04-16", "2014-04-19", "2014-05-31", "2014-06-05", "2014-06-15"),
    (35, "2014-10-28", "2015-04-15", "2015-04-18", "2015-05-27", "2015-06-04", "2015-06-16"),
    (36, "2015-10-27", "2016-04-13", "2016-04-16", "2016-05-30", "2016-06-02", "2016-06-19"),
    (37, "2016-10-25", "2017-04-12", "2017-04-15", "2017-05-25", "2017-06-01", "2017-06-12"),
    (38, "2017-10-17", "2018-04-11", "2018-04-14", "2018-05-28", "2018-05-31", "2018-06-08");