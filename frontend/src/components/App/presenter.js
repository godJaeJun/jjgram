import React, { Component } from 'react';
import style from './styles.scss';
import Footer from 'components/Footer';

class App extends Component {
  render() {
    return (
      <div className={style.app}>
      <Footer/>
      </div>
    );
  }
}

export default App;
