from django.db import models


class Currency(models.Model):
    """A model for storing data about the name and char_code of the currency."""

    char_code = models.CharField(
        max_length=3, unique=True, verbose_name="CharCode")
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Название валюты")

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['id']
