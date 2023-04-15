from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''

class Medicine(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='medicine_images',blank=True,null=True)
    price=models.FloatField()
    qty=models.IntegerField()
    def __str__(self):
        return self.name

class UserDetail(models.Model):
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    actual_name=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=200)
    dob=models.DateField()

    def __str__(self):
        return self.actual_name
    
class Doctor(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    special=models.CharField(max_length=200)
    meet_link=models.URLField()
    experience=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=200)

    def __str__(self):
        return self.name
    
