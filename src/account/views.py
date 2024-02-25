from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from blog.models import Post
from .models import User

# Create your views here.
class Registration:
	
	
	def login_page(request):
		
		if request.method == "POST":
			identifiant = request.POST.get("identifiant")
			pwd = request.POST.get("password")
			user = authenticate(request, username=identifiant, password=pwd)
			
			if user is not None:
				login(request, user)
				return redirect("blog:index")
			else:
				messages.info(request, "Identifiant ou mot de passe incorrect")

		return render(request, "account/registration/login.html")
		
	@login_required
	def logout_page(request):
		logout(request)
		return redirect("blog:index")
		
		
	def check_email(user):
		return user.username.endswith("@example.com")
	
	
	def register_page(request):
		
		if request.method == "POST":
			first_name = request.POST.get("first_name")
			last_name = request.POST.get("last_name")
			identifiant = request.POST.get("identifiant")
			pwd = request.POST.get("password")
			
			User.objects.create_user(
				email = identifiant, 
				first_name = first_name,
				last_name = last_name, 
				password=pwd
			)
			
			request.POST = {}

			return redirect("account:login")
		
		return render(request, "account/registration/register.html")
	
	def edit_page(request):
		pass
		
@login_required
def index(request):
	our_posts = Post.objects.all().filter(writed_by = request.user).order_by('-updated_at')

	context = {
		"our_posts": our_posts,
	}


	return render(request, "account/account.html", context=context)
	
def allUsers(request):
  return render(request, 'account/users.html', {'users': User.objects.all()})