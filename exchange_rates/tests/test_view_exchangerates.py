from django.test import TestCase, Client
from django.urls import reverse

from exchange_rates.models import ExchangeRates
from guide_currency.models import Currency
from exchange_rates.views import ExchangeRatesView


class ExchangeRatesViewTest(TestCase):
    """Checks the operation of the ExchangeRatesView view"""

    def setUp(self):
        self.view = ExchangeRatesView()
        self.client = Client()
        self.currency_usd = Currency.objects.create(
            char_code="AUD", name="Австралийский доллар")
        self.currency_eur = Currency.objects.create(
            char_code="AZN", name="Азербайджанский манат")

        ExchangeRates.objects.create(
            currency=self.currency_usd, date="2024-05-15", value=60.2970)
        ExchangeRates.objects.create(
            currency=self.currency_eur, date="2024-05-16", value=114.7744)

    def test_url_status_code(self):
        """Checks whether the status of the code is received by url."""

        response = self.client.get("/show_rates?date=2024-05-15")
        expected_status = 200
        self.assertEqual(response.status_code, expected_status)

    def test_url_status_code_by_name(self):
        """Checks whether the status of the code is received by viewname."""

        response = self.client.get(reverse("exchange_rates:show_rates"), {
                                   "date": "2024-05-16"})
        expected_status = 200
        self.assertEqual(response.status_code, expected_status)

    def test_url_status_code_without_date(self):
        """Checks whether the status of the code is received by url without date."""

        response = self.client.get("/show_rates/")
        expected_status = 404
        self.assertEqual(response.status_code, expected_status)

    def test_url_status_code_with_uncorrect_date(self):
        """Checks whether the status of the code is received by url with uncorrect date."""

        response = self.client.get("/show_rates?date=2024-05-15-02")
        expected_status = 404
        self.assertEqual(response.status_code, expected_status)

    def test_table_used(self):
        """Checks which model is used in the view."""

        table = self.view.model
        expected_model = ExchangeRates
        self.assertEqual(table, expected_model)

    def test_template_name(self):
        """Checks which template_name is used in the view."""

        response = self.client.get("/show_rates?date=2024-05-15")
        expected_template_name = "exchange_rates/show_rates.html"

        self.assertTemplateUsed(response, expected_template_name)

    def test_get_context_data_with_correct_date(self):
        """Check whether the contextual data is received correctly, with the correct specified date."""

        response = self.client.get("/show_rates?date=2024-05-15")
        len_context_rates = len(response.context["data_rates"])
        expected_count_rates = 1

        self.assertEqual(len_context_rates, expected_count_rates)

    def test_get_context_data_without_data_by_date(self):
        """Check whether the contextual data is received correctly, without date."""

        response = self.client.get("/show_rates?date=2024-05-01")
        len_context_rates = len(response.context["data_rates"])
        expected_count_rates = 0

        self.assertEqual(len_context_rates, expected_count_rates)
