SELECT 
    gh.game_id, gh.game_date, home.name, away.name
FROM game_header gh
JOIN team as home on gh.home_team_id = home.id
JOIN team as away on gh.away_team_id = away.id
WHERE
    (home.id = 1610612744 or away.id = 1610612744) AND 
    (gh.game_date >= '2017-10-17') AND (gh.game_date < '2018-04-14')
ORDER BY gh.game_date;
