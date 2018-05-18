const util = require("util");
const NBA = require("nba");
const mysql = require('mysql');

const curry = NBA.findPlayer('Stephen Curry');

/* logs the following:
{
  firstName: 'Stephen',
  lastName: 'Curry',
  playerId: 201939,
  teamId: 1610612744,
  fullName: 'Stephen Curry',
  downcaseName: 'stephen curry'
}
*/
function savePlayer (connection, playerRawInfo) {
    var playerInfo = playerInfo.commonPlayerInfo[0];
    var insertQuery = `
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
        ${playerInfo.jersey},
        "${playerInfo.position}",
        ${playerInfo.fromYear},
        ${playerInfo.toYear},
        "${playerInfo.dleagueFlag}",
        ${playerInfo.draftYear},
        ${playerInfo.draftRound},
        ${playerInfo.draftNumber}
    );`;
}

function savePlayerSimple (connection, player) {
    var insertQuery = `
    INSERT INTO nba.player_simple VALUES (
        ${player.playerId},
        "${player.firstName}",
        "${player.lastName}",
        ${player.teamId}
    );`;

    connection.query(insertQuery, function (error, results, fields) {
        if (error) {
            if (error.code != 'ER_DUP_ENTRY') {
                throw error;
            }
        }
    });
}

function saveTeam (connection, team) {
    var insertQuery = `
    INSERT INTO nba.team VALUES (
        ${team.teamId},
        "${team.simpleName}",
        "${team.abbreviation}",
        "${team.location}"
    );`;

    connection.query(insertQuery, function (error, results, fields) {
        if (error) {
            console.log(player);
            throw error;
        }
    });
}


var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'nba'
});
connection.connect();

for (player_index in NBA.players) {
    player = NBA.players[player_index];
    console.log(`Saving player (simple): ${player.firstName} ${player.lastName}`);
    savePlayerSimple(connection, player);
    // NBA.stats.playerInfo({ PlayerID: player.playerId }).then(savePlayer);
}

/*

for (team_index in NBA.teams) {
    const team = NBA.teams[team_index];
    console.log(`Saving team: ${team.simpleName}`);
    saveTeam(connection, team);
}

*/

connection.end();
