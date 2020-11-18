from django.contrib import admin
from .models import Area_category,Plan,User_plan,Seller_Product,Car_type
# Register your models here.
admin.site.register(Area_category)
admin.site.register(Plan)
admin.site.register(User_plan)
admin.site.register(Seller_Product)
admin.site.register(Car_type)
