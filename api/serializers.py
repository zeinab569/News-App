from rest_framework import serializers
from articles.models import Comment,Artical
from users.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ("title","body","date","author")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id","article","comment","author")

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","username","email","age")