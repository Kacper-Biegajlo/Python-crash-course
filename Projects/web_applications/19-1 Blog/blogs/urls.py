"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [ 
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('blogposts/', views.blogposts, name='blogposts'),
    # Detail page for a single topic. 
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    # Page for adding a new topic
    path('new_blogpost/', views.new_blogpost, name='new_blogpost'),
    # Page for editing an entry.
    path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
]
