# Generated by Django 4.0.2 on 2022-02-16 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0005_rename_type_name_size_unit_unit_name'),
        ('vendor', '0011_remove_product_size_remove_product_size_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.size_unit'),
        ),
    ]
