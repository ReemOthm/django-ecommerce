# Generated by Django 4.2.15 on 2024-09-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_cart_color_cart_image_cart_name_cart_price_cart_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='itemsdetails',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
