'''Admin for No Sweat fitforum'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''PostAdmin Class'''
    list_display = (
        'title', 'label', 'author', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''CommentAdmin Class'''
    list_display = ('name', 'post', 'body', 'created_on')
    search_fields = ['name', 'email', 'body']
