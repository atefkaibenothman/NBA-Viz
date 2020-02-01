import React, { Component } from 'react';

class PlayerGameInfo extends Component {
    render() {
        let data = {};
        if (this.props.gamelogs.data !== undefined) {
            data = this.props.gamelogs.data;
        }

        // <ul>
        //     {Object.keys(data).map(function (key) {
        //         return <li key={data[key]['game_id']}>{data[key]['game_date']} -- {data[key]['mp']} -- {data[key]['pts']} -- {data[key]['ast']} -- {data[key]['tot_reb']}</li>
        //     })}
        // </ul>

        return (
            <div className="gameinfodiv">
                <ul>
                </ul>
                <table className="table table-sm table-bordered">
                    <thead className="thead-dark">
                        <tr>
                            <th scope="col">date</th>
                            <th scope="col">matchup</th>
                            <th scope="col">W/L</th>
                            <th scope="col">mp</th>
                            <th scope="col">points</th>
                            <th scope="col">blocks</th>
                            <th scope="col">rebounds</th>
                            <th scope="col">steals</th>
                        </tr>
                    </thead>
                    <tbody>
                        {Object.keys(data).map(function (key) {
                            return <tr key={data[key]['game_id']}>
                                <th>{data[key]['game_date']}</th>
                                <th>{data[key]['matchup']}</th>
                                <th>{data[key]['winlose']}</th>
                                <th>{data[key]['mp']}</th>
                                <th>{data[key]['pts']}</th>
                                <th>{data[key]['blk']}</th>
                                <th>{data[key]['tot_reb']}</th>
                                <th>{data[key]['stl']}</th>
                            </tr>
                        })}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default PlayerGameInfo;