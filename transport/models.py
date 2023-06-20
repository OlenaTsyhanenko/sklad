from django.db import models
from traffic.models import Traffic
from unload.models import Unloader


class Transport(models.Model):
    name = models.CharField(verbose_name="Назва техники", max_length=50, blank=True)
    timeUse = models.IntegerField(default=0, verbose_name="Хвилин использования за сегодня", null=True, blank=True)
    HoursDay = models.IntegerField(default=8, verbose_name="Норма годин в день", null=True, blank=True)
    allHours = models.IntegerField(default=6400, verbose_name="Ресурс использования в часах", null=True, blank=True)
    allHoursUse = models.IntegerField(default=0, verbose_name="Використовується годин", null=True, blank=True)
    unloads = models.ForeignKey(Traffic, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Разгружает Вантажопотік")
    unloadsTr = models.ForeignKey(Unloader, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Разгружает Вантажопотік")
    bTrucker = models.BooleanField(default=False, verbose_name="Это грузовик")
    coutPallet = models.IntegerField(default=4000, verbose_name="кількість палет вместимость (только для грузовиков)", null=True, blank=True)

    dateEditStatus = models.DateTimeField(null=True, blank=True, verbose_name="Дата изменения статуса")
    categories2 = (
        ("Простой", "Простой"),
        ("Використовується", "Використовується"),
    )
    status = models.CharField(
        default="Простой",
        max_length=30,
        verbose_name="Статус использования",
        choices=categories2
    )
    categories = (
        ("Сухі товари", "Сухі товари"),
        ("Швидко псуються товари", "Швидко псуються товари"),
        ("Крихкі товари", "Крихкі товари"),
    )
    typeTransport = models.CharField(
        default="Сухі товари",
        max_length=30,
        verbose_name="Тип транспорта",
        choices=categories
    )

    def __str__(self):
        return "{0}_{1}".format(self.name, self.typeTransport)

    class Meta:
        verbose_name = u"Транспорт"
        verbose_name_plural = u"Транспорт"
