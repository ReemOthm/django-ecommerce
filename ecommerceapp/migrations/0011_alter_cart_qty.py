# Generated by Django 4.2.15 on 2024-09-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0010_alter_order_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
