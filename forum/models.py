'''Models for No Sweat fitforum'''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    '''
    Post model.
    '''
    TAG_CHOICES = [
        ('healthy eating', 'Healthy Eating'),
        ('aerial', 'Aerial'),
        ('barre', 'Barre'),
        ('bootcamp', 'Bootcamp'),
        ('boxing', 'Boxing'),
        ('kickboxing', 'Kickboxing'),
        ('circuit training', 'Circuit training'),
        ('crossfit', 'Crossfit'),
        ('cycling', 'Cycling'),
        ('dance', 'Dance'),
        ('gym classes', 'Gym classes'),
        ('interval training', 'Interval training'),
        ('pilates', 'Pilates'),
        ('sports', 'Sports'),
        ('strength training', 'Strength training'),
        ('yoga', 'Yoga'),
    ]
    title = models.CharField(max_length=29, unique=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts") # noqa
    label = models.CharField(max_length=17, choices=TAG_CHOICES, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder', blank=True) # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='forum_likes', blank=True) # noqa

    class Meta:
        '''Meta class sets descending order.'''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        '''Generates the number of likes per post.'''
        return self.likes.count()


class Comment(models.Model):
    '''
    Comment model.
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # noqa
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta class sets ascending order.'''
        ordering = ['created_on']

    def __str__(self):
        return f"{self.body} commented by {self.name}"
