# Generated by Django 3.1.1 on 2020-10-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20201002_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subCategories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.DeleteModel(
            name='subCategory',
        ),
    ]
