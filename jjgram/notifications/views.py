from rest_framework.views import APIView
from rest_framework.response import Response#엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from rest_framework import status #status 상태를 확인하는 클래스
from . import models,serializers

class Notifications(APIView):

    def get(self,request,format=None):

        user=request.user

        #나에 대한 알림을 가져온다.
        notifications=models.Notification.objects.filter(to=user)

        serializer=serializers.NotificationSerializer(notifications,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

#알림을 API로 줄수없기 때문에 function생성
def create_notification(creator,to,notifications_type,image=None,comment=None):

    Notification= models.Notification.objects.create(
        creator=creator,
        to=to,
        notifications_type=notifications_type,
        image=image,
        comment=comment
    )

    Notification.save()