from django.db import models
from django.contrib import admin
class shopping(models.Model):
    ProductId = models.CharField( primary_key=True,max_length=10)
    ProductName= models.CharField(max_length=30)
    Category= models.CharField(max_length=15)
    Price= models.IntegerField()
    ProductDescription= models.CharField(max_length=100)
    Discount= models.IntegerField()
    Retailer= models.CharField(max_length=10)
class shoppingAdmin(admin.ModelAdmin):
    list_display=["ProductId","ProductName","Category","Price","ProductDescription","Discount","Retailer"]
