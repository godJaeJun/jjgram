from django.contrib import admin
from . import models

#notification admin을 생성한다.
@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=(
        'creator',
        'to',
        'notifications_type',
    )