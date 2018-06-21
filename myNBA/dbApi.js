const pool = require("./memsqlPool").pool;

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

        pool.getConnection((err, connection) => {
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

        pool.getConnection((err, connection) => {
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

function saveGameLineScore (gameLineScore) {
    if (gameLineScore) {
        pool.getConnection((err, connection) => {
            const insertQuery = `
                INSERT INTO nba.game_team_line_score VALUES (
                    ${gameLineScore.gameId},
                    ${gameLineScore.teamId},
                    ${gameLineScore.ptsQtr1},
                    ${gameLineScore.ptsQtr2},
                    ${gameLineScore.ptsQtr3},
                    ${gameLineScore.ptsQtr4},
                    ${gameLineScore.ptsOt1},
                    ${gameLineScore.ptsOt2},
                    ${gameLineScore.ptsOt3},
                    ${gameLineScore.ptsOt4},
                    ${gameLineScore.ptsOt5},
                    ${gameLineScore.ptsOt6},
                    ${gameLineScore.ptsOt7},
                    ${gameLineScore.ptsOt8},
                    ${gameLineScore.ptsOt9},
                    ${gameLineScore.ptsOt10},
                    ${gameLineScore.pts},
                    ${gameLineScore.fgPct},
                    ${gameLineScore.fg3Pct},
                    ${gameLineScore.ftPct},
                    ${gameLineScore.ast},
                    ${gameLineScore.reb},
                    ${gameLineScore.tov}
                ) ON DUPLICATE KEY UPDATE points=points;
            `;

            console.log(insertQuery);
            connection.query(insertQuery, (error, results, fields) => {
                connection.release();
                if (error) {
                    if (error.code != "ER_DUP_ENTRY") {
                        throw error;
                    } else {

                    }
                }
            });
        });
    }
}

function saveGameHeader (gameHeader) {
    if (gameHeader) {
        pool.getConnection((err, connection) => {
            const insertQuery = `
                INSERT INTO nba.game_header VALUES (
                    ${gameHeader.gameId},
                    "${gameHeader.gameDateEst}",
                    ${gameHeader.homeTeamId},
                    ${gameHeader.visitorTeamId},
                    "${gameHeader.natlTvBroadcasterAbbreviation}"
                ) ON DUPLICATE KEY UPDATE game_date=game_date;
            `;

            connection.query(insertQuery, function (error, results, fields) {
                connection.release();
                if (error) {
                    if (error.code != "ER_DUP_ENTRY") {
                        throw error;
                    } else {

                    }
                }
            });
            // TODO: why doesn't this release at the end
        });
    }
}


module.exports = {
    saveTeam: saveTeam,
    savePlayer: savePlayer,
    saveGameLineScore: saveGameLineScore,
    saveGameHeader: saveGameHeader
}
