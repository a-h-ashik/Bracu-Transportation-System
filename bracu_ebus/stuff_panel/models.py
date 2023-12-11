from django.db import models

# Create your models here.

class OfferTable(models.Model):
    offer_name=models.CharField(max_length=100)
    duration_date=models.CharField(max_length=100)

class Notification(models.Model):
    givenotification=models.CharField(max_length=100)
    
    
class Pointaddmodel(models.Model):
    email=models.EmailField(max_length=100)
    pointno=models.CharField(max_length=10)