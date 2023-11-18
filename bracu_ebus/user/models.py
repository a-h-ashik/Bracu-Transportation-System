from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, default="#1")
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    point = models.IntegerField(default=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

class UserLoggedIn(models.Model):
    logged_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    logged_date = models.DateTimeField(auto_now_add=True)

class AccountRequestTable(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_requested = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)