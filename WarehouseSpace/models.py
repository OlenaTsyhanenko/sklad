from django.db import models
from shelving.models import Shelving


class WarehouseSpace(models.Model):
    name = models.CharField(verbose_name="Назва склада", max_length=30, blank=True)
    height = models.IntegerField(verbose_name="розміри помещения (Висота)", null=True, blank=True)
    size = models.IntegerField(verbose_name="Площадь помещения", null=True, blank=True)
    optimumTemperature = models.IntegerField(verbose_name="Температура склада", null=True, blank=True)
    shelving = models.ForeignKey(Shelving, on_delete=models.CASCADE, null=True, verbose_name="Стеллажи")
    count = models.IntegerField(verbose_name="кількість стеллажей", null=True, blank=True)
    secToPal = models.IntegerField(verbose_name="Секунд на розвантаження 1 палету", default=12)
    secToPalZ = models.IntegerField(verbose_name="Секунд на загрузку 1 палету", default=12)
    categories = (
        ("Сухі товари", "Сухі товари"),
        ("Швидко псуються товари", "Швидко псуються товари"),
        ("Крихкі товари", "Крихкі товари"),
    )
    typeProduct = models.CharField(
        default="Сухі товари",
        max_length=30,
        verbose_name="Тип склада",
        choices=categories
    )

    def get_S_pol(self):
        S_shelving = (self.shelving.lengthS/1000) * (self.shelving.widthS/1000)
        return round(S_shelving * self.count)

    def __str__(self):
        return "{0}_{1}".format(self.name, self.typeProduct)

    class Meta:
        verbose_name = u"Склад"
        verbose_name_plural = u"Склад"
