from rest_framework import serializers
from . import models
from jjgram.users import models as user_models

#유저 프로필 이미지 시리얼라이저 여기에 생성하는 이유는 양쪽에서 부르고 부르고 할 수 없다.
class CountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Image
        fields=(
            'id',
            'file',
            'comment_count',
            'like_count',
        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=user_models.User
        fields=(
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):
    
    creator=FeedUserSerializer(read_only=True)  #creator는 생성할 수 없고 읽기만 가능...

    class Meta:
        model=models.Comment #모델은 Comment를 가지고 온다.
        fields=(
            'id',
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):

    #image= ImageSerializer()    
    #nasted serializer로 좋아요 시리얼라이즈가 이미지 시리얼라이즈를 가지고 있다.(이미지의 모든 정보)

    class Meta:
        model=models.Like   #Like모델을 가지고 온다.
        fields='__all__'

class ImageSerializer(serializers.ModelSerializer):

    #시리얼라이즈의 데이터를 보고 싶을 때 ... 이렇게 하면 오류 발생 comment와 like가 먼저 정의 되지 않았기 때문에...
    comments=CommentSerializer(many=True)
    creator=FeedUserSerializer()

    class Meta:
        model=models.Image # 모델은 이미지 모델을 가지고 오고
        fields=(
            'id',
            'file',
            'location',
            'caption',
            'comments',  #어떤 댓글이 이 이미지에 댓글을 달았는 가
            'like_count',     #누가 좋아요를 눌렀는가
            'creator',
        ) 