SELECT 
    gh.game_id, gh.game_date, home.name, away.name
FROM game_header gh
JOIN team as home on gh.home_team_id = home.id
JOIN team as away on gh.away_team_id = away.id
WHERE
    (home.id = 1610612744 or away.id = 1610612744) AND 
    
    (gh.game_date >= '2017-10-17') AND (gh.game_date <= '2018-04-14')
ORDER BY gh.game_date;

/*
select gh.game_id, gh.home_team_id, gh.away_team_id, ht.name as hometeamname, atm.name as awayteamname
from game_header gh
inner join team ht on gh.home_team_id=ht.id 
inner join team atm on gh.away_team_id=atm.id
where
gh.game_date >= '2017-10-17' 
and gh.game_date <= '2018-04-14' and
(gh.home_team_id = 1610612744 or gh.away_team_id = 1610612744)
order by game_date DESC;
*/