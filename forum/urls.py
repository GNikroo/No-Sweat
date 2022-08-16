'''Urls for No Sweat fitforum'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]
