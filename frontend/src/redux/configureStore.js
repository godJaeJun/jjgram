import {createStore,combineReducers} from "redux";
import user from 'modules/user';

const reducer=combineReducers({
    user
})

let store=initalState=>createStore(reducer);

export default store();