import React, { Component } from "react";
import CommentBox from "./presenter";

class Container extends Component {
  state={
    comment:""
  }
  render() {
    return <CommentBox 
    {...this.state}
    {...this.props}
    handleInputChange={this._handleInputChange}
    handleKeyPress={this._handleKeyPress}/>;
  }
  _handleInputChange=event=>{
    const {target :{value}}=event;
    this.setState({
      comment:value
    });
  };
  _handleKeyPress=event=>{
    const {submitComment}=this.props;
    const {comment} =this.state;
    const {key}=event;
    if(key==="Enter"){
      event.preventDefault();//Enter 무효화 자바스크립트에게 디폴트행동을 하지 말라고 한다.
      submitComment(comment);
    }
  }
}

export default Container;