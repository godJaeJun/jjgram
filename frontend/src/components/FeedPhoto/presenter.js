import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import PhotoActions from "components/PhotoActions";

const FeedPhoto = (props, context) => {
    return (
      <div className={styles.feedPhoto}>
        <header>
          <img
            src={props.creator.profile_image || require("images/noPhoto.jpg")}
            alt={props.creator.username}
          />
          <div>
            <span>{props.creator.username}</span>
            <span>{props.location}</span>
          </div>
        </header>
        <img src={props.file} alt={props.caption} />
        <div>
          <PhotoActions number={props.like_count} />
        </div>
      </div>
    );
  };

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