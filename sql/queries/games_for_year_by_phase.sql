WITH season_dates AS (
	SELECT
		*
	FROM season
	WHERE regular_season_start > "1979-01-01"
	ORDER BY regular_season_start ASC
	LIMIT 1
),
all_games_in_regular_season AS (
	SELECT
		*
	FROM
		game_header gh,
		season_dates sd
	WHERE
		gh.game_date BETWEEN sd.regular_season_start AND sd.regular_season_end
),
all_games_in_playoffs AS (
	SELECT
		*
	FROM
		game_header gh,
		season_dates sd
	WHERE
		gh.game_date BETWEEN sd.playoffs_start AND sd.playoffs_end
),
all_games_in_finals AS (
	SELECT
		*
	FROM
		game_header gh,
		season_dates sd
	WHERE
		gh.game_date BETWEEN sd.finals_start AND sd.finals_end
)
SELECT
    agip.game_date,
    agip.natl_tv_broadcaster,
    ht.name home_team_name,
    at.name away_team_name,
    hls.pts home_team_pts,
    als.pts away_team_pts
FROM
    all_games_in_playoffs agip

-- Get the home team information
JOIN team ht ON
    agip.home_team_id = ht.id
JOIN line_score hls ON
    hls.game_id = agip.game_id AND
    hls.team_id = ht.id

-- Get the visiting team information
JOIN team at ON
    agip.away_team_id = at.id
JOIN line_score als ON
    als.game_id = agip.game_id AND
    als.team_id = at.id
ORDER BY agip.game_date DESC