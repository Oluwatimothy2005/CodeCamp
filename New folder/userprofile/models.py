from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pix = models.ImageField(upload_to='customer')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Customer'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'    
    