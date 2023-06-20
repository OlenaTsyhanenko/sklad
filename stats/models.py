from django.db import models
from WarehouseSpace.models import WarehouseSpace


class Stats(models.Model):
    sklad = models.ForeignKey(WarehouseSpace, on_delete=models.CASCADE, null=True, verbose_name="Cклад")
    count = models.IntegerField(default=0, verbose_name="кількість Вантажопотіков Всіго", null=True, blank=True)
