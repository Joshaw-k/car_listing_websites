from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from car_listing_app.models import Seller_Product
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from car_listing_app.forms import SellerProductForm

@login_required
def dashboard(request):
    seller_product = request.user
    if seller_product.is_superuser == False:
        return redirect('admin-login')
    else:    
        context = { 'seller_product':seller_product}
        return render(request,'admin-dashboard.html',context) 

@login_required
def profile(request):
    seller_product = request.user
    context = { 'seller_product':seller_product}
    return render(request,'admin-profile.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_superuser(username=form['username'],password=form['password1'])
            return redirect('sellers')
    else:
        form = UserRegisterForm()        
    context = {'form':form}
    return render(request,'create-admin.html',context) 
    
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
    return render(request,'all_cars.html',context)

def ban_sellers(request,id):
    banned_seller = User.objects.get(id=id)
    banned_seller.is_active = False
    banned_seller.save()
    return redirect('sellers')

def remove_ban(request,id):
    banned_seller = User.objects.get(id=id)
    banned_seller.is_active = True
    banned_seller.save()
    return redirect('sellers') 

def add_car(request):
    if request.method == 'POST':
        form = SellerProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SellerProductForm()        
    context = {'form':form}

    return render(request,'add_car.html',context)     

# def deactivate_car(request,id):
#     deactivated_car = Seller_Product.objects.get(id=id)
#     deactivated_car.cat_status = False
#     deactivated_car.save()
#     return redirect('all_cars')

# def activate_car(request,id):
#     activate_car = Seller_Product.objects.get(id=id)
#     activate_car.cat_status = True
#     activate_car.save()
#     return redirect('all_cars')