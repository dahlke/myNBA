const util = require("util");
const NBA = require("nba");
const moment = require('moment');
const sqlPool = require('./myNBA/sqlPool');

const API_DATE_FMT = 'MM/DD/YYYY';
const NBA_FOUNDED_DATE = '06/06/1946';
const NBA_SEASON_MONTHS = [1, 2, 3, 4, 5, 6, 10, 11, 12];
const PROMISES = [];

const _LAURI = 1628374;
const _BULLS = 1610612741;
const LAURI = {PlayerID: _LAURI};
const dubs = {TeamID: _BULLS};
const game = {GameID: "0021401082"};

let start = moment();
let fmtStart = start.format(API_DATE_FMT);
let dateInSeason = false;

/*

// Scoreboard for a day
NBA.stats.scoreboard({gameDate: "03/27/2015"}).then((response) => {
    let year = start.format('YYYY');
    let month = start.format('MM');
    let day = start.format('DD');
    let gameHeaders = response.gameHeader;
    let gameLineScores = response.lineScore;
    let gameHeader, gameLineScore, gameLineScoreId;

    for (i in gameHeaders) {
        gameHeader = gameHeaders[i];
        persistToFile(["json", "gameHeader", year, month, day, gameHeader.gameId], gameHeader);
        break;
    }

    for (i in gameLineScores) {
        gameLineScore = gameLineScores[i];
        persistToFile(["json", "gameLineScore", year, month, day, gameLineScore.teamId], gameLineScore);
        break;
    }
});

NBA.stats.commonTeamRoster({ TeamID: _BULLS }).then((response) => {
    console.log(response);
});

NBA.stats.playerProfile({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});

NBA.stats.shots({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});

NBA.stats.boxScore({GameID: "0021401082"}).then((response) => {
    console.log(response);
});

NBA.stats.teamHistoricalLeaders({ TeamID: _BULLS }).then((response) => {
    console.log(response);
});

NBA.stats.shots({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});

sqlPool.getConnection((err, connection) => {
    console.log(err, connection);
    const playerExistsQuery = `SELECT id FROM nba.player WHERE id=${_LAURI};`;
    connection.query(playerExistsQuery, function (error, results, fields) {
        connection.release();
    });
});

*/
