import {createStore,combineReducers,applyMiddleware} from "redux";
import thunk from 'redux-thunk';//리덕스 미들웨어 추가
import { createBrowserHistory } from "history";
import { composeWithDevTools } from "redux-devtools-extension";
import { connectRouter, routerMiddleware } from "connected-react-router";
import { i18nState } from "redux-i18n";
import users from 'redux/modules/users';
//히스토리는 내가 뒤로 가기를 눌렀을 때 페이지를 기억한다. 브라우저 히스토리를 사용한다.

//이건 node.js의 전체 정보를 갖고있는 variable이다. 현재상태가 dev인지 prob인지 확인
const env=process.env.NODE_ENV;

export const history = createBrowserHistory();//히스토리생성하기

const middlewares = [thunk, routerMiddleware(history)];//여기에 미들웨어를 넣을 것이다.(미들웨어 추가)

//만약 내환경이 dev라면 Redux logger를 부른다.
if (env === "development") {
    const { logger } = require("redux-logger");
    middlewares.push(logger);
  }

//합치기 첫번째 리듀서는 유저 여기서 더많은 리듀서를 작성하면 된다. 여기에 라우팅 미들웨어 등도 많이 입력할 것.
const reducer = history =>
  combineReducers({
    users,
    router: connectRouter(history),
    i18nState,
  });

let store;

if (env === "development") {
    store = initialState =>
      createStore(reducer(history),composeWithDevTools(applyMiddleware(...middlewares))
      );
  } else {
    store = initialState =>
       createStore(reducer(history), applyMiddleware(...middlewares));
  }
  
  export default store();
//store를 생성한다 리듀서로 합쳐서 한개의 스토어 생성
//applyMiddleware에 미들웨어를 넣어준다. ...array를 unpack한다.array가 thunk,router이렇게 된다.