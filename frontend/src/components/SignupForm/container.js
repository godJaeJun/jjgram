import React, {Component} from "react";
import SignupForm from "./presenter";

class Container extends Component{
    state={
        email:"",
        fullname:"",
        username:"",
        password:""
    }
    render(){
        const {email,fullname,username,password}=this.state;
        return <SignupForm 
        handleSubmit={this._handleSubmit}
        handleInputChange={this._handleInputChange} 
        handleFacebookLogin={this._handleFacebookLogin}
        emailValue={email}
        fullnameValue={fullname}
        usernameValue={username} 
        passwordValue={password}
        />
    }
    //아이디나 비밀번호 입력시의 이벤트 name은 username이나 password에 value자신이 입력한 값이 들어간다.
    _handleInputChange=event=>{
        const {target:{value,name}}=event;
        this.setState({
            [name]:value
        });
    };
    //로그인 submit클릭시 반응없게 하기
    _handleSubmit=event=>{
        event.preventDefault();
        console.log(this.state)
        //redux will be here
    }

    _handleFacebookLogin=response=>{
        console.log(response);
    }
}

export default Container;