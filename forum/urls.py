'''Urls for No Sweat fitforum'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user_profile/', views.UserPostList.as_view(), name='user_profile'),  # noqa
    path('search/', views.Search.as_view(), name='search'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/update_post', views.UpdatePost.as_view(), name='update_post'), # noqa
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/delete_post', views.DeletePost.as_view(), name='delete_post'), # noqa
    path('<slug:slug>/<int:pk>/update_comment', views.UpdateComment.as_view(), name='update_comment'), # noqa
    path('<slug:slug>/<int:pk>/delete_comment', views.DeleteComment.as_view(), name='delete_comment'), # noqa
]
