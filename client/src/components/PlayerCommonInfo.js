import React, { Component } from 'react';

class PlayerCommonInfo extends Component {
    render() {
        let player_id = "Player ID";
        let lname = "Last";
        let fname = "First";
        let position = "Position";
        let team_abr = "Team abr";
        let jersey = "--";

        if (this.props.cinfo.data === undefined) {
            // console.log('cinfo is undefined');
        }
        else {
            let data = this.props.cinfo.data['0'];
            player_id = data['player_id'];
            lname = data['lname'];
            fname = data['fname'];
            position = data['position'];
            team_abr = data['team_abr'];
            jersey = data['jersey'];
        }

        return (
            <div>
                <div className="commoninfodiv">
                    <div>
                        <h4 className="inline">{fname} {lname}</h4>
                        <h6 className="inline">#{jersey}</h6>
                    </div>
                    <div>
                        <p className="statspan"><span className="teamname">{team_abr}</span><span className="playerpos">{position}</span></p>
                        <p className="playerid">{player_id}</p>
                    </div>
                </div>
            </div>
        );
    }
}

export default PlayerCommonInfo;