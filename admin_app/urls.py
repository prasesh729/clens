from django.contrib import admin
from django.urls import path,include
from admin_app import views


urlpatterns = [
    path('dashboard/',views.admindashboard, name="dashboard"),
    path('addadmin/', views.addadmins,name ='addadmin'),
    path('customers/', views.C_details,name='customers'),
    path('customers/',include('user.urls')),
    path('login/', views.adminlogin,name='login'),
    path('loginredirect/',views.login_redirect),
    path('logout/', views.signout,name='logout'),
    path('products/', views.p_details,name='products'),
    path('products/', include('products.urls')),
    path('edit/', views.product_edit, name='edit'),
    path('products/pdelete/<int:product_id>', views.product_delete, name='delete'),
    path('dashboard/adelete/<int:a_id>', views.admin_delete),
    path('uprofile/<int:edit_id>', views.adminupdate),
    path('customers/c_delete/<int:id>', views.customer_delete),
    path('purchase/', views.view_user_booking, name="purchase"),
    path('update_p/<int:editt_id>', views.update_products),
    path('update_c/<int:edittt_id>', views.update_customers),



]