from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
from . import models,serializers
from jjgram.notifications import views as notification_views #상황에 맞게 알림이 떠야하기 때문에 가지고옴.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

#최근 가입한 5명의 유저 추천받기
class ExploreUsers(APIView):

    def get(self,request,format=None):
        
        last_five = models.User.objects.all().order_by('-date_joined')[:5]   #5명만 불러옴

        serializer=serializers.ListUserSerializer(last_five,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

#팔로우 하기
class FollowUser(APIView):

    def post(self,request,user_id,format=None):
       
        user=request.user   #나

        try:
            user_to_follow=models.User.objects.get(id=user_id)  #url에서 팔로잉할 유저를 가져온다.
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)  #팔로우하기

        user.save() #저장

        #팔로우 알림...
        notification_views.create_notification(user,user_to_follow,'follow')

        return Response(status=status.HTTP_200_OK)

#팔로우 취소
class UnFollowUser(APIView):

    def post(self,request,user_id,format=None):
       
        user=request.user   #나

        try:
            user_to_follow=models.User.objects.get(id=user_id)  #url에서 팔로잉할 유저를 가져온다.
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_follow)  #팔로우하기

        user.save() #저장

        return Response(status=status.HTTP_200_OK)
    
#유저의 프로필 보기
class UserProfile(APIView):

    def get_user(self,username):

        try:
            found_user= models.User.objects.get(username=username)
            return found_user
        except models.User.DoesNotExist:
            return None 

    def get(self,request,username,format=None):
    
        found_user=self.get_user(username)

        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer=serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,username,format=None):

        user=request.user

        found_user=self.get_user(username)

        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        elif found_user.username != user.username : 
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            serializer=serializers.UserProfileSerializer(found_user,data=request.data,partial=True)
            
            #시리얼라이저가 유효하다면
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#해당유저의 팔로우 보기
class UserFollowers(APIView):

    def get(self,request,username,format=None):

        try:
            found_user= models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #해당유저의 팔로워를 가지고 온다.
        user_followers=found_user.followers.all()

        #시리얼라이저를 통해 해당 유저들을 json으로 바꾼다.
        serializer=serializers.ListUserSerializer(user_followers,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

#유저가 팔로잉한 유저들 보기
class UserFollowing(APIView):

    def get(self,request,username,format=None):

        try:
            found_user= models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #해당유저의 팔로잉을 가지고 온다.
        user_following=found_user.following.all()

        #시리얼라이저를 통해 해당 유저들을 json으로 바꾼다.
        serializer=serializers.ListUserSerializer(user_following,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

#유저명으로 검색하기
class Search(APIView):
    def get(self,request,format=None):
        
        username=request.query_params.get('username',None)

        if username is not None:
            #i를 통해서 대소문자를 구별하지 않고 contains를 사용하여 유저명이 포함된 것을 검색
            #변경함 istartswith으로 시작하는 것...oo으로 시작
            users=models.User.objects.filter(username__istartswith=username)

            serializer=serializers.ListUserSerializer(users,many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#비밀번호 변경 
class ChangePassword(APIView):

    def put(self,request,username,format=None):
        
        user=request.user

        if user.username==username:
            #현재 비밀번호를 입력받는다. 없으면 none
            current_password=request.data.get('current_password',None)

            if current_password is not None:
                #장고에서 디폴트로 있는 비밀번호체크 
                passwords_match=user.check_password(current_password)

                if passwords_match:
                    #새로운 비밀번호를 입력받는다. 없으면 none
                    new_password=request.data.get('new_password',None)

                    if new_password is not None:
                        user.set_password(new_password)

                        user.save()

                        return Response(status=status.HTTP_200_OK)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

#페이스북로그인
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter