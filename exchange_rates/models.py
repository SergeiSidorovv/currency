from django.db import models


class ExchangeRatesModels(models.Model):
    currency = models.ForeignKey(
        "guide_currency.Currency", on_delete=models.RESTRICT, verbose_name="id_валюты")
    date = models.DateField(verbose_name="дата")
    value = models.DecimalField(max_digits=9, decimal_places=4)

    class Meta:
        ordering = ['id']
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'
