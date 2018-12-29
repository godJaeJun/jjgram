from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
from . import models,serializers

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

    def get(self,request,username,format=None):

        try:
            found_user= models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

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

