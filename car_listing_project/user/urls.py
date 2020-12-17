from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.dashboard,name='admin-dashboard'),
    path('admin-login/',auth_views.LoginView.as_view(template_name='admin-login.html'),name='admin-login'),
    path('admin-profile/',views.profile,name='admin-profile'),
    path('admin-logout/',auth_views.LogoutView.as_view(template_name='admin-logout.html'),name='admin-logout'),
    path('sellers/',views.sellers,name='sellers'),
    path('sellers/',views.sellers,name='sellers'),
    path('ban-seller/<int:id>',views.ban_sellers,name='ban_seller'),
    path('remove-ban/',views.remove_ban,name='remove_ban'),
    path('create-admin/',views.create,name='create-admin'),
    path('all-cars/',views.all_cars,name='all_cars'),
    path('add-car/',views.add_car,name='add_car'),
    ]
