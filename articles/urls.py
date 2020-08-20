from django.urls import path
from .views import (
    ArticalListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,

)

urlpatterns = [
    path('',ArticalListView.as_view(),name="article_list"),
    path("<int:pk>/edit/",ArticleUpdateView.as_view(),name="article_edit"),
    path("<int:pk>/",ArticleDetailView.as_view(),name="article_detail"),
    path("<int:pk>/delete/",ArticleDeleteView.as_view(),name="article_delete"),
    path("new/",ArticleCreateView.as_view(),name="article_new")

]

