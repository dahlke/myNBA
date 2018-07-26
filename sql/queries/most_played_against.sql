SELECT
    COUNT(*),
    ht.name home_team_name,
    at.name away_team_name
FROM
    game_header gh
-- Get the home team information
INNER JOIN team ht ON
    gh.home_team_id = ht.id
-- Get the visiting team information
INNER JOIN team at ON
    gh.away_team_id = at.id
GROUP BY 2, 3
ORDER BY 1 DESC
LIMIT 10;