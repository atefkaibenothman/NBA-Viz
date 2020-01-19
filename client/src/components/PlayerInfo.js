import React, { Component } from 'react';

// components
import PlayerCommonInfo from '../components/PlayerCommonInfo';
import PlayerGameInfo from '../components/PlayerGameInfo';

class PlayerInfo extends Component {
    render() {
        return (
            <div>
                <div>
                    <div>
                        <PlayerCommonInfo />
                        <PlayerGameInfo />
                    </div>
                </div>
            </div >
        );
    }

}

export default PlayerInfo;