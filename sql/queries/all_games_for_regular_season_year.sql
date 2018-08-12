WITH season_dates AS (
	SELECT
		*
	FROM season
	WHERE regular_season_start > "1979-01-01"
	ORDER BY regular_season_start ASC
	LIMIT 1
)
SELECT
	*
FROM
	game_header gh,
	season_dates sd
WHERE
	gh.game_date BETWEEN sd.regular_season_start AND sd.regular_season_end;