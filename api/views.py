from rest_framework import generics
from articles.models import Comment,Artical
from users.models import CustomUser
from .serializers import ArticleSerializer,CommentSerializer,UsersSerializer
from django.views.generic import TemplateView
# Create your views here.
class ArticleAPIView(generics.ListCreateAPIView):
    queryset = Artical.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artical.objects.all()
    serializer_class = ArticleSerializer


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class CommentDeailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    


class UsersAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer

class UsersDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer

class APIView(TemplateView):
    template_name ="myapi.html"
