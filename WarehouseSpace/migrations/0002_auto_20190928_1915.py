# Generated by Django 2.2.5 on 2019-09-28 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelving', '0002_auto_20190928_1915'),
        ('WarehouseSpace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousespace',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='кількість стеллажей'),
        ),
        migrations.AddField(
            model_name='warehousespace',
            name='shelving',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shelving.Shelving', verbose_name='Стеллажи'),
        ),
        migrations.AddField(
            model_name='warehousespace',
            name='sizeGr',
            field=models.IntegerField(blank=True, null=True, verbose_name='Площадь грузовая'),
        ),
        migrations.AlterField(
            model_name='warehousespace',
            name='size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Площадь помещения'),
        ),
        migrations.AlterField(
            model_name='warehousespace',
            name='typeProduct',
            field=models.CharField(choices=[('Сухі товари', 'Сухі товари'), ('Швидко псуються товари', 'Швидко псуються товари'), ('Крихкі товари', 'Крихкі товари')], default='Вантажник', max_length=30, verbose_name='Тип склада'),
        ),
    ]
