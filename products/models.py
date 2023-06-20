from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace
from traffic.models import Traffic
from unload.models import Unloader


class Product(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=50, blank=True)
    optimumTemperature = models.IntegerField(verbose_name="Оптимальна температура товара", null=True, blank=True)
    shelfLife = models.DateTimeField(verbose_name="Термін придатності до", null=True, blank=True)
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата завантаження")
    dateUnUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата розвантаження")
    sklad = models.ForeignKey(WarehouseSpace, on_delete=models.CASCADE, null=True, verbose_name="Склад")
    traffic = models.ForeignKey(Traffic, on_delete=models.CASCADE, null=True, verbose_name="Вантажопотік")
    Unloader = models.ForeignKey(Unloader, on_delete=models.CASCADE, null=True, verbose_name="Вантажопотік розвантження")
    countPallet = models.IntegerField(verbose_name="кількість палет", null=True, blank=True)
    height = models.IntegerField(default=1500, verbose_name="Висота палета", null=True, blank=True)
    categories = (
        ("Сухі товари", "Сухі товари"),
        ("Швидко псуються товари", "Швидко псуються товари"),
        ("Крихкі товари", "Крихкі товари"),
    )
    categories2 = (
        ("Відправлен", "Відправлен"),
        ("У обробці", "У обробці"),
        ("Прийнятий", "Прийнятий"),
        ("Скасований", "Скасований"),
        ("Завантажений", "Завантажений"),
    )
    typeProduct = models.CharField(
        default="Сухі товари",
        max_length=30,
        verbose_name="Тип продукта",
        choices=categories
    )
    status = models.CharField(
        default="Відправлен",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.name, self.dateUpload)

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукт"


