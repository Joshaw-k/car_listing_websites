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
    
    def __str__(self):
        return self.plan_name

class User_plan(models.Model):
    user_plan_name =  models.ForeignKey(Plan,on_delete=models.CASCADE,blank=True,null=True) 

    def __str__(self):
        return f'You are on a {self.user_plan_name} Plan'      

class Seller_Product(models.Model):
    car_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=80)
    car_model = models.CharField(max_length=80)
    car_year = models.CharField(max_length=80)
    car_type = models.ForeignKey(Car_type,on_delete=models.CASCADE)
    car_speed = models.DecimalField(max_digits=7,decimal_places=2)
    car_owner_location = models.CharField(max_length=80)
    car_image = models.ImageField(default='default.jpg',upload_to='product_pics')
    car_price = models.DecimalField(max_digits=12,decimal_places=2)
    car_description = models.TextField(default='',blank=True,null=True)
    area_cat = models.ForeignKey(Area_category,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    @property
    def imageURL(self):
        try:
            url = self.car_image.url
        except :
            url = '' 
        return url 
    # def get_absolute_url(self):
    #     return reverse('home')    

