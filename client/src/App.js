import React, { Component } from 'react';

// components
import Header from './components/Header';
import SearchForm from './components/SearchForm';
import PlayerInfo from './components/PlayerInfo';

class App extends Component {
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
