 -- https://www.reddit.com/r/dataisbeautiful/comments/7ajydl/every_final_score_that_has_occurred_in_the_nba_oc/

SELECT
	gh.game_date,
	gh.natl_tv_broadcaster,
	ht.name home_team_name,
	at.name away_team_name,
	hls.pts home_team_pts,
	als.pts home_team_pts
FROM
	game_header gh
-- Get the home team information
INNER JOIN team ht ON
	gh.home_team_id = ht.id
INNER JOIN line_score hls ON
	hls.game_id = gh.game_id AND
	hls.team_id = ht.id
-- Get the visiting team information
INNER JOIN team at ON
	gh.away_team_id = at.id
INNER JOIN line_score als ON
	als.game_id = gh.game_id AND
	als.team_id = at.id
ORDER BY gh.game_date DESC
LIMIT 10;