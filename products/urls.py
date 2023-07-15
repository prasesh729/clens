from django.urls import path

from products import views

urlpatterns = [
    path('add/',views.add_user_product),

    path('purchase/<int:p_id>', views.purchase,name='purchase'),
    path('book_details/<int:p_id>', views.book_details,name='book_details'),
    path('update/<int:p_edit_id>',views.product_edit),
    path('delete/<int:product_id>',views.user_product_delete),
    path('done/',views.purchasedone),


]