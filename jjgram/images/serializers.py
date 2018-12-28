from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Comment #모델은 Comment를 가지고 온다.
        fields='__all__'#필드는 전체 필드를 가지고 온다.

class LikeSerializer(serializers.ModelSerializer):

    #image= ImageSerializer()    
    #nasted serializer로 좋아요 시리얼라이즈가 이미지 시리얼라이즈를 가지고 있다.(이미지의 모든 정보)

    class Meta:
        model=models.Like   #Like모델을 가지고 온다.
        fields='__all__'

class ImageSerializer(serializers.ModelSerializer):

    #시리얼라이즈의 데이터를 보고 싶을 때 ... 이렇게 하면 오류 발생 comment와 like가 먼저 정의 되지 않았기 때문에...
    comments=CommentSerializer(many=True)
    likes=LikeSerializer(many=True)

    class Meta:
        model=models.Image # 모델은 이미지 모델을 가지고 오고
        fields=(
            'id',
            'file',
            'location',
            'caption',
            'comments',  #어떤 댓글이 이 이미지에 댓글을 달았는 가
            'likes',     #누가 좋아요를 눌렀는가
        ) 