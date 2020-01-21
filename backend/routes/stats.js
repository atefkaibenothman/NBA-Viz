var express = require('express');
var router = express.Router();
var db = require('../pgpool');

router.get('/', function (req, res, next) {
    const player_id = req.query.id;

    if (player_id == undefined) {
        res.send('Must enter a player id');
    }
    else {
        async function begin() {
            let data = {};
            let teamData = await getTeamID();
            let commonData = await getPlayerCommonInfo();
            let gameLogData = await getPlayerGameLogs();
            data['teamData'] = teamData;
            data['commonData'] = commonData;
            data['gameLogData'] = gameLogData;
            return data;
        }

        begin()
            .then(function (data) {
                res.send(data);
                console.log('api successfully sent data');
            })
    }

    async function getTeamID() {
        var pool = db.getPool();
        var team_id = await pool.query(`select team_id from player where player_id=${player_id}`);
        team_id = team_id.rows['0']['team_id'].toString();
        var result = await pool.query(`select * from team where team_id=${team_id}`);
        return result.rows;
    }

    async function getPlayerCommonInfo() {
        var pool = db.getPool();
        var result = await pool.query(`select * from player where player_id=${player_id}`);
        return result.rows;
    }

    async function getPlayerGameLogs() {
        var pool = db.getPool();
        var result = await pool.query(`select * from gamestats where player_id=${player_id}`);
        return result.rows;
    }
});

module.exports = router;
