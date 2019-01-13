//import

//actions

//action creators

//intitial state
const initialState={
    //localStorage란 브라우저에 저장하는 쿠키 같은 것. jwt가 없으면 false
    //redux thunk의 역할 : api에 request로 아이디와 비번을 보내서 맞으면 true로 변하게하고 틀리면 false로 유지시키는 역할
    isLoggedIn:localStorage.getItem("jwt")||false
};
//reducer
function reducer(state=initialState,action){
    switch(action.type){
        default:
            return state;
    }
}
//reducer functions

//exports

//reducer export
export default reducer;