from django.core.management.base import BaseCommand

from guide_currency.services import get_currency, add_currency_in_table_currency
from exchange_rates.services import add_currency_in_table_exchangecurrency


class Command(BaseCommand):
    """The command to get new currency data."""

    help = "Команда для получения и сохранения валют и их курсов"

    def handle(self, *args, **options):
        """Save or updates data in the Currency and ExchangeRates tables of the database."""

        data_currency = get_currency.get_currency()
        add_currency_in_table_currency.add_or_update_currency_in_table_currency(
            data_currency)
        add_currency_in_table_exchangecurrency.add_exchange_currency(
            data_currency)

        self.stdout.write(
            self.style.SUCCESS('Валюты были обновлены и добавлены')
        )
