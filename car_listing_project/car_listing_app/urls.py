from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
    path('create/',views.create,name="create"),
    path('profile/',views.profile,name='profile'),
    path('plan/',views.plan,name='plan'),
    ]
