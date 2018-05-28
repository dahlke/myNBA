const util = require("util");
const NBA = require("nba");
const moment = require('moment');
const dbApi = require("./nba_stats/dbApi");
const fileApi = require("./nba_stats/fileApi");

const API_DATE_FMT = 'MM/DD/YYYY';
const NBA_FOUNDED_DATE = '06/06/1946';
const NBA_SEASON_MONTHS = [1, 2, 3, 4, 5, 6, 10, 11, 12];
let start = moment();
let fmtStart = start.format(API_DATE_FMT);
let dateInSeason = false;


/*

// TODO: first loop through all the NBA teams.

for (i in NBA.teams) {
    const team = NBA.teams[i];
    const teamExistsQuery = `SELECT * FROM nba.team WHERE id=${team.teamId};`;
    connection.query(teamExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            NBA.stats.teamInfoCommon({ TeamID: team.teamId }).then((response) => {
                const teamDetail = response.teamInfoCommon[0];
                persistToFile("teamDetail", teamDetail.teamId, response);
                dbApi.saveTeam(connection, teamDetail);
            });

        }
    });
    NBA.stats.commonTeamRoster({ TeamID: team.teamId }).then((response) => {
        console.log(response);
        // persistToFile("teamDetail", teamDetail.teamId, response);
    });
    break;
}
*/

/*
// Then store all the NBA players.
for (i in NBA.players) {
    const player = NBA.players[i];
    const playerExistsQuery = `SELECT * FROM nba.player WHERE id=${player.playerId};`;
    connection.query(playerExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            NBA.stats.playerInfo({ PlayerID: player.playerId }).then((playerDetail) => {
                const playerId = playerDetail.commonPlayerInfo[0].personId;
                ersistToFile("playerDetail", playerId, playerDetail);
            });

            // TODO playerProfile
        }
    });
}
*/

/*
while (fmtStart != NBA_FOUNDED_DATE) {
    fmtStart = start.format(API_DATE_FMT);
    dateInSeason = NBA_SEASON_MONTHS.includes(parseInt(start.format('MM')));
    if (dateInSeason) {
        NBA.stats.scoreboard({gameDate: fmtStart}).then((response) => {
            let gameHeaders = response.gameHeader;
            let gameLineScores = response.lineScore;
            let gameHeader, gameLineScore, gameLineScoreId;
            let year = start.format('YYYY');
            let month = start.format('MM');
            let day = start.format('DD');

            for (i in gameHeaders) {
                gameHeader = gameHeaders[i];
                persistToFile(["json", "gameHeader", year, month, day, gameHeader.gameId], gameHeader);
            }

            for (i in gameLineScores) {
                gameLineScore = gameLineScores[i];
                persistToFile(["json", "gameLineScore", year, month, day, gameLineScore.teamId], gameLineScore);
            }
        });
    }
    start = start.subtract({days: 1});
    // TODO: add some sleeping mechanism
}
*/
