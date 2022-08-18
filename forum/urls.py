'''Urls for No Sweat fitforum'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user_profile/', views.UserPostList.as_view(), name='user_profile'),  # noqa
    path('search/', views.Search.as_view(), name='search'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
