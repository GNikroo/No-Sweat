'''Views for No Sweat fitforum'''
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm, UpdateForm, UpdateCommentForm


class Search(View):
    """..."""
    def get(self, request):
        """..."""
        query = request.GET.get('query', '')

        if query:
            posts = Post.objects.all().filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(label__icontains=query))  # noqa
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
    queryset = Post.objects.all().order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


class UserPostList(View):
    '''a list view of six posts per page'''
    def get(self, request):
        queryset = Post.objects.all()

        if queryset:
            posts = Post.objects.filter(author=request.user.id).order_by('-created_on')  # noqa

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


class TagSearch(View):
    def get(self, request):
        """..."""
        queryset = request.GET.get('queryset', '')
        posts = Post.objects.filter(Q(label__icontains=queryset))

        return render(
            request,
            "tag_search.html",
            {
                "queryset": queryset,
                "posts": posts,
                "tag_request": True,
            },
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
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post_form.post = post
            post_form.save()
            messages.success(request, "Your post has been added!")
        else:
            post_form = PostForm()
            messages.error(request, 'Invalid form submission.')

        return HttpResponseRedirect('/user_profile')


class UpdatePost(View):
    '''...'''
    def get(self, request, *args, **kwargs):
        '''...'''
        slug = kwargs.get('slug')
        post_to_update = Post.objects.get(slug=slug)
        update_form = UpdateForm(initial={
            'title': post_to_update.title,
            'featured_image': post_to_update.featured_image,
            'content': post_to_update.content,
        })

        return render(
            request,
            'update_post.html',
            {
                'update_form': update_form,
            },
        )

    def post(self, request, *args, **kwargs):
        """..."""
        slug = kwargs.get('slug')
        post_object = Post.objects.get(slug=slug)
        update_form = UpdateForm(request.POST, request.FILES, instance=post_object)  # noqa
        if update_form.is_valid():
            update_form.instance.author = request.user
            post = update_form.save(commit=False)
            post.slug = slugify(post.title)
            update_form.post = post
            update_form.save()
            messages.success(request, "Your post has been updated!")
        else:
            update_form = UpdateForm()
            messages.error(request, 'Invalid form submission.')

        return HttpResponseRedirect('/user_profile')


class DeletePost(View):
    '''...'''
    def get(self, request, *args, **kwargs):
        '''...'''
        return render(
            request,
            'delete_post.html',
        )

    def post(self, request, *args, **kwargs):
        """..."""
        slug = kwargs.get('slug')
        post_to_delete = Post.objects.get(slug=slug)
        post_to_delete.delete()
        messages.success(request, 'Your post has been deleted.')
        return HttpResponseRedirect('/user_profile')


class UpdateComment(View):
    '''...'''
    def get(self, request, **kwargs):
        '''...'''
        comment_id = kwargs.get('pk')
        comment_obj = Comment.objects.get(pk=comment_id)
        update_comment_form = UpdateCommentForm(initial={
            'body': comment_obj.body,
        })

        return render(
            request,
            'update_comment.html',
            {
                'update_comment_form': update_comment_form,
            },
        )

    def post(self, request, **kwargs):
        """..."""
        slug = kwargs.get('slug')
        comment_id = kwargs.get('pk')
        comment_obj = Comment.objects.get(pk=comment_id)
        update_comment_form = UpdateCommentForm(request.POST, instance=comment_obj)  # noqa
        if update_comment_form.is_valid():
            if comment_obj.owner == request.user:
                update_comment_form.instance.owner = request.user
                comment_obj = update_comment_form.save(commit=False)
                update_comment_form.comment = comment_obj
                update_comment_form.save()
                messages.success(request, "Your comment has been updated!")
        else:
            update_comment_form = UpdateCommentForm()
            messages.error(request, 'Invalid form submission.')

        return HttpResponseRedirect(f"/{slug}")


class DeleteComment(View):
    '''...'''
    def get(self, request, *args, **kwargs):
        '''...'''
        return render(
            request,
            'delete_comment.html',
        )

    def post(self, request, *args, **kwargs):
        """..."""
        slug = kwargs.get('slug')
        comment_id = kwargs.get('pk')
        comment_to_delete = Comment.objects.get(pk=comment_id)
        comment_to_delete.delete()
        messages.success(request, 'Your comment has been deleted.')
        return HttpResponseRedirect(f'/{slug}')


class PostDetail(View):
    '''shows the user important post details'''

    def get(self, request, slug, *args, **kwargs):
        '''method to request important post details'''
        queryset = Post.objects.all()
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
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Your comment has been added!")
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
