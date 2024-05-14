from django.db import models


class Currency(models.Model):

    char_code = models.CharField(max_length=3, verbose_name="CharCode")
    name = models.CharField(max_length=100, verbose_name="Название валюты")

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['id']
