from django.urls import path

from .views import (ArticleAPIView,ArticleDetailAPIView,
CommentAPIView,CommentDeailAPIView,
UsersAPIView,UsersDetailAPIView,
APIView)

urlpatterns =[
    path("",ArticleAPIView.as_view(),name="api article"),
    path("<int:pk>/",ArticleDetailAPIView.as_view()),
    path("commentapi",CommentAPIView.as_view(),name="api comment"),
    path("<int:pk>/",CommentDeailAPIView.as_view(),),
    path("userapi",UsersAPIView.as_view(),name="api user"),
    path("<int:pk>/",UsersDetailAPIView.as_view()),
    path("thismyapi",APIView.as_view()),
]


