from rest_framework import serializers
from . import models
from jjgram.images import serializers as images_serializers
#유저 프로필 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):

    images=images_serializers.UserProfileImageSerializer(many=True)

    class Meta:
        model=models.User 
        fields=(
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

