from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from jjgram.users import models as user_models
from jjgram.images import models as image_models

class Notification(image_models.TimeStampeModel):

    TYPE_CHOICES=(
        ('like','Like'),    #여기서 두번째는 어드민 패널 첫번째는 데이터베이스를 위해서 쓰는 것이다.
        ('comment','Comment'),
        ('follow','Follow')
    )

    #원래 같은 모델에 두개의 같은 foreignkey를 사용하면 에러발생
    #장고 2.0이상에서부터는 외부의 모델을 foreignkey로 받아올때 on_delete를 꼭 써줘야한다.
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,related_name='creator')  
    to = models.ForeignKey(user_models.User,on_delete=models.PROTECT,related_name='to')
    #creator는 주는 사람 to는 받는사람
    notifications_type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    #choices=Type_CHOICES인것은 팔로잉 이나 그런 알람종류가 있기 때문
    image=models.ForeignKey(image_models.Image,on_delete=models.PROTECT,null=True,blank=True)
    comment=models.TextField(null=True,blank=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return 'From: {} - To: {}'.format(self.creator,self.to)

