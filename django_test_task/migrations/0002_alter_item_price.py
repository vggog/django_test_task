# Generated by Django 4.1.3 on 2022-11-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]