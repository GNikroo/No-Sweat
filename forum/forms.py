"""..."""
from django_summernote.widgets import SummernoteInplaceWidget
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """..."""
    class Meta:
        """..."""
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """..."""
    class Meta:
        """..."""
        model = Post
        fields = [
            'title',
            'featured_image',
            'content',
        ]
        widgets = {
            'bar': SummernoteInplaceWidget(),
        }


class UpdateForm(forms.ModelForm):
    """..."""
    class Meta:
        model = Post
        fields = [
            'title',
            'featured_image',
            'content',
        ]
        widgets = {
            'bar': SummernoteInplaceWidget(),
        }


class UpdateCommentForm(forms.ModelForm):
    """..."""
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {
            'bar': SummernoteInplaceWidget(),
        }
