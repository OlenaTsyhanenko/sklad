# Generated by Django 2.2.5 on 2019-10-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_auto_20191006_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='unloads',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Розвантаження'),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='timeProc',
            field=models.IntegerField(blank=True, null=True, verbose_name='Хвилин на розвантаження'),
        ),
    ]