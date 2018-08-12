SELECT
	*
FROM season
WHERE regular_season_start > "1979-01-01"
ORDER BY regular_season_start ASC
LIMIT 1;