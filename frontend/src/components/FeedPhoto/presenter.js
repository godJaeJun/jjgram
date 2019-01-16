import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import PhotoActions from "components/PhotoActions";
import PhotoComments from "components/PhotoComments";
import TimeStamp from "components/TimeStamp";
import CommentBox from "components/CommentBox";

const FeedPhoto = (props, context) => {
    return (
      <div className={styles.feedPhoto}>
        <header className={styles.header}>
          <img
            src={props.creator.profile_image || require("images/noPhoto.jpg")}
            alt={props.creator.username}
            className={styles.image}
          />
          <div className={styles.headerColumn}>
            <span className={styles.creator}>{props.creator.username}</span>
            <span className={styles.location}>{props.location}</span>
          </div>
        </header>
        <img src={props.file} alt={props.caption} />
        <div className={styles.meta}>
          <PhotoActions number={props.like_count} />
          <PhotoComments
            caption={props.caption}
            creator={props.creator.username}
            comments={props.comments}
          />
          <TimeStamp time={props.natural_time}/>
          <CommentBox/>
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
    natural_time:PropTypes.string.isRequired
}
export default FeedPhoto;