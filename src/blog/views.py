from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Comment, PostTag, Category

class Posts:
	
	def index(request):
		
		posts = Post.objects.all()
		popularPosts = Post.objects.all().order_by("-nb_likes", "-updated_at")[:5]

		categories = Category.objects.all()
		post_tag = PostTag.objects.all()
		
		context = {
			'post_tag': post_tag,
			'categories': categories,
			'popularPosts': popularPosts,
		}
		
		if request.method == "POST":
			
			form = request.POST
			
			searchValue = form.get("search")
			
			if searchValue is not None:
				
				posts = posts.filter(title__icontains = searchValue)
				context['searchValue'] = searchValue
			
			else:
			
				return redirect("blog:index")
		
		posts = posts.order_by("-updated_at")
		
		paginator = Paginator(posts, 10)
		page = request.GET.get('page')
		posts = paginator.get_page(page)
		
		context['posts'] = posts

		
		return render(request, 'blog/Posts/index.html', context)
	
	def show(request, post_id):
		
		post = get_object_or_404(Post, pk = post_id)
		
		if request.method == "POST":
			form = request.POST
			comment = form.get('comment')
			
			if comment:
				Comment.objects.create(
					content = comment,
					comment_by = request.user,
					post = post
				)
				comment = ""
		
		comments = Comment.objects.all().filter(post__id = post_id).order_by('-created_at')
		post_tag = PostTag.objects.all()
		
		context = {
			'post' : post,
			'tags' : post_tag,
			'comments' : comments,
		}
		
		return render(request, 'blog/Posts/show.html', context)
	
	
	def postsByCategory(request, category_id):
		posts = Post.objects.filter(category__id = category_id).order_by("-updated_at")
		
		popularPosts = Post.objects.all().order_by("-nb_likes", "-updated_at")[:5]
		
		categories = Category.objects.all()
		post_tag = PostTag.objects.all()
		
		paginator = Paginator(posts, 10)
		page = request.GET.get('page')
		posts = paginator.get_page(page)
		
		context = {
			'filterActive': category_id,
			'posts': posts,
			'post_tag': post_tag,
			'categories': categories,
			'popularPosts': popularPosts,
		}
		
		return render(request, 'blog/Posts/index.html', context)
	
	def postsByTag(request, tag_id):
		posts = Post.objects.filter(tag__id = tag_id).order_by("-updated_at")
		
		popularPosts = Post.objects.all().order_by("-nb_likes", "-updated_at")[:5]
		
		categories = Category.objects.all()
		post_tag = PostTag.objects.all()
		
		paginator = Paginator(posts, 10)
		page = request.GET.get('page')
		posts = paginator.get_page(page)
		
		context = {
			'posts': posts,
			'post_tag': post_tag,
			'categories': categories,
			'popularPosts': popularPosts,
		}
		
		return render(request, 'blog/Posts/index.html', context)
	

	def like(request, post_id):
		post = get_object_or_404(Post, pk = post_id)
		post.nb_likes = post.nb_likes + 1
		post.save()
		return redirect('blog:show', post_id=post_id)
	
	
	def createPost(request):
		pass