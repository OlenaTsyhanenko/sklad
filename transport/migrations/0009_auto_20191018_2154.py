# Generated by Django 2.2.5 on 2019-10-18 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0008_transport_unloadstr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='unloads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='traffic.Traffic', verbose_name='Разгружает Вантажопотік'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='unloadsTr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unload.Unloader', verbose_name='Разгружает Вантажопотік'),
        ),
    ]