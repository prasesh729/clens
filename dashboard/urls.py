"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dashboard import views
from dashboard.views import Product_p
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('aaadmin/', admin.site.urls),
    path('',views.dashboard),
    path('login/',views.loginn,name='login'),
    path('register/',views.customer_register),
    path('aboutus/',views.aboutus),
    path('admin/',include("admin_app.urls")),
    path('user/',include('user.urls'),name='user'),
    path('product/',views.product,name='product'),
    path('product/',include('products.urls')),
    path('product_detail/<int:id>/',Product_p.as_view(), name='product_detail'),
    path('c_logout/', views.signout,name='logout'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),



    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),



    path('reset/done/',auth_views.PasswordResetCompleteView.as_view( template_name='password_reset_complete.html'), name='password_reset_complete'),
]
