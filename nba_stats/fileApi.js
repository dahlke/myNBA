const fs = require('fs');
const mkdirp = require('mkdirp');
const getDirName = require('path').dirname;

function persistJSON (filePathArray, payload) {
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


module.exports = {
    persistJSON: persistJSON
}
