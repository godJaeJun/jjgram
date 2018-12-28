from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from . import models,serializers

class Feed(APIView):
    def get(self,request,format=None):
        user=request.user #요청한 유저명

        following_users=user.following.all()#많은 유저를 가지고 있다.

        image_list=[] # 많은 이미지가 들어갈 수 있는 리스트


        for following_user in following_users:
            user_images=following_user.images.all()[:2]  #팔로잉한 유저의 이미지를 가져온다 2개만...

            for image in user_images:
                image_list.append(image) #이미지 리스트에 불러온 이미지들을 넣어준다.

        #정렬을 한다. key= return값을 기준으로 파이썬이 정렬을 한다. reverse는 거꾸로 람다식으로 하면 편함...
        sorted_list=sorted(image_list,key=lambda image: image.created_at,reverse=True)

        #시리얼라이저로 출력가능하게 만듬 json 데이터로 
        serializer=serializers.ImageSerializer(sorted_list,many=True)

        return Response(serializer.data)

class LikeImage(APIView):
    def get(self,request,image_id,format=None):
        
        print(image_id)

        return Response(status=200)