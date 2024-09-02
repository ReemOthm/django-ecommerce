from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Items, StoreType, ItemsDetails, Cart
from django.views.decorators.csrf import csrf_exempt

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
