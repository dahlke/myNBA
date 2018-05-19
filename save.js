const util = require("util");
const NBA = require("nba");
const mysql = require('mysql');
const fs = require('fs');

const PROMISES = [];
const _LAURI = 1628374;
const _BULLS = 1610612741;

const connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'nba'
});
connection.connect();

// Library
// https://github.com/bttmly/nba

// Endpoints
// https://github.com/bttmly/nba/blob/master/doc/stats.md

/*

DONE:
nba.stats.teamInfoCommon(params) -> Promise
nba.stats.playerInfo(params) -> Promise

TODO:

nba.stats.assistTracker(params) -> Promise
nba.stats.commonTeamRoster(params) -> Promise
nba.stats.homepageV2(params) -> Promise
nba.stats.playByPlay(params) -> Promise
nba.stats.playerClutch(params) -> Promise
nba.stats.playerProfile(params) -> Promise
nba.stats.playerShooting(params) -> Promise
nba.stats.playerSplits(params) -> Promise
nba.stats.playerStats(params) -> Promise
nba.stats.playerTracking(params) -> Promise
nba.stats.scoreboard(params) -> Promise
nba.stats.shots(params) -> Promise
nba.stats.teamClutch(params) -> Promise
nba.stats.teamHistoricalLeaders(params) -> Promise
nba.stats.teamPlayerDashboard(params) -> Promise
nba.stats.teamShooting(params) -> Promise
nba.stats.teamSplits(params) -> Promise

*/

function saveToFile (prefix, id, payload) {
    const filePath = `json/${prefix}/${id}.json`;
    fs.writeFile(filePath, JSON.stringify(payload), (err) => {
        if (err) {
            console.log('Error writing to file system', err);
        }
    });
}

function savePlayerToDatabase (connection, playerDetail) {
    const playerInfo = playerDetail.commonPlayerInfo[0];
    const playerJersey = playerInfo.jersey || "NULL";
    const playerDraftYear = playerInfo.draftYear == "Undrafted" ? "NULL" : playerInfo.draftYear;
    const playerDraftRound = playerInfo.draftRound == "Undrafted" ? "NULL" : playerInfo.draftRound;
    const playerDraftNumber = playerInfo.draftNumber == "Undrafted" ? "NULL" : playerInfo.draftNumber;

    const insertQuery = `
    INSERT INTO nba.player VALUES (
        ${playerInfo.personId},
        "${playerInfo.firstName}",
        "${playerInfo.lastName}",
        ${playerInfo.teamId},
        "${playerInfo.birthdate}",
        "${playerInfo.school}",
        "${playerInfo.country}",
        "${playerInfo.lastAffiliation}",
        "${playerInfo.height}",
        "${playerInfo.weight}",
        ${playerInfo.seasonExp},
        ${playerJersey},
        "${playerInfo.position}",
        ${playerInfo.fromYear},
        ${playerInfo.toYear},
        "${playerInfo.dleagueFlag}",
        ${playerDraftYear},
        ${playerDraftRound},
        ${playerDraftNumber}
    ) ON DUPLICATE KEY UPDATE first_name=first_name;`;

    connection.query(insertQuery, function (error, results, fields) {
        if (error) {
            if (error.code != "ER_DUP_ENTRY") {
                console.log(insertQuery);
                throw error;
            }
        }
    });
}

function saveTeamToDatabase (connection, team) {
    var insertQuery = `
    INSERT INTO nba.team VALUES (
        ${team.teamId},
        "${team.seasonYear}",
        "${team.teamCity}",
        "${team.teamName}",
        "${team.teamAbbreviation}",
        "${team.teamConference}",
        "${team.teamDivision}",
        "${team.w}",
        "${team.l}",
        "${team.confRank}",
        "${team.divRank}",
        "${team.minYear}",
        "${team.maxYear}"
    ) ON DUPLICATE KEY UPDATE name=name`;

    connection.query(insertQuery, function (error, results, fields) {
        if (error) {
            console.log(insertQuery);
            console.log(error);
        }
    });
}

for (i in NBA.teams) {
    const team = NBA.teams[i];
    const teamExistsQuery = `SELECT * FROM nba.team WHERE id=${team.teamId};`;
    connection.query(teamExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            PROMISES.push(NBA.stats.teamInfoCommon({ TeamID: team.teamId }).then((response) => {
                const teamDetail = response.teamInfoCommon[0];
                saveToFile("teamDetail", teamDetail.teamId, teamDetail);
                saveTeamToDatabase(connection, teamDetail);
            }));
        }
    });
}

// Retrieve and store the player details
for (i in NBA.players) {
    const player = NBA.players[i];
    const playerExistsQuery = `SELECT * FROM nba.player WHERE id=${player.playerId};`;
    console.log(playerExistsQuery);
    connection.query(playerExistsQuery, function (error, results, fields) {
        if (results && results.length < 1) {
            PROMISES.push(NBA.stats.playerInfo({ PlayerID: player.playerId }).then((playerDetail) => {
                const playerId = playerDetail.commonPlayerInfo[0].personId;
                saveToFile("playerDetail", playerId, playerDetail);
                savePlayerToDatabase(connection, playerDetail);
            }));
        }
    });
}
/*
// Do this properly
Promise.all(PROMISES).then(function() {
    connection.end();
});
*/
