# Generated by Django 4.0.2 on 2022-02-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0005_rename_type_name_size_unit_unit_name'),
        ('vendor', '0007_rename_image_tag_image_image_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.image_type'),
        ),
    ]
