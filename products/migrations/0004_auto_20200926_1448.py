# Generated by Django 3.1.1 on 2020-09-26 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_order_orderproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproducts',
            name='orderd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
