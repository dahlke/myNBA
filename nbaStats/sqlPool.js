const mysql = require('mysql');

// TODO: config file
const HOST = 'localhost';
const USER = 'root';
const PASSWORD = '';
const DATABASE = 'nba';

const pool = mysql.createPool({
    host: HOST,
    user: USER,
    password: PASSWORD,
    database: DATABASE
});

function getConnection(callback) {
    pool.getConnection(function(err, connection) {
        callback(err, connection);
    });
};

module.exports = {
    getConnection: getConnection
};
