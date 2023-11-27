from django.db import models

# Create your models here.
class Buses(models.Model):
    bus_number = models.IntegerField(primary_key=True)
    d1 = models.CharField(max_length=50)
    d2 = models.CharField(max_length=50)
    d3 = models.CharField(max_length=50)
    d4 = models.CharField(max_length=50)
    d5 = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

class Tickets(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=50)
    bus_number = models.IntegerField()
    seat_number = models.CharField(max_length=5)
    user_id = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

