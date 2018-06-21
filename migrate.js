const fs = require('fs');
const dbApi = require("./myNBA/dbApi");
const pool = require("./myNBA/sqlPool").pool;

function migratePlayersToDatabase(dirPathArray) {
    const dirPath = `${dirPathArray.join("/")}`;

    fs.readdirSync(dirPath).forEach(file => {
        const path = `${dirPath}/${file}`;
        const playerDataRaw = fs.readFileSync(path, 'utf8');
        const playerDataJson = JSON.parse(playerDataRaw);
        dbApi.savePlayer(playerDataJson);
    });
}

function migrateTeamsToDatabase(dirPathArray) {
    const dirPath = `${dirPathArray.join("/")}`;

    fs.readdirSync(dirPath).forEach(file => {
        const path = `${dirPath}/${file}`;
        const teamDataRaw = fs.readFileSync(path, 'utf8');
        const teamDataJson = JSON.parse(teamDataRaw);
        dbApi.saveTeam(teamDataJson);
    });
}

function migrateGameHeadersToDatabase(dirPathArray) {
    const dirPath = `${dirPathArray.join("/")}`;

    fs.readdirSync(dirPath).forEach(dir => {
        const yearPath = `${dirPath}/${dir}`;
        fs.readdirSync(yearPath).forEach(dir => {
            const monthPath = `${yearPath}/${dir}`;
            fs.readdirSync(monthPath).forEach(dir => {
                const dayPath = `${monthPath}/${dir}`;
                fs.readdirSync(dayPath).forEach(file => {
                    const gamePath = `${dayPath}/${file}`;
                    const gameHeaderDataRaw = fs.readFileSync(gamePath, 'utf8');
                    const gameHeaderDataJson = JSON.parse(gameHeaderDataRaw);

                    dbApi.saveGameHeader(gameHeaderDataJson);
                });
            });
        });
    });
}

// migratePlayersToDatabase(['json', 'apiPlayerInfo', 'commonPlayerInfo']);
migrateTeamsToDatabase(['json', 'apiTeamInfoCommon']);
// migrateGameLineScoresToDatabase(['json', 'apiScoreboard', 'gameHeader']);
//migrateGameHeadersToDatabase(['json', 'apiScoreboard', 'gameHeader']);
pool.end();
