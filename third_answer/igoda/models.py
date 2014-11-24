from django.db import models
from django.contrib import admin
class ShopList(models.Model):
       shop_name = models.TextField()
       shop_address = models.TextField()
       shop_tel = models.CharField(max_length=20)
admin.site.register(ShopList)
# Create your models here.
