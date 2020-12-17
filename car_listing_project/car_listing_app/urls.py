from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('detail/<int:id>',views.car_details,name='car-detail'),
    path('confirm-delete/<int:id>',views.confirm_delete,name='confirm-delete'),
    path('delete/<int:id>',views.delete_car,name='delete-car'),
    path('edit-detail/<int:id>',views.edit_details,name='edit-detail'),
    path('seller_logout/',views.logout_view,name='logout'),
    # path('register/',views.register,name='register'),
    # path('register_plan/',views.register_plan,name='register_plan'),
    # path('plan_save/',views.plan_save,name='plan_save'),
    path('create/',views.create,name="create"),
    path('profile/',views.profile,name='profile'),
    path('plan/',views.plan,name='plan'),
    path('user_plan/<int:id>',views.user_plan,name='user_plan'),
    path('about-us/',views.about_us,name='about-us'),
    path('blog/',views.blog,name='blog'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('faq/',views.faq,name='faq'),
    path('terms/',views.terms,name='terms'),
    path('contact/',views.contact,name='contact'),
    path('cars/',views.cars,name='cars'),
    ]
