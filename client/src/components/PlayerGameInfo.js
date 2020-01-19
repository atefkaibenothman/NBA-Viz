import React, { Component } from 'react';

class PlayerGameInfo extends Component {
    render() {
        let data = {};

        if (this.props.gamelogs.data !== undefined) {
            data = this.props.gamelogs.data;
        }

        return (
            <div className="gameinfodiv">
                <h5>Game Logs</h5>
                <ul>
                    {Object.keys(data).map(function (key) {
                        return <li key={data[key]['game_id']}>{data[key]['game_date']} -- {data[key]['mp']} -- {data[key]['pts']} -- {data[key]['ast']} -- {data[key]['tot_reb']}</li>
                    })}
                </ul>
            </div>
        );
    }
}

export default PlayerGameInfo;