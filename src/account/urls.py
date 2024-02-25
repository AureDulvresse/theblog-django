from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
  path('login/', views.Registration.login_page, name="login"),
  path('logout/', views.Registration.logout_page, name = "logout"),
  path('register/', views.Registration.register_page, name = "register"),
  path('', views.index, name="index"),
  path('edit/', views.Registration.edit_page, name = "edit"),
  path('users/', views.allUsers),
]