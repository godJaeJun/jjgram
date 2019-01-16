import React, {Component} from "react";
import PropTypes from "prop-types"
import Feed from "./presenter";

class Container extends Component{
    state={
        loading:true//일단 로딩
    };
    static propTypes={
        getFeed:PropTypes.func.isRequired
    };
    componentDidMount() {
        const {getFeed}=this.props;
        getFeed();
    }
    render(){
        return <Feed {...this.state}/>
    }
}

export default Container;