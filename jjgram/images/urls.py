from django.urls import path
from . import views

app_name="images"
#장고 2. 이상부터는 path를 사용한다. 밑에는 /all로 들어갈 경우 view는 클래스이기 때문에 as_view로 뷰를 보여준다. 
urlpatterns = [
    path("",view=views.Feed.as_view(),name="feed"), 
    path("<int:image_id>/like",view=views.LikeImage.as_view(),name="like_image")
]
