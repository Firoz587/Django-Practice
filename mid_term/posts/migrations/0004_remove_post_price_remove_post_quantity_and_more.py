# Generated by Django 5.1.3 on 2024-12-17 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0003_remove_post_brand_post_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='post',
            name='brand',
        ),
        migrations.AddField(
            model_name='post',
            name='brand',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
