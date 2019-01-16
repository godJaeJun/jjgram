import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

const FeedPhoto= (props,context)=>{
    console.log(props);
    return <div className={styles.feedPhoto}>hello!</div>
}

//shape는 오브젝트의 모습
FeedPhoto.propTypes={
    creator:PropTypes.shape({
        profile_image:PropTypes.string, //없는 경우가 있기에 is Required를 안붙인다.
        username:PropTypes.string.isRequired
    }).isRequired,
    location:PropTypes.string.isRequired,
    file:PropTypes.string.isRequired,
    like_count:PropTypes.number.isRequired,
    caption:PropTypes.string.isRequired,
    comments:PropTypes.arrayOf(
        PropTypes.shape({
            message:PropTypes.string.isRequired,
            creator:PropTypes.shape({
                profile_image:PropTypes.string, 
                username:PropTypes.string.isRequired
            }).isRequired
        })
    ).isRequired,
    created_at:PropTypes.string.isRequired
}
export default FeedPhoto;