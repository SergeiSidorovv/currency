from django.contrib import admin

from exchange_rates.models import ExchangeRates


class ExchangeRatesAdmin(admin.ModelAdmin):
    """The administrator model for interacting with the ExchangeRates table in the database."""

    list_display = ["id", "currency", "date", "value"]
    fields = ["currency", "date", "value"]
    search_fields = ["id", "currency", "date", "value"]

    list_prefetch_related = ["currency"]


admin.site.register(ExchangeRates, ExchangeRatesAdmin)
