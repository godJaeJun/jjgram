import React from "react";
import "./index.scss";

const Auth = (props, context) => (
    <main className="Auth">
      <div className="Column">
        <img src={require("images/phone.png")} className="Column-child" alt="Checkout our app. Is cool" />
      </div>
      <div className="Column">
        <div className="White-box-child-formBox">
          <img  src={require("images/logo.png")} className="White-box-child-formBox-img" alt="Logo" />
        </div>
        <div className="White-box-child">
        </div>
        <div className="App-box">
          <span>Get the app</span>
          <div className="App-box-appstores">
            <img
              src={require("images/ios.png")}
              className="App-box-appstores-img"
              alt="Download it on the Apple Appstore"
            />
            <img
              src={require("images/android.png")}
              className="App-box-appstores-img"
              alt="Download it on the Apple Appstore"
            />
          </div>
        </div>
      </div>
    </main>
  );

export default Auth;