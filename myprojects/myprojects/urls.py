from django.contrib import admin
from django.urls import path
from post.views import create_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/create', create_post, name='create_post'),
]
