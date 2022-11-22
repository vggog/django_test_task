# Generated by Django 4.1.3 on 2022-11-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test_task', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_id',
            field=models.TextField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]