import React, { Component } from 'react';

// components
import Header from './components/Header';
import SearchForm from './components/SearchForm';
import PlayerInfo from './components/PlayerInfo';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      info: {}
    }

    this.updateState = this.updateState.bind(this);
  }

  updateState(data) {
    this.setState({
      info: data
    })
  }

  render() {
    return (
      <div>
        <Header />
        <SearchForm data={{ updateState: this.updateState }} />
        <PlayerInfo player_data={{ data: this.state.info }} />
      </div>
    );
  }
}

export default App;
