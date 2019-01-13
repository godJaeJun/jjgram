import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import I18n from "redux-i18n";
import {ConnectedRouter} from "connected-react-router";//연결된 라우터를 불러온다.
import store, {history} from 'redux/configureStore'//스토어에서는 히스토리도 불러온다.
import { tranlations } from "translations";
import App from 'components/App';
import 'react-app-polyfill/ie9'; // For IE 9-11 support
import 'react-app-polyfill/ie11'; // For IE 11 support

//history={history}는 라우터에게 히스토리 오브젝트를 준다. 그래서 router와 middleware는 둘다 같은 동일한 히스토리 오브젝트를 갖게됨.
ReactDOM.render(
    <Provider store={store}>
        <ConnectedRouter history={history}>
            <I18n translations={tranlations} initialLang="en" fallbackLang="en">
                <App />
            </I18n>
        </ConnectedRouter>
    </Provider>, 
    document.getElementById('root')
);