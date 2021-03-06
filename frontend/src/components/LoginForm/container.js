import React, {Component} from "react";
import PropTypes from "prop-types"
import LoginForm from "./presenter";


class Container extends Component{
    state={
        username:"",
        password:""
    }
    static propTypes={
        facebookLogin:PropTypes.func.isRequired,
        usernameLogin:PropTypes.func.isRequired
    }
    render(){
        const {username,password}=this.state;
        return <LoginForm 
        handleSubmit={this._handleSubmit}
        handleInputChange={this._handleInputChange} 
        handleFacebookLogin={this._handleFacebookLogin}
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
        const {usernameLogin}=this.props;
        const {username,password}=this.state;
        event.preventDefault();
        usernameLogin(username,password);
    }

    _handleFacebookLogin=response=>{
        const {facebookLogin}=this.props;
        facebookLogin(response.accessToken);
    }
}

export default Container;