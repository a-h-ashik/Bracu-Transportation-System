from django.db import models


# Create your models here.
class paymentTable(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_number = models.CharField(max_length=255, default='')
    payment_status = models.CharField(max_length=20, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    


    def __str__(self):
        return self.name
        