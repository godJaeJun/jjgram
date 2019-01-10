import React from 'react';
import ReactDOM from 'react-dom';
import 'index.css';
import {Provider} from 'react-redux';
import store from 'redux/configureStore'//스토어에서는 히스토리도 불러온다.
import App from 'App';
import 'react-app-polyfill/ie9'; // For IE 9-11 support
import 'react-app-polyfill/ie11'; // For IE 11 support

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>
    , document.getElementById('root'));

