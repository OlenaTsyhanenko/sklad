from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace


class Traffic(models.Model):
    name = models.CharField(verbose_name="Юр.лицо", max_length=50, blank=True)
    dateRegister = models.DateTimeField(default=datetime.now, verbose_name="Дата реєстрації")
    dateArrival = models.DateTimeField(null=True, blank=True, verbose_name="Очікуємое прибиття")
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата прибитя")
    timeProc = models.IntegerField(default=0, verbose_name="Хвилин на розвантаження", null=True, blank=True)
    sklad = models.ForeignKey(WarehouseSpace, on_delete=models.CASCADE, null=True, verbose_name="На склад")
    coutPalletAll = models.IntegerField(verbose_name="кількість палет", null=True, blank=True)
    unloads = models.BooleanField(default=False, null=True, blank=True, verbose_name="Розвантаження")

    categories2 = (
        ("Відправлен", "Відправлен"),
        ("Прибув", "Прибув"),
        ("Прийнятий", "Прийнятий"),
        ("Скасований", "Скасований"),
    )

    status = models.CharField(
        default="Відправлен",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.name, self.dateRegister)
    class Meta:
        verbose_name = u"Вантажопотік"
        verbose_name_plural = u"Вантажопотік"



