//import

//actions

//action creators

//intitial state
const intitialState={
    //localStorage란 브라우저에 저장하는 쿠키 같은 것. jwt가 없으면 false
    isLoggedIn:localStorage.getItem("jwt")||false
};
//reducer
function reducer(state=intitialState,action){
    switch(action.type){
        default:
            return state;
    }
}
//reducer functions

//exports

//reducer export
export default reducer;