import React, { Component } from 'react';
import { LineChart, Line, AreaChart, Area, Brush, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

class Graph extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        }
    }


    render() {
        const { data } = this.props.gamelogs;
        console.log(data);

        return (
            <div className="graph" >
                <h5>Mins Played</h5>
                <LineChart width={1250} height={200} data={data} syncId="anyId"
                    margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="game_date" />
                    <YAxis />
                    <Tooltip />
                    <Line type='monotone' dataKey='mp' stroke='#82ca9d' fill='#82ca9d' />
                </LineChart>
                <h5>Points</h5>
                <LineChart width={1250} height={200} data={data} syncId="anyId"
                    margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="game_date" />
                    <YAxis />
                    <Tooltip />
                    <Line type='monotone' dataKey='pts' stroke='#8884d8' fill='#8884d8' />
                </LineChart>
            </div >
        );
    }
} export default Graph;