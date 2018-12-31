from rest_framework import serializers
from . import models
from jjgram.images import serializers as images_serializers
#유저 프로필 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImageSerializer(many=True,read_only=True)
    #밑에 세개는 수정안되게 읽기만 가능하게 수정
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    class Meta:
        model=models.User 
        fields=(
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images'
        )

#유저 정보 시리얼라이저
class ListUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.User
        fields=(
            'id',
            'profile_image',
            'username',
            'name',
        )

