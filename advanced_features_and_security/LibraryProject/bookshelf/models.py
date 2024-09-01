from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)
    class Meta:
        permissions = [
            ('can_view','Can view book'),
            ('can_create','Can create book'),
            ('can_edit','Can edit book'),
            ('can_delete','Can delete book'),
        ]
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,date_of_birth,password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,date_of_birth=date_of_birth,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,date_of_birth=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, date_of_birth=date_of_birth,password=password,**extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True,blank=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']



    def __str__(self):
        return self.email
