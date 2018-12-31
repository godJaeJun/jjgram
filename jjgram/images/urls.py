from django.urls import path
from . import views

app_name="images"
#장고 2. 이상부터는 path를 사용한다. 밑에는 /all로 들어갈 경우 view는 클래스이기 때문에 as_view로 뷰를 보여준다. 
urlpatterns = [
    path("",view=views.Images.as_view(),name="feed"), 
    path("<int:image_id>/",view=views.ImageDetail.as_view(),name="detail_image"), 
    path("<int:image_id>/likes",view=views.LikeImage.as_view(),name="like_image"),
    path("<int:image_id>/unlikes",view=views.UnLikeImage.as_view(),name="like_image"),
    path("<int:image_id>/comments",view=views.CommentOnImage.as_view(),name="comment_image"),
    path("<int:image_id>/comments/<int:comment_id>",view=views.ModerateComment.as_view(),name="moderate_comment"),
    path("comments/<int:comment_id>",view=views.Comment.as_view(),name="comment"),
    path("search/",view=views.Search.as_view(),name='search'),
]
