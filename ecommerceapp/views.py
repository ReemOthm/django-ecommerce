from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Items, StoreType, ItemsDetails, Cart
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login ,authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginUserForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))

def products(request):
    p = Items.objects.filter(storetype=1)
    template = loader.get_template('products.html')
    return HttpResponse(template.render({'request':request, 'items':p}))

def details(request,id):
    template = loader.get_template('details.html')
    data = ItemsDetails.objects.select_related('item').filter(item_id=id).first()
    return HttpResponse(template.render({'request':request, 'data':data}))

@csrf_exempt
def add_to_cart(request):
    id = request.POST.get('id')
    p= Cart(itemsid= id)
    p.save()
    row = Cart.objects.all()
    count =0
    for item in row:
        count = count + 1
    request.session["cart"]= count
    return JsonResponse({'count': count})

@login_required(login_url='/auth_login/')
def checkout(request):
    template = loader.get_template('checkout.html')
    cart_items = Cart.objects.values_list('itemsid', flat=True)
    items = ItemsDetails.objects.select_related("item").filter(id__in=cart_items)
    return HttpResponse(template.render({'request': request, 'items': items }))

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