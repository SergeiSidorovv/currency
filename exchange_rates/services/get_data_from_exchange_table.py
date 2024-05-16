from django.db.models import Prefetch
from django.db.models.manager import BaseManager

from guide_currency.models import Currency
from exchange_rates.models import ExchangeRates


def get_data_by_date(requested_date: str) -> BaseManager[ExchangeRates]:
    """
    Retrieves currency exchange rate information by date from the database.

    Keyword argument:
    requested_date -- the date for which the data needs to be found.

    Returns:
    Exchange rates.
    """

    data_currency = ExchangeRates.objects.filter(date=requested_date).only("date", "value", "currency").prefetch_related(
        Prefetch("currency", Currency.objects.only("name", "char_code")))

    return data_currency
