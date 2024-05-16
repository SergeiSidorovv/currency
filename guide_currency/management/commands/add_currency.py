from django.core.management.base import BaseCommand
import requests

from guide_currency.services import get_currency, add_currency_in_table_currency
from exchange_rates.services import add_currency_in_table_exchangecurrency


class Command(BaseCommand):
    help = "Команда для получения и сохранения валют и их курсов"

    def handle(self, *args, **options):
        data_currency = get_currency.get_currency()
        add_currency_in_table_currency.add_currency_in_table_currency(
            data_currency)
        add_currency_in_table_exchangecurrency.add_exchange_currency(
            data_currency)

        self.stdout.write(
            self.style.SUCCESS('Валюты были обновлены и добавлены')
        )
