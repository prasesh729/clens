from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from user.models import User
from products.models import Products,Category,Sub_Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages

from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def dashboard(request):
    return render(request,"dashboard.html",{})

def aboutus(request):
    return render(request,"aboutus.html",{})

def product(request):
    category = Category.objects.all()
    product = Products.objects.all()
    paginator = Paginator(product, 16)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
        'category': category,
    }
    return render(request, "product.html", data)

class Product_p(View):
    def post(self,request,id):
        product=request.POST.get("product")
        cart = request.session.get('cart')
        if cart:
            quantity =cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] =1
        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('')


    def get(self,request,id):
        single_product = get_object_or_404(Products, pk=id)

        data = {
            'single_product': single_product,
        }
        return render(request, "product_details.html", data)


def loginn(request):
    if request.method == 'POST':
        username=request.POST["uname"]
        pswd1 = request.POST["pswd"]

        user =authenticate(username=username,password=pswd1)
        if user is not None:
            login(request,user)
            return redirect('/')
            messages.success(request, "login")
        else:
            return redirect("/login")
            messages.error(request, "Incorrect password")
    else:
        return render(request, "login.html", {})

def signout(request):
    logout(request)
    return redirect('/')


def customer_register(request):
    if (request.method == 'POST'):
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        uname = request.POST['uname']
        email = request.POST['Email']
        pswd = request.POST['pswd']
        ins = User.objects.create_user(first_name=f_name, last_name=l_name, username=uname, email=email, password=pswd)
        ins.save()
        return redirect('http://127.0.0.1:8012/')
    else:
        customers = User.objects.all()
        return render(request, "register.html", {'customer': customers})