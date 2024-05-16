from django.views.generic.list import ListView
from django.http import Http404

from exchange_rates.models import ExchangeRates
from exchange_rates.services import get_data_from_exchange_table, check_format


class ExchangeRatesView(ListView):
    """A view for displaying currency exchange rate data."""

    model = ExchangeRates
    template_name = "exchange_rates/show_rates.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        """Returns a contact data with information about the currency exchange rate."""

        context = super().get_context_data(**kwargs)
        requested_date = self.request.GET.get("date")

        if requested_date is None:
            raise Http404()

        check_date = check_format.check_date(requested_date)

        if check_date is True:
            data_rates_by_date = get_data_from_exchange_table.get_data_by_date(
                requested_date)
            context["data_rates"] = data_rates_by_date
            return context

        raise Http404()
