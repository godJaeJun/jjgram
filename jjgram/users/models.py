from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

#AbstractUser를 상속 받기 때문에 모든 필드를 정의하지 않아도 된다.
class User(AbstractUser):

    #코멘트 넣기
    """ User Model """

    #GENDER_CHOICES를 통해서 성별을 제한을 둔다.
    GENDER_CHOICES=(
        ('male','Male'),
        ('female','Female'),
        ('not-specified','Not specified')
    )

    #null=True는 현재 변화한 데이터 이전의 올드 멤버에게 디폴트로 null값을 주는 것
    #max_length는 길이 제한을 두고, choices는 선택가능하게 한다.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website=models.URLField(null=True)
    bio=models.TextField(null=True)
    phone=models.CharField(max_length=140,null=True)
    gender=models.CharField(max_length=80,choices=GENDER_CHOICES,null=True)
    #followers생성 자기 자신과 연결 "self"
    followers=models.ManyToManyField("self")
    #following생성 여러 유저가 팔로잉 할 수 있으니까 self로 설정한다.
    following=models.ManyToManyField("self")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

