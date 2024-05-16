from guide_currency.models import Currency


def add_currency_in_table_currency(data_for_currency: dict):
    """
    Adds data with the name of the currency and its char_code to the Currency table.

    Keyword arguments:
    data_for_currency -- currency data to be added to the Currency table in the database.
    """

    valute_data = data_for_currency["Valute"].items()
    for currency_key, currency_data in valute_data:
        Currency.objects.update_or_create(
            char_code=currency_key,
            defaults={
                "char_code": currency_key,
                "name": currency_data['Name']
            }
        )
