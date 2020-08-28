from rest_framework import generics
from articles.models import Comment,Artical
from users.models import CustomUser
from .serializers import ArticleSerializer,CommentSerializer,UsersSerializer
from django.views.generic import TemplateView
# Create your views here.
class ArticleAPIView(generics.ListAPIView):
    queryset = Artical.objects.all()
    serializer_class = ArticleSerializer

class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UsersAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer

class APIView(TemplateView):
    template_name ="myapi.html"
