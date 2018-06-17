const sqlPool = require("./sqlPool");

function saveTeam (teamRawJson) {
    const team = teamRawJson.teamInfoCommon[0];
    if (team) {
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
            ) ON DUPLICATE KEY UPDATE name=name
        `;

        sqlPool.getConnection((err, connection) => {
            connection.query(insertQuery, function (error, results, fields) {
                connection.release();
                if (error) {
                    if (error.code != "ER_DUP_ENTRY") {
                        throw error;
                    }
                } else {

                }
            });
            // TODO: why doesn't this release at the end
        });
    }
}

function savePlayer (playerDetail) {
    if (playerDetail) {
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
            ) ON DUPLICATE KEY UPDATE first_name=first_name;
        `;

        sqlPool.getConnection((err, connection) => {
            connection.query(insertQuery, function (error, results, fields) {
                connection.release();
                if (error) {
                    if (error.code != "ER_DUP_ENTRY") {
                        throw error;
                    }
                } else {

                }
            });
            // TODO: why doesn't this release at the end
        });
    } else {
        console.log(playerDetail);
    }

}

function saveGameLineScore (connection, gameLineScore) {

}

function saveGameHeader (connection, gameHeader) {

}


module.exports = {
    saveTeam: saveTeam,
    savePlayer: savePlayer,
    saveGameLineScore: saveGameLineScore,
    saveGameHeader: saveGameHeader
}
