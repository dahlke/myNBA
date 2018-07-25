SELECT id FROM player WHERE first_name = 'Stephen';
/*
+--------+
| id     |
+--------+
| 201939 |
+--------+
1 row in set (0.10 sec)
*/

SELECT gh.game_date, bs.pts, bs.plus_minus
FROM box_score bs, game_header gh
WHERE
	gh.game_id = bs.game_id AND
	bs.player_id = 201939 AND
	gh.game_date > '2017/10/01'
ORDER BY gh.game_date DESC;