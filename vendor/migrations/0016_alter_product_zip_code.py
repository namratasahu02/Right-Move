# Generated by Django 4.0.2 on 2022-02-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0015_alter_product_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
