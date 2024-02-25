from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	
  path('', views.Posts.index, name = "index"),
  path('posts/category/<int:category_id>', views.Posts.postsByCategory, name = "PostsByCategory"),
  path('posts/tag/<int:tag_id>', views.Posts.postsByTag, name = "PostsByTag"),
  path('post/<int:post_id>', views.Posts.show, name = "show"),
  path('post/like/<int:post_id>', views.Posts.like, name = "like"),
  path('post/new-post/', views.Posts.createPost, name="create-post"),
  path('post/publish-post/<str:user_id>', views.Posts.publishPost, name="publish-post"),
]