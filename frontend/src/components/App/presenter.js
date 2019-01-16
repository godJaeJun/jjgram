import React from 'react';
import Proptypes from 'prop-types';
import {Route,Switch} from "react-router-dom";//스위치는 둘 중에 하나만 보여주는 기능을 한다.
import './styles.scss';
import Footer from 'components/Footer';
import Auth from 'components/Auth';
import Navigation from "components/Navigation";
import Feed from "components/Feed";
//key는 array를 리턴할때마다 키의 숫자가 필요하다.
const App=props=>[
    props.isLoggedIn?<Navigation key={1}/>:null,
    props.isLoggedIn?<PrivateRoutes key={2}/> : <PublicRoutes key={2}/>,//로그인 되어있으면 PrivateRoutes로 아니면 Public으로...
    <Footer key={3}/>
]

//props관리
App.propTypes={
    isLoggedIn:Proptypes.bool.isRequired
}

//로그인시
const PrivateRoutes=props=>(
    <Switch>
        <Route exact path="/" component={Feed}/>
        <Route exact path="/explore" render={()=>"explore"}/>
    </Switch>
)

//비로그인시
const PublicRoutes=props=>(
    <Switch>
        <Route exact path="/" component={Auth}/>
        <Route exact path="/forgot" render={()=>"password"}/>
    </Switch>
)
export default App;
