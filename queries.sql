SELECT *
FROM
    game_header gh,
    team t
WHERE gh.home_team_id = t.id;

select
    gh.game_date,
    gh.home_team_id,
    gh.visitor_team_id,
    IF (t.team_id = gh.home_team_id, t.name, NULL) home_team,
    IF (t.team_id = gh.visitor_team_id, t.name, NULL) visitor_team
from
    game_header gh,
    team t
where
    game_date = '2015-10-03' AND
    (
        home_team_id = t.team_id OR
        visitor_team_id = t.team_id
    );
