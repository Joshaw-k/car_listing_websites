from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from car_listing_app.models import Seller_Product
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    seller_product = request.user
    context = { 'seller_product':seller_product}
    return render(request,'admin-dashboard.html',context) 

@login_required
def sellers(request):
    user = User.objects.all()
    context ={'user':user}
    return render(request,'admin-sellers.html',context)
    
@login_required
def all_cars(request):
    seller_product = Seller_Product.objects.all()
    context = {
        'seller_product':seller_product
    }
    return render(request,'all_car.html',context)
