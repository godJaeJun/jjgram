from django.contrib import admin
from . import models

#클래스는 모델들이 어드민패널에서 어떻게 보이게 될지 결정한다.
#데코레이터는 항상 클래스 위에 적어야 한다. 안그러면 에러 발생...
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    #list_display_links는 클릭 시 수정 가능하게 한다. 쉼표가 없으면 에러 발생...
    list_display_links=(
        'location',
    )

    #검색창이 생긴다. location으로 검색할 수 있게 끔...
    search_fields=(
        'location',
    )

    #list_filter는 해당 컬럼으로 필터할 수 있음...
    list_filter=(
        'location',
        'caption'
    )
    #list_display는 어드민 패널에서 보여주고 싶은것을 다 보여 줄 수 있게 한다.
    list_display=(
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=(
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=(
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )