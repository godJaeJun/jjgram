from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
from . import models,serializers

#최근 가입한 5명의 유저 추천받기
class ExploreUsers(APIView):

    def get(self,request,format=None):
        
        last_five = models.User.objects.all().order_by('-date_joined')[:5]   #5명만 불러옴

        serializer=serializers.ExploreUserSerializer(last_five,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
