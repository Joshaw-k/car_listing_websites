# Generated by Django 3.1.1 on 2020-12-14 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_listing_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_product',
            old_name='area_cat',
            new_name='area_category',
        ),
        migrations.RemoveField(
            model_name='seller_product',
            name='car_speed',
        ),
    ]
