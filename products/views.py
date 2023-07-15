from django.shortcuts import render
from products.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Products


# Create your views here.


def add_user_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Sucessfully Added")
    return render(request,"add_user_product.html",{})

@login_required(login_url='/login')
def product_edit(request,p_edit_id):
    products = Products.objects.get(product_id=p_edit_id)
    if (request.method == "POST"):
        form = ProductForm(request.POST, instance=products)
        form.p_name = request.POST['p_name']
        form.p_category = request.POST['p_category']
        form.p_description = request.POST['p_description']
        form.p_quantity = request.POST['p_quantity']
        form.p_price = request.POST['p_price']
        form.img = request.FILES['p_image']
        print(form)
        form.save()
        messages.success(request, "Product Sucessfully Updated")
    return render(request, "edit_product.html",{'pr':products})


def purchase(request):
    return render(request,"purchase.html",{})


def user_product_delete(request,product_id):
    product = Products.objects.get(product_id=product_id)
    product.delete()

    return redirect('/')

@login_required(login_url='/login')
def purchase(request, p_id):
    print(request)


    if request.method == "POST":
        form = BookForm(request.POST)

        try:
            form.save()
            messages.success(request, "you have sucessfully purchased this product")
            redirect('/')

        except:
            print("error")

    else:
        form = BookForm()
    products = Products.objects.get(product_id=p_id)

    return render(request, 'purchase.html', {'products': products, 'form': form})

@login_required(login_url='login')
def book_details(request, p_id):

    purchase = Products.objects.get(product_id=p_id)

    return render(request, 'purchase.html', {'Products': purchase})


def purchasedone(request, p_id):

    return render(request, 'purchasemodal.html', {})
