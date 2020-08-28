from django.urls import path

from .views import ArticleAPIView,CommentAPIView,UsersAPIView,APIView

urlpatterns =[
    path("",ArticleAPIView.as_view(),name="api article"),
     path("commentapi",CommentAPIView.as_view(),name="api comment"),
      path("userapi",UsersAPIView.as_view(),name="api user"),
      path("thismyapi",APIView.as_view()),
]


