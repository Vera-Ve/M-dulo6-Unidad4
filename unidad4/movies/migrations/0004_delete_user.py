# Generated by Django 4.2.2 on 2023-06-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]