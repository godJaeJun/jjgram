from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
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
    
    following=serializers.SerializerMethodField()

    class Meta:
        model=models.User
        fields=(
            'id',
            'profile_image',
            'username',
            'name',
            'following'
        )
    def get_following(self,obj):
        if 'request' in self.context:
            request=self.context['request']
            if obj in request.user.following.all():
                return True
        return False

class SignUpSerializer(RegisterSerializer):

    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
