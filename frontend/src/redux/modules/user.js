//import

//actions

//action creators

//API actions

function facebookLogin(access_token){
    return function(dispatch){
        fetch("/users/login/facebook/",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({//바디에서 JSON을 스트링으로 변환 json은 엑세스토큰임
                access_token
            }) 
        })
        .then(response=>response.json())//작업이 완료된 후 response입력.
        .then(json=>console.log(json))
        .catch(err=>console.log(err));
    };
}

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

const actionCreators={
    facebookLogin
};

export {actionCreators};
//reducer export
export default reducer;