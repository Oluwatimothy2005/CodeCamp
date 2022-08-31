from django.contrib import admin
from . models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','username','first_name','last_name','phone','address','email','pix']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','price','qty','amount','paid']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Cart,CartAdmin)