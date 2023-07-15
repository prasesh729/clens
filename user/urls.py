from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [


    path('update/<int:profile_id>',views.update_profile),
    path('products/<int:user_id>',views.user_product),



]