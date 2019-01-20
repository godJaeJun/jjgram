import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

const UserDisplay = (props, context) => (
  <div className={styles.container}>
    <div className={styles.column}>
      <img
        src={props.profile_image || require("images/noPhoto.jpg")}
        alt={props.user.username}
        className={props.big ? styles.bigAvatar : styles.avatar}
      />
      <div className={styles.user}>
        <span className={styles.username}>{props.user.username}</span>
        <span className={styles.name}>{props.user.name}</span>
      </div>
    </div>
    <span className={styles.column}>
      <button className={styles.button}>{context.t("Follow")}</button>
    </span>
  </div>
);

UserDisplay.contextTypes = {
  t: PropTypes.func.isRequired
};

UserDisplay.propTypes = {
  user: PropTypes.shape({
    profile_image: PropTypes.string,
    username: PropTypes.string.isRequired,
    name: PropTypes.string
  }).isRequired,
  big: PropTypes.bool
};

UserDisplay.defaultProps = {
  big: false
};

export default UserDisplay;