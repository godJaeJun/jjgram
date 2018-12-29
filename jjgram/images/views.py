from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
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

#좋아요
class LikeImage(APIView):
    def post(self,request,image_id,format=None):    #겟를 이용해서 이미지 like하기 바디를 바꾸지 않기 때문에 postX
        
        user=request.user

        #try except로 이미지가 있을 경우 가지고 오고, 없는 경우 404에러를 띄운다.
        try:
            found_image=models.Image.objects.get(id=image_id) #url로 호출한 이미지 id값을 가져온다.
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like=models.Like.objects.get(  #이미 좋아요 된 경우를 확인
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        
        except models.Like.DoesNotExist:
            #좋아요를 생성한다 url을 요청한 유저를 creator로 url에 포함되어 있는 이미지를 image로 설정한다.
            new_like=models.Like.objects.create(        
            creator=user,
            image=found_image
        )

        new_like.save() #생성된 내용을 저장한다.

        return Response(status=status.HTTP_201_CREATED)

#좋아요 취소
class UnLikeImage(APIView):
    
    def delete(self,request,image_id,format=None):
        
        user=request.user

        #try except로 이미지가 있을 경우 가지고 오고, 없는 경우 404에러를 띄운다.
        try:
            found_image=models.Image.objects.get(id=image_id) #url로 호출한 이미지 id값을 가져온다.
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like=models.Like.objects.get(  #이미 좋아요 된 경우를 확인
                creator=user,
                image=found_image
            )
            preexisiting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


#댓글 달기
class CommentOnImage(APIView):
    
    def post(self,request,image_id,format=None):

        user=request.user #요청한 유저명을 가지고온다.
        serializer=serializers.CommentSerializer(data=request.data) #json데이터를 파이썬이 이해할 수 있게

        try:
            found_image=models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():   #유효성을 검증한다. 쓸수있나?
            serializer.save(creator=user,image=found_image)

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Comment(APIView):
    def delete(self,request,comment_id,format=None):
        
        user=request.user
        try:
            #댓글 ID는 URL이어야하고 생성자는 현재 삭제를 요청하는 유저와 같아야 한다! 남의 댓글 못지우게
            comment=models.Comment.objects.get(id=comment_id,creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


      