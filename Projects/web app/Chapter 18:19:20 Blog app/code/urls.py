from django.urls import path
from .import views

app_name = 'blogs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Posts
    path('posts/', views.posts, name='posts'),
    # View a single post
    path('post/<int:post_id>/', views.post, name="post"),
    # Creating new post
    path('new_post/', views.new_post, name='new_post'),
    # Edit post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]