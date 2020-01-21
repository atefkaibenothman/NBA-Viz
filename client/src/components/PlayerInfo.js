import React, { Component } from 'react';

// components
import PlayerCommonInfo from '../components/PlayerCommonInfo';
import PlayerGameInfo from '../components/PlayerGameInfo';
import TeamCommonInfo from '../components/TeamCommonInfo';

class PlayerInfo extends Component {
    render() {
        let team_common_info = this.props.player_data['data']['teamData'];
        let player_common_info = this.props.player_data['data']['commonData'];
        let game_logs = this.props.player_data['data']['gameLogData'];
        // console.log(common_info);
        // console.log(game_logs);

        return (
            <div>
                <div>
                    <div>
                        <div className="grid">
                            <PlayerCommonInfo cinfo={{ data: player_common_info }} />
                            <TeamCommonInfo tcinfo={{ data: team_common_info }} />
                        </div>
                        <div>
                            <PlayerGameInfo gamelogs={{ data: game_logs }} />
                        </div>
                    </div>
                </div>
            </div >
        );
    }

}

export default PlayerInfo;