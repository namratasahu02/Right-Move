# Generated by Django 4.0.2 on 2022-02-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_unit',
        ),
    ]
