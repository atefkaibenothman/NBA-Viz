var pg = require('pg');

// database
let pool = new pg.Pool({
    host: 'localhost',
    user: 'kai',
    database: 'nba_db',
    password: '123',
    port: 5432
})

module.exports = {
    getPool: () => {
        return pool;
    }
}