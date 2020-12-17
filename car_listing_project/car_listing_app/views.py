from django.shortcuts import render,redirect
from .forms import SellerProductForm,UpdateProductForm,UserRegisterForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Seller_Product
from django.contrib.auth import login,authenticate,logout
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Seller_Product,Plan,User_plan
from django.http import HttpResponse,JsonResponse
import json

# def home(request):
#     seller_product = Seller_Product.objects.all()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('dashboard') 
#         else:
#             return HttpResponse('not correct')       
#     else:
#         pass
#     context = {
#         'seller_product':seller_product,
#     }
#     return render(request,'index.html',context)

def home(request):
    seller_product = Seller_Product.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')    
    else:
        form = UserRegisterForm()
    context = {
        'seller_product':seller_product,
        'form':form
    }
    return render(request,'index.html',context)    

def dashboard(request):
    seller_product = request.user
    context = { 'seller_product':seller_product}
    return render(request,'dashboard.html',context)    

def create(request):
    user = request.user.username
    user_plan = User_plan.objects.all()
    data = []
    for user in user_plan:
        data_small = {'username':user.user_name}
        data.append(data_small)


    if user not in data:
                
        return redirect('plan')
    else:
        if request.method == 'POST':
            form = SellerProductForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = SellerProductForm()

    context = {'form':form}
    return render(request,'post_form.html',context)

# def register(request):
#     return render(request,'register.html')

# @csrf_exempt
# def register_plan(request):
#     plans = Plan.objects.all()
#     plan_data = []
#     for plan in plans:
#         data = {'id':plan.id,'plan_name':plan.plan_name,'plan_desc':plan.plan_desc}
#         plan_data.append(data)
#     return JsonResponse(json.dumps(plan_data),content_type="application/json",safe=False)

# @csrf_exempt
# def plan_save(request):
#     email = request.POST.get("email")
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     picked_id = request.POST.get("picked")
#     register = User.objects.create_user(email=email,username=username,password=password)
#     register.save()
#     picked_obj = Plan.objects.get(id=picked_id)
#     username_obj = User.objects.get(username=username)
#     picked = User_plan(user_plan_name=picked_obj,user_name=username_obj)
#     picked.save()
#     return HttpResponse("ok")    

@login_required
def car_details(request,id):
    seller_product = Seller_Product.objects.get(id=id)
    context = {'seller_product':seller_product}
    return render(request,'car-detail.html', context)

@login_required
def edit_details(request,id):
    seller_product = Seller_Product.objects.get(id=id)
    if request.method == 'POST':
        edit_car = UpdateProductForm(request.POST,request.FILES,instance=seller_product)
        if edit_car.is_valid():
            edit_car.save()
            return redirect('profile')
    else:
        edit_car = UpdateProductForm(instance=seller_product)        
    context = {'seller_product':edit_car}
    return render(request,'edit-detail.html', context)

@login_required()
def confirm_delete(request,id):
    get_value = id
    context={
        'get_value':get_value
    }
    return render(request,'confirm_delete.html',context)

def delete_car(request,id):
    delete_product = Seller_Product.objects.get(id=id)
    delete_product.delete()
    return redirect('profile')



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
    user = request.user
    # user_plan = User_plan.objects.get(user_name=user)
    plan = Plan.objects.all()
    context = {"plan":plan}
    return render(request,'plan2.html',context)    

def user_plan(request,id):
    user = request.user
    plan = Plan.objects.get(id=id)
    print(user)
    user_plan = User_plan.objects.get(user_name=user)
    user_plan.user_plan_name = plan
    user_plan.save()
    return redirect('plan')

def about_us(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonials.html')

def faq(request):
    return render(request,'faq.html')

def terms(request):
    return render(request,'terms.html') 

def contact(request):
    return render(request,'contact.html')

def cars(request):
    car = Seller_Product.objects.all()
    total_car=0
    for total in car:
        total_car+=1   
    context = {'cars':car,'total-cars':total_car}
    return render(request,'cars.html',context)           

def logout_view(request):
    logout(request)
    return redirect("home")
