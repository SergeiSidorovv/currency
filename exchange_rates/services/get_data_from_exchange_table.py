from django.db.models import Prefetch

from guide_currency.models import Currency
from exchange_rates.models import ExchangeRates


def get_data_by_date(requested_date: str):

    data_currency = ExchangeRates.objects.filter(date=requested_date).only("date", "value", "currency").prefetch_related(
        Prefetch("currency", Currency.objects.only("name", "char_code")))

    return data_currency