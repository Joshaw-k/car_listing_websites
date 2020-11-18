from django.shortcuts import render,redirect
from .forms import UserRegisterForm,SellerProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Seller_Product
from django.contrib.auth import login,authenticate,logout
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Seller_Product,Plan
def home(request):
    seller_product = Seller_Product.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    else:
        pass       
    context = {
        'seller_product':seller_product
    }
    return render(request,'index.html',context)

def dashboard(request):
    seller_product = request.user
    context = { 'seller_product':seller_product}
    return render(request,'dashboard.html',context)    

def create(request):
    if request.method == 'POST':
        form = SellerProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SellerProductForm()        
    context = {'form':form}

    return render(request,'post_form.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()        
    context = {'form':form}
    return render(request,'register.html',context) 

def profile(request):
    user = request.user.id
    all_cars = Seller_Product.objects.filter(car_owner__id=user)
    foreign = all_cars.filter(area_cat__id=1)
    local = all_cars.filter(area_cat__id=2)
    x=0
    y=0
    z=0
    for number in all_cars:
        x+=1
    for number in foreign:
        y+=1
    for number in local:
        z+=1

    total_all = x
    total_foreign = y
    total_local = z
    context = { 'all':all_cars,'total_all':total_all,'total_foreign':total_foreign,'total_local':total_local,'foreign':foreign,'local':local}
    return render(request,'profile.html',context) 

def plan(request):

    plan = Plan.objects.all()
    context = {"plan":plan}
    return render(request,'plan.html',context)

def logout_view(request):
    logout(request)
    return redirect("home")
