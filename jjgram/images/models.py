from django.db import models

#타임 스태프는 날짜이다. abstract timestamp model생성
class TimeStampeModel(models.Model):
    #생성된 날짜와 시간, auto_now_add는 처음 생성됬을 경우 자동으로 날짜 생성
    created_at= models.DateTimeField(auto_now_add=True)
    #업데이트 된 날짜와 시간, auto_now는 변경될때마다 날짜를 자동으로 불러온다.
    updated_at= models.DateTimeField(auto_now=True)

    #Meta class abstract=True로 바꿔주면 TimeStampModel이 abstract model이 된다.
    #이 모델은 데이터베이스를 생성하기 위해 사용되지 않는다. 대신 다른모델들의 base로 사용된다.
    class Meta:
        abstract=True 

class Image(TimeStampeModel):
    #올린 이미지 파일의 정보
    file=models.ImageField()
    #위치정보
    location=models.CharField(max_length=140)
    #캡션정보
    caption=models.TextField()

#댓글 모델 생성
class Comment(TimeStampeModel):
    #댓글에 대한 내용
    message=models.TextField()
    