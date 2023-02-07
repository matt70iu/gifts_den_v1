# Generated by Django 3.2 on 2023-02-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_contactusform'),
        ('products', '0010_auto_20230206_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='product_likes', to='profiles.UserProfile'),
        ),
    ]
