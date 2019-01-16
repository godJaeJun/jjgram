import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import Ionicon from "react-ionicons";
import styles from "./styles.module.scss";

const Navigation = (props, context) => (
    <div className={styles.navigation}>
      <div className={styles.inner}>
        <div className={styles.column}>
          <Link to="/">
            <img
              src={require("images/logo.png")}
              className={styles.logo}
              alt={context.t("Logo")}
            />
          </Link>
        </div>
        <div className={styles.column}>
          <input
            type="text"
            placeholder={context.t("Search")}
            className={styles.searchInput}
          />
        </div>
        <div className={styles.column}>
          <div className={styles.navIcon}>
            <Link to="/explore">
              <Ionicon icon="ios-compass-outline" fontSize="28px" color="black" />
            </Link>
          </div>
          <div className={styles.navIcon}>
            <Ionicon icon="ios-heart-outline" fontSize="28px" color="black" />
          </div>
          <div className={styles.navIcon}>
            <Link to="/profile">
              <Ionicon icon="ios-person-outline" fontSize="32px" color="black" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
  //번역을 위해 설정한 것이다.
  Navigation.contextTypes = {
    t: PropTypes.func.isRequired
  };
  
  export default Navigation;
  