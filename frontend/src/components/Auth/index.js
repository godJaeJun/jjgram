import {connect} from "react-redux";//리덕스스토어에 연결 인덱스에서 로그인 회원가입 유저명 확인 등의 액션을 할거니까
import Container from "./container";

//Add all the actions for:
//Log in
//Sign up
//Recover password
//Check username
//Check password
//Check email

export default connect()(Container);