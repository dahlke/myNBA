const util = require("util");
const NBA = require("nba");
const moment = require('moment');
const dbApi = require("./nbaStats/dbApi");
const fileApi = require("./nbaStats/fileApi");

const API_RATE_LIMIT_WAIT_SECS = 5 * 1000;
const API_DATE_FMT = 'MM/DD/YYYY';
const NBA_FOUNDED_DATE = '06/06/1946';
const NBA_SEASON_MONTHS = [1, 2, 3, 4, 5, 6, 10, 11, 12];
let start = moment();
let fmtStart = start.format(API_DATE_FMT);
let dateInSeason = false;

/*


// TODO: Check if already on filesystem and in database.
console.log("Beginning NBA Data API download.");
for (i in NBA.teams) {
    const team = NBA.teams[i];
    NBA.stats.teamInfoCommon({ TeamID: team.teamId }).then((response) => {
        const teamDetail = response.teamInfoCommon[0];
        fileApi.persistJSON(["json", "apiTeamInfoCommon", "teamDetail", teamDetail.teamId], response);
        // dbApi.saveTeam(connection, teamDetail);
    });
}
*/


function requestPlayer (playerId)  {
    NBA.stats.playerInfo({ PlayerID: playerId }).then((playerDetail) => {
        const playerId = playerDetail.commonPlayerInfo[0].personId;
        fileApi.persistJSON(["json", "apiPlayerInfo", "commonPlayerInfo", playerId], playerDetail);
    });
}

function requestScoreboard (gameDate)  {
    NBA.stats.scoreboard({gameDate: gameDate}).then((response) => {
        let gameHeaders = response.gameHeader;
        let gameLineScores = response.lineScore;
        let gameHeader, gameLineScore, gameLineScoreId;
        let year = start.format('YYYY');
        let month = start.format('MM');
        let day = start.format('DD');

        for (i in gameHeaders) {
            gameHeader = gameHeaders[i];
            fileApi.persistJSON(["json", "apiScoreboard", "gameHeader", year, month, day, gameHeader.gameId], gameHeader);
        }

        for (i in gameLineScores) {
            gameLineScore = gameLineScores[i];
            fileApi.persistJSON(["json", "apiScoreboard", "gameLineScore", year, month, day, gameLineScore.teamId], gameLineScore);
        }
    });
}

function loopPlayers() {
    for (i in NBA.players) {
        const player = NBA.players[i];
        console.log(`Requesting player info for ${player.fullName}...`);
        requestPlayer(player.playerId);
    }
}

function loopScoreboards() {
    fmtStart = start.format(API_DATE_FMT);
    dateInSeason = NBA_SEASON_MONTHS.includes(parseInt(start.format('MM')));
    if (dateInSeason) {
        console.log(`Requesting Scoreboards for ${fmtStart}`);
        setTimeout(() => {
            requestScoreboard(fmtStart);
            start = start.subtract({days: 1});
            if (fmtStart != NBA_FOUNDED_DATE) {
                loopScoreboards();
            }
        }, API_RATE_LIMIT_WAIT_SECS);
    }
}


function main() {
    // TODO: Check all if already on filesystem and in database.
    // loopScoreboards();
    loopPlayers();
}

main();
