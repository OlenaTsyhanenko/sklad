from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace


class Unloader(models.Model):
    dateRegister = models.DateTimeField(default=datetime.now, verbose_name="Дата реєстрації")
    dateArrival = models.DateTimeField(null=True, blank=True, verbose_name="Очікуємое время начала розвантження")
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата розвантаження")
    timeProc = models.IntegerField(default=0, verbose_name="Хвилин на розвантаження", null=True, blank=True)
    coutPalletAll = models.IntegerField(verbose_name="кількість палет", null=True, blank=True)
    loads = models.BooleanField(default=False, null=True, blank=True, verbose_name="Завантажений")

    categories2 = (
        ("Ожидание", "Ожидание"),
        ("Завантажений", "Завантажений"),
        ("Відправлен", "Відправлен"),
    )
    status = models.CharField(
        default="Ожидание",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.dateRegister, self.status)

    class Meta:
        verbose_name = u"Розвантаження"
        verbose_name_plural = u"Розвантаження"



