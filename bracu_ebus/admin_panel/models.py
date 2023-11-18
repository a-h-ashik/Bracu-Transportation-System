from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id = models.CharField(max_length=10, primary_key=True, default="A1")
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=10)

class AdminLoggedIn(models.Model):
    logged_id = models.OneToOneField(Admin, on_delete=models.CASCADE, primary_key=True)
    logged_date = models.DateTimeField(auto_now_add=True)

class Staff(models.Model):
    staff_id = models.CharField(max_length=5, default="S1", primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default="0000")

    def __str__(self):
        return self.name
    

