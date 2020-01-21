import React, { Component } from 'react';

class TeamCommonInfo extends Component {
    render() {
        let city = "City";
        let team_name = "teamName";
        let team_abr = "teamAbr";
        let team_id = "teamID";
        let team_conference = "teamConference";
        let team_division = "teamDivision";
        let team_wins = "Wins";
        let team_loses = "Loses";

        if (this.props.tcinfo.data === undefined) {
            console.log('tcinfo is undefined');
        }
        else {
            let data = this.props.tcinfo.data['0'];
            city = data['team_city'];
            team_name = data['team_name'];
            team_abr = data['team_abr'];
            team_id = data['team_id'];
            team_conference = data['team_conference'];
            team_division = data['team_division'];
            team_wins = data['team_wins'];
            team_loses = data['team_loses'];
        }

        return (
            <div className="teamcommoninfodiv">
                <h4><span className="team-name">{city}</span><span className="team-name">{team_name}</span><span className="team-name">({team_abr})</span></h4>
                <p><span className="team-atr">{team_id}</span><span className="team-atr">{team_conference}</span><span className="team-atr">{team_division}</span></p>
                <p className="team-atr-bot"><span>{team_wins}</span> / <span>{team_loses}</span></p>
            </div>
        );
    }
}

export default TeamCommonInfo;