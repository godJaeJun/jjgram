from django.contrib import admin
from . import models

#클래스는 모델들이 어드민패널에서 어떻게 보이게 될지 결정한다.
#데코레이터는 항상 클래스 위에 적어야 한다. 안그러면 에러 발생...
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass 

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass