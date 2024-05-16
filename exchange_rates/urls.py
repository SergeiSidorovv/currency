from django.urls import path

from exchange_rates import views


app_name = "exchange_rates"

urlpatterns = [
    path('show_rates', views.ExchangeRatesView.as_view(), name="show_rates")
]
