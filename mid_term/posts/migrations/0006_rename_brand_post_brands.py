# Generated by Django 5.1.3 on 2024-12-17 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='brand',
            new_name='brands',
        ),
    ]