const util = require("util");
const NBA = require("nba");
const mysql = require('mysql');
const fs = require('fs');
const mkdirp = require('mkdirp');
const getDirName = require('path').dirname;
const moment = require('moment');
const persistToDatabase = require("./persistStat/persistToDatabase");

const API_DATE_FMT = 'MM/DD/YYYY';
const NBA_FOUNDED_DATE = '06/06/1946';
const NBA_SEASON_MONTHS = [1, 2, 3, 4, 5, 6, 10, 11, 12];
const PROMISES = [];
const _LAURI = 1628374;
const _BULLS = 1610612741;
const LAURI = {PlayerID: _LAURI};
const dubs = {TeamID: _BULLS};
const game = {GameID: "0021401082"};

const connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'nba'
});
connection.connect();

function persistToFile (filePathArray, payload) {
    const filePath = `${filePathArray.join('/')}.json`;
    const dirPath = getDirName(filePath);

    mkdirp(dirPath, function (err) {
        if (!err){
            fs.writeFile(filePath, JSON.stringify(payload), {
                flag: 'wx'
            }, (err) => {
                if (err) {
                    if (err.code != "EEXIST") {
                        console.log('Error writing to file system', err);
                    }
                }
            });
        } else {
            console.log(err);
        }
    });
}

/*
for (i in NBA.teams) {
    const team = NBA.teams[i];
    const teamExistsQuery = `SELECT * FROM nba.team WHERE id=${team.teamId};`;
    connection.query(teamExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            PROMISES.push(NBA.stats.teamInfoCommon({ TeamID: team.teamId }).then((response) => {
                const teamDetail = response.teamInfoCommon[0];
                persistToFile("teamDetail", teamDetail.teamId, response);
                persistToDatabase.saveTeamToDatabase(connection, teamDetail);
            }));

        }
    });
    PROMISES.push(NBA.stats.commonTeamRoster({ TeamID: team.teamId }).then((response) => {
        console.log(response);
        // persistToFile("teamDetail", teamDetail.teamId, response);
    }));
    break;
}
*/

// Retrieve and store the player details
for (i in NBA.players) {
    const player = NBA.players[i];
    const playerExistsQuery = `SELECT * FROM nba.player WHERE id=${player.playerId};`;
    connection.query(playerExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            /*
            PROMISES.push(NBA.stats.playerInfo({ PlayerID: player.playerId }).then((playerDetail) => {
                const playerId = playerDetail.commonPlayerInfo[0].personId;
                ersistToFile("playerDetail", playerId, playerDetail);
            }));
            */

            /*
            PROMISES.push(NBA.stats.playerProfile({ PlayerID: _LAURI }).then((result) => {
                persistToFile("playerProfile", playerId, playerDetail);
                {
                    seasonTotalsRegularSeason: [],
                    careerTotalsRegularSeason: [],
                    seasonTotalsPostSeason: [],
                    careerTotalsPostSeason: [],
                    seasonTotalsAllStarSeason: [],
                    careerTotalsAllStarSeason: [],
                    seasonTotalsCollegeSeason: [],
                    careerTotalsCollegeSeason: [],
                    seasonTotalsPreseason: [],
                    careerTotalsPreseason: [],
                    seasonRankingsRegularSeason: [],
                    seasonRankingsPostSeason: [],
                    seasonHighs: [],
                    careerHighs: [],
                    nextGame: []
                }
            }));
            */
        }
    });
}

/*
// Do this properly
Promise.all(PROMISES).then(function() {
    connection.end();
});
*/


let start = moment();
let fmtStart = start.format(API_DATE_FMT);
let dateInSeason = false;

//while (fmtStart != NBA_FOUNDED_DATE) {
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
    //}

/*
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
*/

connection.end();

/*

// Oct 17, 2017 – Jun 17, 2018

NBA.stats.commonTeamRoster({ TeamID: _BULLS }).then((response) => {
    console.log(response);
});

// Player Profile
NBA.stats.playerProfile({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});

// Shot charts
NBA.stats.shots({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});

// Box Scores
NBA.stats.boxScore({GameID: "0021401082"}).then((response) => {
    console.log(response);
});

// TeamID and SeasonID required
NBA.stats.teamHistoricalLeaders({ TeamID: _BULLS }).then((response) => {
    console.log(response);
});

// Shot charts
NBA.stats.shots({ PlayerID: _LAURI }).then((result) => {
    console.log(result);
});
*/
