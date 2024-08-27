from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Items, StoreType, ItemsDetails

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def products(request):
    p = Items.objects.filter(storetype=1)
    template = loader.get_template('products.html')
    return HttpResponse(template.render({'items':p}))

