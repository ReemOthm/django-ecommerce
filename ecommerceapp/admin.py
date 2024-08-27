from django.contrib import admin
from .models import StoreType, Items,ItemsDetails
# Register your models here.
admin.site.register(StoreType)
admin.site.register(Items)
admin.site.register(ItemsDetails)