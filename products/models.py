from django.db import models
from user.models import User
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=150)
    class Meta:
        db_table='category_tbl'


class Sub_Category(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='sub_category_tbl'

class Products(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    p_name = models.CharField(max_length=100,blank=True)
    p_category = models.CharField(max_length=100,blank=True)
    p_description = models.TextField(max_length=300,blank=True)
    p_quantity=models.PositiveIntegerField()
    p_price=models.PositiveIntegerField()
    p_image=models.ImageField(upload_to='product_img',blank=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,default=17)

    class Meta:
        db_table = "product_tbl"

class Booking(models.Model):

    Mbooking_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.ForeignKey(Products,on_delete=models.CASCADE)
    your_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    date = models.DateField()
    phone_number=models.CharField(max_length=50)
    location=models.CharField(max_length=100)

    class Meta:
        db_table="product_booking"




