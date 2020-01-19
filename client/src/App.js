import React, { Component } from 'react';

// components
import Header from './components/Header';
import SearchForm from './components/SearchForm';
import PlayerInfo from './components/PlayerInfo';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      game_logs: ""
    }
  }

  callBackend() {
    fetch('/users')
      .then(res => res.text())
      .then(res => this.setState({ game_logs: res }))
      .catch(err => err);
  }

  componentDidMount() {
    this.callBackend();
  }

  render() {
    return (
      <div>
        <Header />
        <SearchForm />
        <PlayerInfo />
      </div>
    );
  }
}

export default App;
