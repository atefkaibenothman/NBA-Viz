var express = require('express');
var router = express.Router();
var db = require('../pgpool');

router.get('/', function (req, res, next) {
    const player_id = req.query.id;
    let data = {};

    if (player_id == undefined) {
        res.send('Must enter a player id');
    }
    else {
        var pool = db.getPool();
        pool.query(`select player_id, lname, fname, position, team_abr from player where player_id=${player_id}`, (err, table) => {
            if (err) {
                console.log(err);
            }
            else {
                console.log(`succesfully fetched common player info for player: ${player_id}`);
                data['common_info'] = table.rows;
            }
        });
        pool.query(`select * from gamestats where player_id=${player_id}`, (err, table) => {
            if (err) {
                console.log(err);
            }
            else {
                console.log(`succesfully fetched player game logs for player: ${player_id}`);
                data['game_logs'] = table.rows;

                res.send(data);
            }
        })
    }
});

module.exports = router;
