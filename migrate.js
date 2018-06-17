const fs = require('fs');
const dbApi = require("./nbaStats/dbApi");


function migratePlayersToDatabase(dirPathArray) {
    const dirPath = `${dirPathArray.join("/")}`;

    fs.readdirSync(dirPath).forEach(file => {
        const path = `${dirPath}/${file}`;
        const playerDataRaw = fs.readFileSync(path, 'utf8');
        const playerDataJson = JSON.parse(playerDataRaw);
        dbApi.savePlayer(playerDataJson);
    });
}

migratePlayersToDatabase(['json', 'apiPlayerInfo', 'commonPlayerInfo']);
