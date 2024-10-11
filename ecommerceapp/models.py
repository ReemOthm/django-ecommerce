from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class StoreType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Items(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image= models.ImageField(upload_to='images/', null=True)
    price= models.FloatField()
    availability = models.BooleanField()
    color = models.CharField(max_length=50)
    qty = models.IntegerField()
    tax = models.FloatField()
    barcode = models.CharField(max_length=50)
    storetype = models.ForeignKey(StoreType, on_delete= models.CASCADE, null=True)
    def __str__(self):
        template='{0.item_name} {0.description} {0.image} {0.price} {0.availability}'
        return template.format(self)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Cart(models.Model):
    itemsid = models.IntegerField()
    name = models.CharField(max_length=50,null=True)
    image= models.ImageField(upload_to='images/', null=True)
    color = models.CharField(max_length=50,null=True)
    qty = models.IntegerField()
    price= models.FloatField()

class Order(models.Model):
    items = models.ManyToManyField(Items)
    qty = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
    total= models.FloatField()
    status = models.CharField(max_length=50)
    products = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)


