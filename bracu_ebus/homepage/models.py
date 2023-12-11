from django.db import models

# Create your models here.
    
from django.db import models

# Create your models here.

class Lost(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    lostitem=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    
       