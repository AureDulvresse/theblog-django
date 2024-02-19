from django.db import models
from account.models import User

class Category(models.Model):
  
  name = models.CharField(max_length = 50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def ___str__(self):
    return self.name

class Tag(models.Model):
  
  name = models.CharField(max_length = 50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def ___str__(self):
    return self.name


class Post(models.Model):
  
  title = models.CharField(max_length = 50, unique = True)
  slug = models.CharField(max_length = 70, unique = True)
  content = models.TextField(blank = True)
  excerpt = models.CharField(max_length = 80)
  thumbnail = models.CharField(max_length = 255, default = "post.jpg")
  category = models.ForeignKey(Category, null = True, on_delete = models.SET_NULL)  
  tags = models.ManyToManyField(Tag, through="PostTag")
  nb_likes = models.IntegerField()
  writed_by = models.ForeignKey(User, related_name ="Auteur", on_delete = models.CASCADE)
  likes = models.ManyToManyField(User, related_name="Votant", through = "PostUserLikes")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
  
  content = models.CharField(max_length = 200)
  comment_by = models.ForeignKey(User, on_delete = models.CASCADE)
  post = models.ForeignKey(Post, on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def ___str__(self):
    return self.content
    
class PostUserLikes(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)   
  post = models.ForeignKey(Post, on_delete = models.CASCADE)
  
class PostTag(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete = models.CASCADE)