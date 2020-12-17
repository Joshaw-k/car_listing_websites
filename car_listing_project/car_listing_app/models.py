from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Area_category(models.Model):
    area_cate = models.CharField(max_length=60)

    def __str__(self):
        return self.area_cate

class Car_type(models.Model):
    car_type = models.CharField(max_length=60)

    def __str__(self):
        return self.car_type

class Plan(models.Model):
    plan_name = models.CharField(max_length=60)
    plan_desc = models.TextField(default="")
    def __str__(self):
        return self.plan_name
        

class User_plan(models.Model):
    user_plan_name =  models.ForeignKey(Plan,on_delete=models.CASCADE,blank=True,null=True)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) 

    def __str__(self):
        return f'{self.user_name} is on a {self.user_plan_name} Plan'      

class Seller_Product(models.Model):
    car_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=80)
    car_model = models.CharField(max_length=80)
    car_year = models.CharField(max_length=80)
    car_type = models.ForeignKey(Car_type,on_delete=models.CASCADE)
    car_owner_location = models.CharField(max_length=80)
    car_image_front = models.ImageField(upload_to='product_pics',default='default.jpg')
    car_image_side = models.ImageField(upload_to='product_pics',default='default.jpg')
    car_image_top = models.ImageField(upload_to='product_pics',default='default.jpg')
    car_image_back = models.ImageField(upload_to='product_pics',default='default.jpg')
    car_price = models.CharField(max_length=80)
    car_description = models.TextField(default='',blank=True,null=True)
    car_features = models.TextField(default='',blank=True,null=True)
    area_category = models.ForeignKey(Area_category,on_delete=models.CASCADE)
    car_status = models.BooleanField(default=True)
    sponsored_car = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    # @property
    # def image_url(self):
    #     if 

       
    # def get_absolute_url(self):
    #     return reverse('home')    

