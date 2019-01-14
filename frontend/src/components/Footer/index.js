import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

class Footer extends React.Component{
  static contextTypes={
    t: PropTypes.func.isRequired //번역함수
  };
  render(){
    return(
      <footer className={styles.footer}>
        <div className={styles.column}>
          <nav className={styles.nav}>
           <ul className={styles.list}>
              <li className={styles.listItem}>{this.context.t("About Us")}</li>
              <li className={styles.listItem}>{this.context.t("Support")}</li>
              <li className={styles.listItem}>{this.context.t("Blog")}</li>
              <li className={styles.listItem}>{this.context.t("Press")}</li>
              <li className={styles.listItem}>{this.context.t("API")}</li>
              <li className={styles.listItem}>{this.context.t("Jobs")}</li>
              <li className={styles.listItem}>{this.context.t("Privacy")}</li>
              <li className={styles.listItem}>{this.context.t("Terms")}</li>
              <li className={styles.listItem}>{this.context.t("Directory")}</li>
              <li className={styles.listItem}>{this.context.t("Language")}</li>
            </ul>
          </nav>
        </div>
        <div className={styles.column}>
          <span className={styles.copyright}>© 2019 JJgram</span>
        </div>
      </footer>
    )
  }
}

export default Footer;