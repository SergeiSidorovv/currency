from django.contrib import admin

from guide_currency.models import Currency


class CurrencyAdmin(admin.ModelAdmin):

    list_display = ["id", "char_code", "name"]
    fields = ["char_code", "name"]
    search_fields = ["id", "char_code", "name"]


admin.site.register(Currency, CurrencyAdmin)
