import React from 'react';
import {Route,Switch} from "react-router-dom";//스위치는 둘 중에 하나만 보여주는 기능을 한다.
import style from './styles.scss';
import Footer from 'components/Footer';

//key는 array를 리턴할때마다 키의 숫자가 필요하다.
const App=props=>[
    //Nav,
    props.isLoggedIn?<PrivateRoutes key={2}/> : <PublicRoutes key={2}/>,//로그인 되어있으면 PrivateRoutes로 아니면 Public으로...
    <Footer key={3}/>
]

const PrivateRoutes=props=>(
    <Switch>
        <Route exact path="/" render={()=>"feed"}/>
        <Route exact path="/explore" render={()=>"explore"}/>
    </Switch>
)

const PublicRoutes=props=>(
    <Switch>
        <Route exact path="/" render={()=>"login"}/>
        <Route exact path="/forgot" render={()=>"password"}/>
    </Switch>
)
export default App;
