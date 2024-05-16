from exchange_rates.models import ExchangeRates
from guide_currency.models import Currency

from exchange_rates.services import get_date_for_model


def add_exchange_currency(data_for_currency: dict):
    """
    Adds currency exchange rate data to the ExchangeRates table of the database.

    Keyword argument:
    data_for_currency -- data with all currency information.
    """

    valute_data = data_for_currency['Valute'].items()
    date_str_for_model = get_date_for_model.get_date_for_model(
        data_for_currency)

    for currency_key, currency_data in valute_data:
        currency = Currency.objects.get(char_code=currency_key)

        ExchangeRates.objects.update_or_create(
            currency=currency,
            date=date_str_for_model,
            defaults={
                "currency": currency,
                "date": date_str_for_model,
                "value": currency_data["Value"]
            }
        )
