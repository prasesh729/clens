from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from user.models import User
from products.models import Products
from user.forms import CustomerForm
# Create your views here.

@login_required(login_url='/login')
def user_dashboard(request):
    return render(request,"user_dashboard.html",{})


@login_required(login_url='/login')
def update_profile(request,profile_id):
    customer = User.objects.get(id=profile_id)
    print(request.POST)
    if(request.method=="POST"):
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            request.session.flush()
            return redirect("/login")

    return render(request, "profile.html", {'customers':customer})


@login_required(login_url='/login')
def user_product(request,user_id):
    products = Products.objects.filter(user_id_id=user_id)
    return render(request, "user_product.html", {'product':products})

