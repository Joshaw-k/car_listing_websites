from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Seller_Product

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SellerProductForm(forms.ModelForm):
    class Meta:
        model = Seller_Product
        fields = ['car_name','car_model','car_image_front','car_image_top','car_image_side','car_image_back','car_owner','car_owner_location','car_price','car_features','car_description','car_type','car_year','area_category']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Seller_Product
        fields = ['car_name','car_model','car_image_front','car_image_top','car_image_side','car_image_back','car_owner','car_owner_location','car_price','car_features','car_description','car_type','car_year','area_category']
