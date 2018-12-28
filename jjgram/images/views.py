from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from . import models,serializers

#TEST 모든 이미지 불러오기
class ListAllImages(APIView):
    #APIView는 get이나 post나 사용자가 요청한대로 실행하는 능력을 가지고 있다.
    def get(self,request,format=None):#request = 클라이언트에게서 오브젝트를 요청하는 것
        #db의 모든 이미지 모델 안에 있는 모든 오브젝트 종류의 이미지를 가져와
        all_images=models.Image.objects.all()
        #이미지 시리얼 라이저는 단수다. 1개의 이미지를 시리얼 라이징하니까 그래서 한개가 아니라고 알려줘야함 many로!
        serializer= serializers.ImageSerializer(all_images,many=True)
        #return으로 인해 function은 종료된다. 시리얼라이즈의 데이터를 반환해라 
        return Response(data=serializer.data)

#TEST 모든 댓글 불러오기
class ListAllComments(APIView):
    def get(self,request,format=None):

        all_comments=models.Comment.objects.all()

        serializer=serializers.CommentSerializer(all_comments,many=True)

        return Response(data=serializer.data)

#TEST 모든 좋아요 불러오기
class ListAllLikes(APIView):
    def get(self,request,format=None):

        all_likes=models.Like.objects.all()

        serializer=serializers.LikeSerializer(all_likes,many=True)

        return Response(data=serializer.data)