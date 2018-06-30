const _steph = 201939;
const _dubs = 1610612744;
const steph = {PlayerID: _steph};
const dubs = {TeamID: _dubs};
const game = {GameID: "0021401082"};


// Useful
it("#playerProfile", callMethod("playerProfile", steph));
it("#playerInfo", callMethod("playerInfo", steph));
it("#scoreboard", callMethod("scoreboard", {gameDate: "03/27/2015"})); // response says "GameDate is required" but it doesn't seem to work with uppercase first letter unlike every other parameter -- WTF.

// Potentially Useful
it("#playersInfo", callMethod("playersInfo"));

// Not Useful
it("#teamStats", callMethod("teamStats"));
it("#teamSplits", callMethod("teamSplits", dubs));
it("#teamYears", callMethod("teamYears"));
it("#playerSplits", callMethod("playerSplits", steph));
it("#shots", callMethod("shots", dubs));
it("#playByPlay", callMethod("playByPlay", game));
it("#teamHistoricalLeaders", callMethod("teamHistoricalLeaders", {TeamID: _dubs, SeasonID: "20078"}));
it("#teamInfoCommon", callMethod("teamInfoCommon", dubs));
it("#commonTeamRoster", callMethod("commonTeamRoster", dubs));
it("#teamPlayerDashboard", callMethod("teamPlayerDashboard", {TeamID: _dubs, SeasonType: "Regular Season"}));
it("#lineups", callMethod("lineups"));
it("#playerTracking", callMethod("playerTracking", {PtMeasureType: "CatchShoot"}));
it("#homepageV2", callMethod("homepageV2", {StatType: "Traditional", GameScope: "Season", PlayerScope: "All Players"}));
it("#assistTracker", callMethod("assistTracker"));
it("#playerStats", callMethod("playerStats"));
it("#playerClutch", callMethod("playerClutch", {ClutchTime: "Last 5 Minutes", AheadBehind: "Ahead or Behind", PointDiff: 5}));
it("#teamClutch", callMethod("teamClutch", {ClutchTime: "Last 5 Minutes", AheadBehind: "Ahead or Behind", PointDiff: 5}));
it("#playerShooting", callMethod("playerShooting"));
it("#teamShooting", callMethod("teamShooting"));
it("#boxScoreSummary", callMethod("boxScoreSummary", game));
it("#boxScore", callMethod("boxScore", game));
it("#leagueGameLog", callMethod("leagueGameLog", {PlayerOrTeam: "T"}));
it("#leagueLeaders", callMethod("leagueLeaders"));
it("#playerHustleLeaders", callMethod("playerHustleLeaders"));
it("#teamHustleLeaders", callMethod("teamHustleLeaders"));
it("#playerHustle", callMethod("playerHustle"));
it("#teamHustle", callMethod("teamHustle", { TeamID: _dubs }));
it("#leagueStandings", callMethod("leagueStandings"));
