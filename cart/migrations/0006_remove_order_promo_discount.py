# Generated by Django 3.1.1 on 2020-10-03 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20201003_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='promo_discount',
        ),
    ]
