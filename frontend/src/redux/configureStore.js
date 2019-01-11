import {createStore,combineReducers,applyMiddleware} from "redux";
import thunk from "redux-thunk"
import user from 'redux/modules/user';

const middlewares=[thunk];

const reducer=combineReducers({
    user
})

let store=initalState=>createStore(reducer,applyMiddleware(...middlewares));

export default store();