from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompanyProfile(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')
    carousel3 = models.ImageField(upload_to='carousel')
    banner = models.ImageField(upload_to='banner')
    favicon = models.ImageField(upload_to='favicon')
    about = models.TextField()
    copyright = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Type(models.Model):
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.brand

    class Meta:
        db_table = 'CompanyProfile'
        managed = True
        verbose_name ='CompanyProfile'
        verbose_name_plural = 'CompanyProfile'
    

    class Meta:
        db_table = 'Type'
        managed = True
        verbose_name ='Type'
        verbose_name_plural = 'Type'
    
class Phone(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    pix = models.ImageField(upload_to='pix')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    network = models.CharField(max_length=50)
    launch = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    feature = models.BooleanField()
    best_selling = models.BooleanField()
    latest = models.BooleanField()
    uploaded_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Phone'
        managed = True
        verbose_name = 'Phone'
        verbose_name_plural = 'Phone'
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class Paiduser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.BooleanField()
    phone = models.CharField(max_length=50)
    oder_no = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    payment_date = models.DateTimeField( auto_now_add=True)

    class Meta:
        db_table = 'paiduser'
        managed = True
        verbose_name = 'Paiduser'
        verbose_name_plural = 'Paiduser'