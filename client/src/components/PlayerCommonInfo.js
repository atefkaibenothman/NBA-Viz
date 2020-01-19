import React, { Component } from 'react';

class PlayerCommonInfo extends Component {
    render() {
        return (
            <div>
                <div className="commoninfodiv">
                    <div>
                        <h4 className="inline">First Last</h4>
                        <h6 className="inline">#15</h6>
                    </div>
                    <div>
                        <p className="teamname">Team Name</p>
                        <p className="playerid">Player ID</p>
                    </div>
                </div>
            </div>
        );
    }
}

export default PlayerCommonInfo;