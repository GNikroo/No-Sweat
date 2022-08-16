'''Views for No Sweat fitforum'''
from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    '''a list view of nine posts per page'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
