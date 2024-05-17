from decimal import Decimal
from django.test import TestCase

from exchange_rates.models import ExchangeRates
from guide_currency.models import Currency
from exchange_rates.services import (
    add_currency_in_table_exchangecurrency,
    check_format,
    get_data_from_exchange_table,
    get_date_for_model
)


class ServicesExchangeRatesTest(TestCase):
    """Business logic tests in the exchange rates app."""

    def setUp(self):
        self.data_for_currency = {
            "Date": "2024-05-16T11:30:00+03:00",
            "PreviousDate": "2024-05-16T11:30:00+03:00",
            "PreviousURL": "\/\/www.cbr-xml-daily.ru\/archive\/2024\/05\/16\/daily_json.js",
            "Timestamp": "2024-05-16T20:00:00+03:00",
            "Valute": {
                "EUR": {
                    "ID": "R01010",
                    "NumCode": "036",
                    "CharCode": "EUR",
                    "Nominal": 1,
                    "Name": "Евро",
                    "Value": 60.7281,
                    "Previous": 60.6679
                },
                "USD": {
                    "ID": "R01235",
                    "NumCode": "840",
                    "CharCode": "USD",
                    "Nominal": 1,
                    "Name": "Доллар США",
                    "Value": 90.9239,
                    "Previous": 91.2573
                },
            }
        }

        self.currency_usd = Currency.objects.create(
            char_code="USD", name="Доллар США")
        self.currency_eur = Currency.objects.create(
            char_code="EUR", name="Евро")

        ExchangeRates.objects.create(
            currency=self.currency_usd, date="2024-05-15", value=60.2970)
        ExchangeRates.objects.create(
            currency=self.currency_eur, date="2024-05-16", value=114.7744)

    def test_add_exchange_currency_create_data(self):
        """Check if the data is being added to the ExchangeRates table correctly."""

        add_currency_in_table_exchangecurrency.add_exchange_currency(
            self.data_for_currency)
        data = ExchangeRates.objects.get(
            currency=self.currency_usd, date="2024-05-16")
        expected_data = Decimal('90.9239')

        self.assertEqual(data.value, expected_data)

    def test_add_exchange_currency_update_data(self):
        """Check if the data is being updated to the ExchangeRates table correctly."""

        add_currency_in_table_exchangecurrency.add_exchange_currency(
            self.data_for_currency)
        data = ExchangeRates.objects.get(
            currency=self.currency_eur, date="2024-05-16")
        expected_data = Decimal('60.7281')

        self.assertEqual(data.value, expected_data)

    def test_check_date_by_correct_date(self):
        """Check whether the date is checked correctly with correct date."""

        correct_date = "2024-05-16"
        check = check_format.check_date(correct_date)
        expected_data = True

        self.assertEqual(check, expected_data)

    def test_check_date_by_uncorrect_date(self):
        """Check whether the date is checked correctly with uncorrect date."""

        correct_date = "2024-05-16-121"
        check = check_format.check_date(correct_date)
        expected_data = False

        self.assertEqual(check, expected_data)

    def test_get_data_by_date(self):
        """Checks which data is returned from the database by date."""

        requested_date = "2024-05-16"
        data = get_data_from_exchange_table.get_data_by_date(requested_date)

        expected_count_data = 1

        self.assertEqual(len(data), expected_count_data)

    def test_get_data_without_date(self):
        """Checks which data is returned from the database without date."""
        requested_date = "2024-05-01"
        data = get_data_from_exchange_table.get_data_by_date(requested_date)

        expected_count_data = 0

        self.assertEqual(len(data), expected_count_data)

    def test_get_date_for_model(self):
        """Checks the date conversion for the ExchangeRates model."""

        date = get_date_for_model.get_date_for_model(self.data_for_currency)

        expected_date = "2024-05-16"

        self.assertEqual(date, expected_date)
