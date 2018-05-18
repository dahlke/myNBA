DROP DATABASE IF EXISTS nba;
CREATE DATABASE nba;
USE nba;

CREATE TABLE player (
	id int,
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
    primary key (id)
);

CREATE TABLE team (
	id int,
	name varchar(32),
	abbreviation varchar(3),
	city varchar(32),
    primary key (id)
);

CREATE TABLE player_simple (
	id int,
	first_name varchar(32),
	last_name varchar(32),
	team_id int,
    primary key (id)
);
