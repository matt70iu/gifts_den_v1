# Generated by Django 3.2 on 2023-02-06 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='wishlist',
        ),
    ]