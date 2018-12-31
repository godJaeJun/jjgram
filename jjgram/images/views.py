from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
from . import models,serializers
from jjgram.users import serializers as user_serializers
from jjgram.users import models as user_models
from jjgram.notifications import views as notification_views #상황에 맞게 알림이 떠야하기 때문에 가지고옴.


class Feed(APIView):
    def get(self,request,format=None):
        user=request.user #요청한 유저명

        following_users=user.following.all()#많은 유저를 가지고 있다.

        image_list=[] # 많은 이미지가 들어갈 수 있는 리스트


        for following_user in following_users:
            user_images=following_user.images.all()[:2]  #팔로잉한 유저의 이미지를 가져온다 2개만...

            for image in user_images:
                image_list.append(image) #이미지 리스트에 불러온 이미지들을 넣어준다.

        #내이미지도 불러온다.
        my_images=user.images.all()[:2]

        for image in my_images:

            image_list.append(image)

        #정렬을 한다. key= return값을 기준으로 파이썬이 정렬을 한다. reverse는 거꾸로 람다식으로 하면 편함...
        sorted_list=sorted(image_list,key=lambda image: image.created_at,reverse=True)

        #시리얼라이저로 출력가능하게 만듬 json 데이터로 
        serializer=serializers.ImageSerializer(sorted_list,many=True)

        return Response(serializer.data)

#좋아요
class LikeImage(APIView):
    #좋아요를 누른사라 확인하기
    def get(self,request,image_id,format=None):
        
        likes=models.Like.objects.filter(image__id=image_id)

        #좋아요를 누른 사람을 찾아낸다.
        like_creators_ids=likes.values('creator_id')
        #array안에 있는 유저를 검색한다.
        users=user_models.User.objects.filter(id__in=like_creators_ids)

        serializer=user_serializers.ListUserSerializer(users,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
     
    #좋아요를 누르기
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

        #좋아요 알림...
        notification_views.create_notification(user,found_image.creator,'like',found_image)

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

            #댓글 알림...
            notification_views.create_notification(user,found_image.creator,'comment',found_image,serializer.data['message'])

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

#hashtag 검색 
class Search(APIView):
    def get(self,request,format=None):
        hashtags=request.query_params.get('hashtags',None)

        if hashtags is not None:
            hashtags=hashtags.split(",")
            #여기서 __name__in은 deep relationship을 검색하는 방법이다. json안에 json을 검색할때 사용
            #exact : 정확하게 검색, contains : 포함(대소문자),  둘다 앞에 i를 붙이면 예) iexact,icontains를 하면 
            #대소문자를 구분 x in은 array가 있으면 array중에서 찾아내라 distinct 중복 x
            images=models.Image.objects.filter(tags__name__in=hashtags).distinct()

            serializer=serializers.CountImageSerializer(images,many=True)
       
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#내 글에 달린 댓글 삭제하기
class ModerateComment(APIView):
    def delete(self,request,image_id,comment_id,format=None):

        user=request.user 

        #해당이미지가 요청한 유저인지 확인하기
        try:
            #댓글아이디는 삭제할 댓글아이디, 이미지아이디는 댓글이 달린 게시물, 생성자는 image의 creator가 요청한 아이디인 경우
            comment_to_delete=models.Comment.objects.get(id=comment_id,image__id=image_id,image__creator=user)
            comment_to_delete.delete()
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)

class ImageDetail(APIView):
    
    #반복되는 일을 메소드로 압축 function이 class 안에 있기 때문에 self가 필요로하다.
    def find_own_image(self,image_id,user):
        try:
            image=models.Image.objects.get(id=image_id,creator=user)
            return image
        except models.Image.DoesNotExist:
             return None 

    def get(self,request,image_id,format=None):
        
        user=request.user 

        try:
            image=models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.ImageSerializer(image)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    #이미지를 변경한다.
    def put(self,request,image_id,format=None):
        
        user=request.user

        image=self.find_own_image(image_id,user)

        if image is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        #수정할 이미지를 시리얼라이저에 넣는다. partial를 사용하면 완료되지 않은 업데이트가 가능하다.
        #즉 3가지 모든 필드가 변경안되도 가능하다.
        serializer=serializers.InputImageSerializer(image,data=request.data,partial=True)

        #시리얼라이저가 유효하면
        if serializer.is_valid():
            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #이미지 삭제한다.
    def delete(self,request,image_id,format=None):
        
        user=request.user 

        image=self.find_own_image(image_id,user)

        if image is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        image.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

        