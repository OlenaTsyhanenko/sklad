# Generated by Django 2.2.5 on 2019-10-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191005_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countPallet',
            field=models.IntegerField(blank=True, null=True, verbose_name='кількість палет'),
        ),
    ]