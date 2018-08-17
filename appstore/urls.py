from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post, Reviews
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name= 'post_list'),
    url(r'^appstore/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
    url(r'^reviews/$', views.reviews, name = 'reviews'),
    url(r'^appstore/new/$', views.post_new, name= 'post_new'),
    url(r'^appstore/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^appstore/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^appstore/(?P<pk>\d+)/comment/edit/$', views.edit_comment_to_post, name='edit_comment_to_post'),
]
