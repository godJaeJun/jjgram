from django.views.generic import View 
from django.http import HttpResponse
from django.conf import settings
import os 

class ReactAppView(View):#View에서 확장됨 

    def get(self,request):#request를 받을 때마다 파일을 열라고 한다. 어떤파일? 밑의 경로
        try:
            with open(os.path.join(str(settings.ROOT_DIR),'frontend','build','index.html')) as file:
                return HttpResponse(file.read())
        
        except:
            return HttpResponse(#파일을 못찾을 경우
                """
                index.html not found! build your React app!!
                """,
                status=501,
            )