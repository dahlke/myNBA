SELECT
    gh.game_date,
    gh.game_id,
    t.name home_team_name,
    t2.name visitor_team_name
FROM
    game_header gh,
    team t,
    team t2
WHERE
	gh.home_team_id = t.team_id AND
	gh.visitor_team_id = t2.team_id
GROUP BY 2, 3, 4, 5
ORDER BY 1 DESC
INTO OUTFILE 'all_games.tsv'
FIELDS TERMINATED BY '\t';
