from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Items, Cart, Order
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from django.contrib.auth import login ,authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginUserForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))

def products(request, id):
    p = Items.objects.filter(Q(storetype=id) & Q(availability=True))
    template = loader.get_template('products.html')
    return HttpResponse(template.render({'request':request, 'items':p}))

def details(request,id):
    template = loader.get_template('details.html')
    data = Items.objects.filter(id=id).first()
    return HttpResponse(template.render({'request':request, 'data':data}))

def calculate_count(request):
    row = Cart.objects.all()
    count =0
    for item in row:
        count = count + int(item.qty)
    request.session["cart"]= count
    return count

def total_price():
    cart_items = Cart.objects.all()
    total = 0
    for item in cart_items:
        total += item.price
    return total

@csrf_exempt
def add_to_cart(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    image = request.POST.get('image')
    color = request.POST.get('color')
    qty = request.POST.get('qty')
    price = request.POST.get('price')

    product = Cart.objects.filter(itemsid=id).first()
    if product:
        product.qty += int(qty)
        product.price += float(price) 
        product.save()
    else: 
        p= Cart(itemsid=id,name=name,image=image,color=color,qty=qty,price=price)
        p.save()
    count = calculate_count(request)
    return JsonResponse({'count': count})

@csrf_exempt
def change_qty(request):
    item = Cart.objects.filter(itemsid=request.POST.get('id')).first()
    action = request.POST.get('action')
    price = Items.objects.filter(id=request.POST.get('id')).first().price
    if action == 'add':
        item.qty += 1
        item.price += price
    elif action == 'remove':
        item.qty -= 1
        item.price -= price
    item.save()
    count = calculate_count(request)
    total = total_price()
    return JsonResponse({"count": count,"price": item.price, "total": total })

@csrf_exempt
def delete_item_from_cart(request):
    item = Cart.objects.filter(itemsid=request.POST.get('id'))
    item.delete()
    count = calculate_count(request)
    return JsonResponse({"count": count})

@csrf_exempt
def remove_all_items(request):
    Cart.objects.all().delete()
    request.session["cart"]= 0
    return JsonResponse({"count": 0})

@csrf_exempt
def pay(request):
    products= Cart.objects.values_list("itemsid", flat=True)
    quantities= Cart.objects.values_list("qty", flat=True)
    ids = ",".join(str(x) for x in products)
    qIds = ",".join(str(x) for x in quantities)
    totalprice = total_price()
    order = Order(qty=qIds, total=totalprice,status="pending",products=ids)
    order.save()
    for idx,i in enumerate(products):
        p = Items.objects.get(id=i)
        p.qty = p.qty - quantities[idx]
        p.save()
        if(p.qty == 0):
            p.availability = False
            p.save()
        order.items.add(p)
    Cart.objects.all().delete()
    request.session["cart"]= 0
    return JsonResponse({"sucess":True})

@login_required(login_url='/auth_login/')
def checkout(request):
    template = loader.get_template('checkout.html')
    cart_items = Cart.objects.all()
    total =  total_price()
    return HttpResponse(template.render({'request': request, 'items': cart_items, 'total': total }))

@login_required(login_url='/auth_login/')
def my_orders(request):
    orders = Order.objects.prefetch_related('items').all()
    template = loader.get_template('orders.html')
    return HttpResponse(template.render({'request': request, "orders": orders, }))

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return checkout(request)
    context={'form':form}
    return render(request,'auth_login.html',context)

@csrf_exempt
def auth_register(request):
    template = loader.get_template('auth_register.html')
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context = {"registerform":form, "request": request}
    return HttpResponse(template.render(context=context))

def logout_view(request):
    logout(request)
    return redirect('/')