const fs = require('fs');
const dbApi = require("./myNBA/dbApi");


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

migratePlayersToDatabase(['json', 'apiPlayerInfo', 'commonPlayerInfo']);
migrateTeamsToDatabase(['json', 'apiTeamInfoCommon']);
