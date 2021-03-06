# Generated by Django 3.1.1 on 2020-09-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cardNumber',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postCode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='provice',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
