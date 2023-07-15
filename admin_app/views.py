from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Products, Booking
from user.forms import CustomerForm
from products.forms import ProductForm
from django.conf import settings


# Create your views here.

# @login_required(login_url='/admin/login')
def admindashboard(request):
    admins = User.objects.all().order_by('username').filter(is_superuser=True)
    # it means (select * from Admins )
    return render(request, "admin_dashboard.html", {'admins': admins})


def view_user_booking(request):
    purchases = Booking.objects.all()
    # it means (select * from Admins )
    return render(request, "users_purchases.html", {'purchases': purchases})


# @login_required(login_url='/admin/login')
def addadmins(request, *args, **kwargs):
    if request.method == 'POST':
        fn = request.POST["f_name"]
        l_name = request.POST['l_name']
        uname = request.POST["uname"]
        Email = request.POST["Email"]
        pswd = request.POST["pswd"]
        user = User(first_name=fn, last_name=l_name, username=uname, email=Email, password=pswd, is_superuser=True,
                    is_admin=True, is_active=True,
                    is_staff=True, is_customer=True)
        user.save()
        return redirect('/admin/dashboard')

    else:
        return render(request, "addadmins.html", {})


# @login_required(login_url='/admin/login')
def C_details(request, *args, **kwargs):
    if (request.method == 'POST'):
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        uname = request.POST['uname']
        email = request.POST['Email']
        pswd = request.POST['pswd']
        ins = User(first_name=f_name, last_name=l_name, username=uname, email=email, password=pswd)
        ins.save()
        return redirect('/admin/customers')
    else:
        customers = User.objects.all().order_by('username').filter(is_superuser=False)
        return render(request, "customer_details.html", {'customer': customers})


# @login_required(login_url='/admin/login')
def p_details(request):
    if (request.method == 'POST'):
        p_name = request.POST['p_name']
        p_category = request.POST['p_category']
        p_description = request.POST['p_description']
        p_quantity = request.POST['quantity']
        p_price = request.POST['p_price']
        if len(request.FILES) != 0:
            p_image = request.FILES['p_image']
            ins = Products(p_name=p_name, p_category=p_category, p_description=p_description,
                           p_quantity=p_quantity, p_price=p_price, p_image=p_image)
            ins.save()
            return redirect('/admin/products')

    else:
        products = Products.objects.all()
        return render(request, "admin_products.html", {'product': products})


# -----------------------------------login and logout views---------------------------------
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        pswd1 = request.POST["pswd"]

        user = authenticate(username=username, password=pswd1)
        if user is not None:
            login(request, user)
            name = user.first_name
            return redirect('/admin/dashboard')

        else:
            messages.error(request, "B=Invalid")
            return redirect("/admin/loginredirect")
    else:
        return render(request, "admin_login.html", {})


def login_redirect(request):
    return render(request, "admin_login.html")


def signout(request, *args, **kwargs):
    logout(request)
    return redirect('/admin/login')


def product_edit(request, product_id):
    if (request.method == 'POST'):
        product = Products.objects.get(product_id=product_id)

    return render(request, 'admin_products.html')


def product_delete(request, product_id):
    product = Products.objects.get(product_id=product_id)
    product.delete()
    return redirect('/admin/products')


def customer_delete(request, id):
    customer = User.objects.get(id=id)
    customer.delete()
    return redirect('/admin/customers/')


def admin_delete(request, a_id):
    admin = User.objects.get(id=a_id)
    admin.delete()
    return redirect('/admin/dashboard/')


def adminupdate(request, edit_id):
    admin = User.objects.get(id=edit_id)

    if (request.method == "POST"):
        form = CustomerForm(request.POST, instance=admin)

        if form.is_valid():
            form.save()
            return redirect('/admin/dashboard/')

        else:
            return render(request, "user_update.html", {'admin': admin, 'profile_form': form})

    contextq = {'profile_form': CustomerForm(instance=admin)}
    return render(request, "user_update.html", contextq)
    # form.username = request.POST['uname']
    # form.email = request.POST['Email']
    # form.first_name = request.POST['f_name']
    # form.last_name = request.POST['l_name']
    # form.password = request.POST['pswd']
    #
    # form.save()


# @login_required(login_url='/login')
def update_products(request, editt_id):
    products = Products.objects.get(product_id=editt_id)
    if (request.method == "POST"):
        form = ProductForm(request.POST, request.FILES, instance=products)
        print("dfsdf")

        if form.is_valid():
            form.save()
            print("fasle")
            return redirect('/admin/products/')
        else:
            return render(request, "update_products.html", {'products': products, 'product_form': form})

    context = {'product_form': ProductForm(instance=products)}
    return render(request, "update_products.html", context)
    # form.p_name = request.POST['p_name']
    # form.p_category = request.POST['p_category']
    # form.p_description = request.POST['p_description']
    # form.p_quantity = request.POST['quantity']
    # form.p_price = request.POST['p_price']
    # form.p_img = request.FILES['p_image']
    # print(form)
    # form.save()


def update_customers(request, edittt_id):
    customerr = User.objects.get(id=edittt_id)

    if (request.method == "POST"):
        form = CustomerForm(request.POST, instance=customerr)
        # form.username = request.POST['uname']
        # form.email = request.POST['Email']
        # form.first_name = request.POST['f_name']
        # form.last_name = request.POST['l_name']
        # form.password = request.POST['pswd']
        # form.save()

        if form.is_valid():
            form.save()
            return redirect('/admin/customers/')
        else:
            return render(request, "update_customer.html", {'customerr': customerr, 'customer_form': form})

    contextt = {'customer_form': CustomerForm(instance=customerr)}
    return render(request, "update_customer.html", contextt)
