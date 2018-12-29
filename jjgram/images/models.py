from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager
from jjgram.users import models as user_models
#models를 두게 불러오면 충돌이 생기기 때문에 as를 사용하여 닉네임을 줘야한다.
#타임 스태프는 날짜이다. abstract timestamp model생성

@python_2_unicode_compatible
class TimeStampeModel(models.Model):
    #생성된 날짜와 시간, auto_now_add는 처음 생성됬을 경우 자동으로 날짜 생성
    created_at= models.DateTimeField(auto_now_add=True)
    #업데이트 된 날짜와 시간, auto_now는 변경될때마다 날짜를 자동으로 불러온다.
    updated_at= models.DateTimeField(auto_now=True)

    #Meta class abstract=True로 바꿔주면 TimeStampModel이 abstract model이 된다.
    #이 모델은 데이터베이스를 생성하기 위해 사용되지 않는다. 대신 다른모델들의 base로 사용된다.
    class Meta:
        abstract=True 

@python_2_unicode_compatible
class Image(TimeStampeModel):

    """ Image Model """

    #올린 이미지 파일의 정보
    file=models.ImageField()
    #위치정보
    location=models.CharField(max_length=140)
    #캡션정보
    caption=models.TextField()
    #이미지를 생성한 생성자
    creator=models.ForeignKey(user_models.User,on_delete=models.CASCADE,null=True,related_name='images')
    #해시태그 검색을 위한 태그 추가
    tags=TaggableManager()

    @property #모델의 필드인데 데이터로 가지는 않지만 모델 안에 존재한다.
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    #해당 로케이션과 캡션을 admin페이지에서 보여주게 한다. 다른거 클릭 시 내용 확인.
    def __str__(self):
        return '{} - {}'.format(self.location,self.caption)

    class Meta:
        ordering=['-created_at']    #이미지가 생성된 날짜순으로 정렬되게 한다.

#댓글 모델 생성
@python_2_unicode_compatible
class Comment(TimeStampeModel):

    """ Comment Model """

    #댓글에 대한 내용
    message=models.TextField()
    #댓글을 생성한 생성자 
    creator=models.ForeignKey(user_models.User,on_delete=models.CASCADE,null=True)
    #어떤 이미지에 댓글이 달렸나 확인. related_name은 image와 연결된 댓글을 찾을 때 사용 comment_set을 comments로 변경
    image=models.ForeignKey(Image,on_delete=models.CASCADE,null=True,related_name='comments')

    def __str__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampeModel):

    """ Like Model """

    #누가 좋아요를 눌렀나. 장고 2버전 이상부터는 on_delete가 필수로 들어가게 된다.
    creator=models.ForeignKey(user_models.User,on_delete=models.CASCADE,null=True)
    #어떤 이미지에 좋아요를 눌렀나 확인.
    image=models.ForeignKey(Image,on_delete=models.CASCADE,null=True,related_name='likes')

    def __str__(self):
        return 'User : {} - Image Caption : {}'.format(self.creator.username,self.image.caption)