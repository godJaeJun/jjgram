from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

    class Meta:
        model=models.Image # 모델은 이미지 모델을 가지고 오고
        fields='__all__' #필드는 전체 필드를 가지고 온다.
class CommentSerializer(serializers.Serializer):

    class Meta:
        model=models.Comment #모델은 Comment를 가지고 온다.
        fields='__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model=models.Like   #Like모델을 가지고 온다.
        fields='__all__'