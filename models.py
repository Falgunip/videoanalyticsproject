from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

"""class customuser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = _('customuser')
        verbose_name_plural = _('customusers')
        swappable = 'AUTH_USER_MODEL'
     """

class analytics_users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25,unique=True)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role=models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()

class video(models.Model):
    videoid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    users_watched_count = models.IntegerField(default=0)
    embed_code = models.TextField()
    viewed_by_users = models.TextField(blank='')
    objects = models.Manager()

