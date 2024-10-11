"""
URL configuration for ecommerceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerceapp import views as ec
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ec.index, name='index'),
    path('products/<int:id>', ec.products, name='products'),
    path('details/<int:id>', ec.details, name='details'),
    path('add_to_cart/', ec.add_to_cart, name='add_to_cart'),
    path('checkout/', ec.checkout, name='check'),
    path('auth_register/',ec.auth_register,  name='auth_register'),
    path('auth_login/',ec.auth_login, name='auth_login'),
    path('logout/',ec.logout_view , name='logout'),
    path('delete_item_from_cart/',ec.delete_item_from_cart),
    path('remove_all_items/',ec.remove_all_items),
    path('change_qty/',ec.change_qty),
    path('pay/',ec.pay, name="pay"),
    path('my_orders/',ec.my_orders, name="my_orders"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
