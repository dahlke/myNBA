const fs = require("fs");
const mkdirp = require("mkdirp");
const getDirName = require("path").dirname;

function syncJsonExists(filePathArray) {
    const filePath = `${filePathArray.join("/")}.json`;
    let exists = false;
    if (fs.existsSync(filePath)) {
        exists = true;
    }
    return exists;
}

function syncDirExists(dirPathArray) {
    const dirPath = `${dirPathArray.join("/")}`;
    let exists = false;
    if (fs.existsSync(dirPath)) {
        exists = true;
    }
    return exists;
}


function persistJSON (filePathArray, payload) {
    const filePath = `${filePathArray.join("/")}.json`;
    const dirPath = getDirName(filePath);

    mkdirp(dirPath, function (err) {
        if (!err){
            fs.writeFile(filePath, JSON.stringify(payload), {
                flag: "wx"
            }, (err) => {
                if (err) {
                    if (err.code != "EEXIST") {
                        console.error("Error writing to file system", err);
                    }
                }
            });
        } else {
            console.error(err);
        }
    });
}

module.exports = {
    persistJSON: persistJSON,
    syncJsonExists: syncJsonExists,
    syncDirExists: syncDirExists
}
