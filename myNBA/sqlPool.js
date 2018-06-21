const mysql = require('mysql');

const HOST = '127.0.0.1';
const USER = 'root';
const PASSWORD = '';
const DATABASE = 'nba';

const pool = mysql.createPool({
    connectionLimit: 1000,
    host: '127.0.0.1',
    user: 'root',
    password: '',
    database: 'nba'
});

module.exports = {
    pool: pool
};
