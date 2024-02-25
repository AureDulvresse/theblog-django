from django import forms
from django.forms import ModelForm
from .models import Comment, Post



class CommentForm(ModelForm):
	
	class Meta:
		model = Comment
		fields= ['content']

class PostForm(ModelForm):
	
	class Meta:
		model = Post
		fields = ['title', 'content', 'thumbnail', 'category']