'''Models for No Sweat fitforum'''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    '''post details'''
    title = models.CharField(max_length=29, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=44, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='forum_likes', blank=True)

    class Meta:
        '''meta class sets descending order'''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        '''generates the number of likes per post'''
        return self.likes.count()
