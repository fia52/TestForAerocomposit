from django.db import models


class Currency(models.Model):
    class Meta:
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"

    name = models.CharField(max_length=50, verbose_name="Наименование")
    symbol = models.CharField(max_length=10, verbose_name="Краткое обозначение")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс валюты (USD)")

    def __str__(self):
        return self.symbol
