from io import StringIO
from unittest.mock import patch
from django.core.management import call_command
from django.test import TestCase


class GuideCurrencyCommandTEst(TestCase):
    """Checks the operation of the command to receive, save, or modify data."""

    def setUp(self):
        self.return_value = {
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

    @patch("guide_currency.management.commands.add_currency.\
get_currency.get_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_currency.add_or_update_currency_in_table_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_exchangecurrency.add_exchange_currency")
    def test_handle_calling_get_currency(
        self,
        mock_add_exchange_currency,
        mock_add_or_update_currency,
        mock_get_currency
    ):
        """
        Checks that the method was called to get the data.

        Keyword arguments:
        mock_add_exchange_currency -- replaces data changes in exchange rates.
        mock_add_or_update_currency -- replaces changes in currency data.
        mock_get_currency -- replaces the API request to get data.
        """

        out = StringIO()
        mock_get_currency.return_value = self.return_value
        call_command("add_currency", stdout=out)
        mock_get_currency.assert_called_once()
        self.assertIn('Валюты были обновлены и добавлены', out.getvalue())

    @patch("guide_currency.management.commands.add_currency.\
get_currency.get_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_currency.add_or_update_currency_in_table_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_exchangecurrency.add_exchange_currency")
    def test_handle_add_or_update_currency_in_table_currency(
        self,
        mock_add_exchange_currency,
        mock_add_or_update_currency,
        mock_get_currency
    ):
        """
        Checks that the data received from the API has been updated,
        or added to the Currency table in the database.

        Keyword arguments:
        mock_add_exchange_currency -- replaces data changes in exchange rates.
        mock_add_or_update_currency -- replaces changes in currency data.
        mock_get_currency -- replaces the API request to get data.
        """

        out = StringIO()
        mock_get_currency.return_value = self.return_value
        call_command("add_currency", stdout=out)
        mock_add_or_update_currency.assert_called_once_with(self.return_value)
        self.assertIn('Валюты были обновлены и добавлены', out.getvalue())

    @patch("guide_currency.management.commands.add_currency.\
get_currency.get_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_currency.add_or_update_currency_in_table_currency")
    @patch("guide_currency.management.commands.add_currency.\
add_currency_in_table_exchangecurrency.add_exchange_currency")
    def test_handle_add_exchange_currency(
        self,
        mock_add_exchange_currency,
        mock_add_or_update_currency,
        mock_get_currency
    ):
        """
        Checks that the data received from the API has been updated,
        or added to the Currency table in the database.

        Keyword arguments:
        mock_add_exchange_currency -- replaces data changes in exchange rates.
        mock_add_or_update_currency -- replaces changes in currency data.
        mock_get_currency -- replaces the API request to get data.
        """
        out = StringIO()
        mock_get_currency.return_value = self.return_value
        call_command("add_currency", stdout=out)
        mock_add_exchange_currency.assert_called_once_with(self.return_value)
        self.assertIn('Валюты были обновлены и добавлены', out.getvalue())
