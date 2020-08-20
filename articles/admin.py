from django.contrib import admin

from .models import Artical,Comment

class CommentInline(admin.TabularInline):
    model = Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInline
    ]
admin.site.register(Artical)
admin.site.register(Comment)
