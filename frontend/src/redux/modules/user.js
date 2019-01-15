//import

//actions
//토큰을 저장시켜줌.
const SAVE_TOKEN="SAVE_TOKEN";

//action creators
//token=내가 저장하고 싶은 토큰
function saveToken(token){
    return{
        type:SAVE_TOKEN,
        token
    }
}

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
        .then(json=>{
            if(json.token){
                localStorage.setItem("jwt",json.token)
                dispatch(saveToken(json.token));
            }
        })
        .catch(err=>console.log(err));
    };
}

//intitial state
const initialState={
    //localStorage란 브라우저에 저장하는 쿠키 같은 것. jwt가 없으면 false
    //redux thunk의 역할 : api에 request로 아이디와 비번을 보내서 맞으면 true로 변하게하고 틀리면 false로 유지시키는 역할
    isLoggedIn:localStorage.getItem("jwt")?true:false
};
//reducer
function reducer(state=initialState,action){
    switch(action.type){
        case SAVE_TOKEN:
            return applySetToken(state,action);
        default:
            return state;
    }
}
//reducer functions
function applySetToken(state,action){
    const {token}=action;
    return{
        ...state,
        isLoggedIn:true,
        token
    }
}
//exports

const actionCreators={
    facebookLogin
};

export {actionCreators};
//reducer export
export default reducer;
