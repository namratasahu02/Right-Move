# Generated by Django 4.0.2 on 2022-02-17 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0013_remove_product_quantity_remove_product_weight_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='local_address',
            new_name='address',
        ),
    ]