SELECT
    gh.game_date,
    gh.game_id,
    /*
    ht.team_id home_team_id,
    vt.team_id visitor_team_id,
    */
    ht.name home_team_name,
    gtls_ht.points home_team_points,
    vt.name visitor_team_name,
    gtls_vt.points visitor_team_points
FROM
    game_header gh,
    game_team_line_score gtls_ht,
    game_team_line_score gtls_vt,
    team ht,
    team vt
WHERE
    gh.game_date >= '2017-07-01' AND
    gh.game_id = gtls_ht.game_id AND
    gh.game_id = gtls_vt.game_id AND
    gtls_ht.team_id = ht.team_id AND
	gh.home_team_id = ht.team_id AND
    gtls_vt.team_id = vt.team_id AND
	gh.visitor_team_id = vt.team_id
GROUP BY 2, 3, 4, 5
ORDER BY 1 DESC;