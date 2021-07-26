from django.core import paginator
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from account.models import User, Order
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'home.html', {'products':products})

def create(request):
    if request.method == "POST":
        new_product = Product()
        new_product.product_name = request.POST["product_name"]
        new_product.product_info = request.POST["product_info"]
        new_product.product_img = request.FILES.get('product_img')
        new_product.save()
        return redirect('home')
    else:
        return render(request, 'create.html')

def detail(request, id):
    product = get_object_or_404(Product, id = id)
    return render(request, 'detail.html', {'product' : product})

def edit(request, id):
    if request.method == "POST":
        update_product = Product.objects.get(id = id)
        update_product.product_name = request.POST["product_name"]
        update_product.product_info = request.POST["product_info"]
        update_product.product_img = request.FILES.get('product_img')
        update_product.save()
        return redirect('detail', update_product.id)
    else:
        product = Product.objects.get(id = id)
        return render(request, 'edit.html', {'product':product})

def delete(request, id):
    delete_product = Product.objects.get(id = id)
    delete_product.delete()
    return redirect('home')

def order(request, id):
    product = get_object_or_404(Product, id = id)
    new_order = Order()
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    new_order.order_user = user
    new_order.order_product = product
    new_order.save()
    return redirect('order_finished')

def order_list(request):
    list = Order.objects.all()
    products=Product.objects.all()

    list = list.filter(order_user = request.user.id)

    result=[]

    for i in list:
        for j in products:
            if str(i) == str(j) :
                result.append(j)
    
    return render(request, 'order_list.html', {'reuslt':result})
    
def order_finished(request):
    return render(request, 'order_finished.html')