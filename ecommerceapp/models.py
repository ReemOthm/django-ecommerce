from django.db import models

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
    availibility = models.BooleanField()
    storetype = models.ForeignKey(StoreType, on_delete= models.CASCADE, null=True)
    def __str__(self):
        template='{0.item_name} {0.description} {0.image} {0.price} {0.availability}'
        return template.format(self)

class ItemsDetails(models.Model):
    color = models.CharField(max_length=50)
    qty = models.FloatField()
    tax = models.FloatField()
    barcode = models.CharField(max_length=50)
    item = models.ForeignKey(Items, on_delete= models.CASCADE, null=True)
    def __str__(self):
        template='{0.color} {0.qty} {0.tax} {0.barcode}'
        return template.format(self)

