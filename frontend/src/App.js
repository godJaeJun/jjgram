import React, { Component } from 'react';
import style from './App.module.scss';

class App extends Component {
  render() {
    return (
      <div className={style.app}>
        <header className={style.appHeader}>
          <p>
            Hello <code>src/App.js</code> and save to reload.
          </p>
          <a
            className={style.appLink}
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
