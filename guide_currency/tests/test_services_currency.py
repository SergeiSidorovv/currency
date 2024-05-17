from unittest.mock import patch, Mock
from django.test import TestCase

from guide_currency.services import get_currency, add_currency_in_table_currency
from guide_currency.models import Currency


class ServicesCurrencyTest(TestCase):
    """Business logic tests in the guide currency app."""

    def setUp(self):
        Currency.objects.create(char_code="USD", name="Доллар США")
        Currency.objects.create(char_code="EUR", name="Евро")

        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        self.return_value = {
            "Date": "2024-05-17T11:30:00+03:00",
            "PreviousDate": "2024-05-16T11:30:00+03:00",
            "PreviousURL": "\/\/www.cbr-xml-daily.ru\/archive\/2024\/05\/16\/daily_json.js",
            "Timestamp": "2024-05-16T20:00:00+03:00",
            "Valute": {
                "AUD": {
                    "ID": "R01010",
                    "NumCode": "036",
                    "CharCode": "AUD",
                    "Nominal": 1,
                    "Name": "Австралийский доллар",
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
        self.status_code = 200

    @patch('guide_currency.services.get_currency.requests')
    def test_get_currency(self, mock_requests):
        """
        Make sure that the data you receive from the site is converted to the correct format..

        Keyword argument:
        mock_requests -- substituting the API request.
        """

        mock_response = Mock()
        mock_response.status_code = self.status_code
        mock_response.json.return_value = self.return_value
        mock_requests.get.return_value = mock_response

        call_function = get_currency.get_currency()

        mock_requests.get.assert_called_once_with(
            url="https://www.cbr-xml-daily.ru/daily_json.js",
            headers=self.headers,
            timeout=5
        )

        self.assertEqual(call_function, self.return_value)

    def test_update_currency_in_table_currency(self):
        """
        Checks that the data in the Currency table has been updated correctly.
        """

        add_currency_in_table_currency.add_or_update_currency_in_table_currency(
            self.return_value)

        data = Currency.objects.get(char_code="USD")
        expected_name = "Доллар США"
        expected_char_code = "USD"

        self.assertEqual(data.name, expected_name)
        self.assertEqual(data.char_code, expected_char_code)

    def test_add_currency_in_table_currency(self):
        """
        Checks that the data in the Currency table has been created correctly.
        """

        add_currency_in_table_currency.add_or_update_currency_in_table_currency(
            self.return_value)

        data = Currency.objects.get(char_code="EUR")
        expected_name = "Евро"
        expected_char_code = "EUR"

        self.assertEqual(data.name, expected_name)
        self.assertEqual(data.char_code, expected_char_code)
