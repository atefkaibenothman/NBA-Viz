import React, { Component } from 'react';

// components
import PlayerCommonInfo from '../components/PlayerCommonInfo';
import PlayerGameInfo from '../components/PlayerGameInfo';

class PlayerInfo extends Component {
    render() {
        let common_info = this.props.player_data['data']['common_info'];
        let game_logs = this.props.player_data['data']['game_logs'];

        return (
            <div>
                <div>
                    <div>
                        <PlayerCommonInfo cinfo={{ data: common_info }} />
                        <PlayerGameInfo gamelogs={{ data: game_logs }} />
                    </div>
                </div>
            </div >
        );
    }

}

export default PlayerInfo;