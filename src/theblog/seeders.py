from django.http import HttpResponse
from django.shortcuts import render

from faker import Faker
from slugify import slugify
from random import randint

from blog.models import Post, Category, Tag, PostTag, Comment, PostUserLikes
from account.models import User


def _selectUser():
  return User.objects.order_by("?").first()

def _selectTag():
    return Tag.objects.all().order_by("?").first()

def _UserSeeder(n):

    fake = Faker('fr_Fr')
    
    admin = User.objects.create_superuser(
      'auredulvresse@gmail.com',
      'Aure',
      'Dulvresse',
      'password123456'
    )
    
    if admin is not None:
      print("SuperUser created")
    
    for i in range(n):
      User.objects.create_user(
        fake.unique.email(),
        fake.first_name(),
        fake.last_name(),
        password = "password"
      )
      

def _CategorySeeder():

    fake = Faker('fr_Fr')
    
    listCat = ["Programmation", "Web design", "jeux video", "reseaux & système"]
    
    for i in range(len(listCat)):
      category = Category()
        
      created_at = fake.date('-1 year')
    
      category.name = listCat[i]
      category.created_at = created_at
      category.updated_at = created_at
        
      category.save()


def _TagSeeder():

    fake = Faker('fr_Fr')
    
    listTag = ["linux", "photoshop", "cisco", "cpp", "java", "python", "csharp", "mobile", "sdl", "javascript", "unity", "security"]
    
    for i in range(len(listTag)):
      tag = Tag()
      created_at = fake.date('-1 year')
        
      tag.name = listTag[i]
      tag.created_at = created_at
      tag.updated_at = created_at
      
      tag.save()

def _PostSeeder(n):

    fake = Faker('fr_Fr')
    
    for i in range(n):
      post = Post()
        
      title = fake.unique.sentence()
      content = fake.paragraphs(nb = 15)
      created_at = fake.date('-1 year')
        
      post.title = title
      post.slug = slugify(title)
      post.content =  "  <br/><br/>".join(content)
      post.excerpt = " ".join(content[0:1])
      post.excerpt = f"{post.excerpt}..."
      post.thumbnail = fake.image_url()
      post.category = Category.objects.order_by("?").first()
      post.nb_likes = randint(1, 18)
      post.writed_by = _selectUser()

      post.created_at = created_at
      post.updated_at = created_at
        
      post.save()
        
      tags = [_selectTag() for i in range(randint(0, 5))]
    
      for tag in tags:
        PostTag.objects.create(post = post, tag = tag)
      
      for _ in range(post.nb_likes):
        PostUserLikes.objects.create(
          user = _selectUser(),
          post = post
        )

def _CommentSeeder(n):

    fake = Faker('fr_Fr')

    for i in range(n):
      comment = Comment()
      created_at = fake.date('-1 year')
      
      comment.content = fake.sentence()
      comment.comment_by = _selectUser()
      comment.post = Post.objects.order_by("?").first()
      comment.created_at = created_at
      comment.updated_at = created_at
        
      comment.save()


def seed(request):

    print("Dropping database...")
    
    Comment.objects.all().delete()
    PostTag.objects.all().delete()
    PostUserLikes.objects.all().delete()
    Post.objects.all().delete()
    User.objects.all().delete()
    Tag.objects.all().delete()
    Category.objects.all().delete()
    
    print("Database Deleted")
    print("Seeding ")
    
    _CategorySeeder()
    print('Category seed : done')
    _TagSeeder()
    print('Tag seed : done')
    _UserSeeder(20)
    print('User seed : done')
    _PostSeeder(45)
    print('Post seed : done')
    _CommentSeeder(100)
    print('Comment seed : done')

    return HttpResponse('<h1>Database Seeded</h1>')
    

def seed_with_option(request, option):
	
	if option == 0:
		print("Dropping database...")
		Comment.objects.all().delete()
		PostTag.objects.all().delete()
		PostUserLikes.objects.all().delete()
		Post.objects.all().delete()
		User.objects.all().delete()
		Tag.objects.all().delete()
		Category.objects.all().delete()
		
		return HttpResponse('<h1>Database Deleted</h1>')
	
		
	if option == 1:
	
		print("Seeding ")
		_CategorySeeder()
		print('Category seed : done')
		_TagSeeder()
		print('Tag seed : done')
		_UserSeeder(20)
		print('User seed : done')
		_PostSeeder(45)
		print('Post seed : done')
		_CommentSeeder(100)
		print('Comment seed : done')
	
	if option == 2:
		print("Seeding ")
		_UserSeeder(20)
		print('User seed : done')
	
	if option == 3:
		print("Seeding ")
		_PostSeeder(20)
		print('Post seed : done')
		
	return HttpResponse('<h1>Database Seeded</h1>')


