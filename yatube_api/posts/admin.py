from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Post, Comment, Group)
class PostAdmin(admin.ModelAdmin):
    pass
