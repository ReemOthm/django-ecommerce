# Generated by Django 4.2.15 on 2024-09-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_alter_cart_price_alter_itemsdetails_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='itemsid',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AddField(
            model_name='cart',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.items'),
        ),
        migrations.AddField(
            model_name='items',
            name='barcode',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='color',
            field=models.CharField(default='hi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='tax',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ItemsDetails',
        ),
    ]
