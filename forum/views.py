'''Views for No Sweat fitforum'''
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.text import slugify
from .models import Post
from .forms import CommentForm, PostForm


class Search(View):
    """..."""
    def get(self, request):
        """..."""
        query = request.GET.get('query', '')

        if query:
            posts = Post.objects.all().filter(Q(title__icontains=query) | Q(content__icontains=query)) # noqa
        else:
            posts = []

        return render(
            request,
            "index.html",
            {
                "query": query,
                "posts": posts,
                "searched": True,
            },
        )


class PostList(generic.ListView):
    '''a list view of six posts per page'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


class UserPostList(View):
    '''a list view of six posts per page'''
    def get(self, request):
        queryset = Post.objects.all()
        
        if queryset:
            posts = Post.objects.filter(author=request.user.id).order_by('-created_on') # noqa

        else:
            posts = []

        return render(
            request,
            "user_profile.html",
            {
                "queryset": queryset,
                "posts": posts,
            }
        )


class AddPost(View):
    '''...'''
    def get(self, request, *args, **kwargs):
        '''...'''
        post_form = PostForm()
        return render(
            request,
            'add_post.html',
            {
                'post_form': post_form,
            },
        )

    def post(self, request, *args, **kwargs):
        """..."""
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.status = 1
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post_form.post = post
            post_form.save()
        else:
            post_form = PostForm()

        return render(
            request,
            "add_post.html",
            {
                "posted": True,
            },
        )


class PostDetail(View):
    '''shows the user important post details'''

    def get(self, request, slug, *args, **kwargs):
        '''method to request important post details'''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        '''method to request important post details'''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class PostLike(View):
    """..."""
    def post(self, request, slug):
        """..."""
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
