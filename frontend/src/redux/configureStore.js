import {createStore,combineReducers} from "redux";
import users from 'redux/modules/users';

//합치기 첫번째 리듀서는 유저 여기서 더많은 리듀서를 작성하면 된다. 여기에 라우팅 미들웨어 등도 많이 입력할 것.
const reducer = combineReducers({
    users,
})

//store를 생성한다 리듀서로 합쳐서 한개의 스토어 생성
let store=initialState=>createStore(reducer);

export default store();