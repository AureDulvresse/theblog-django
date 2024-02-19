from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
  
  def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self, email, first_name, last_name, password=None):
    user = self.create_user(
      email,
      password = password,
      first_name = first_name,
      last_name = last_name,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser): 
  email = models.EmailField(
    max_length = 100, 
    unique = True, 
    verbose_name='email'
  )
  first_name = models.CharField(max_length = 150)
  last_name = models.CharField(max_length = 100)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  
  picture = models.CharField(max_length = 255, default = "user.png")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  objects = MyUserManager()
  
  USERNAME_FIELD = "email"
  
  EMAIL_FIELD = "email"
  
  REQUIRED_FIELDS = [
    'first_name',
    'last_name',
  ]
  
  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
    return True

  def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
    return True

  @property
  def is_staff(self):
    "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
    return self.is_admin
  
