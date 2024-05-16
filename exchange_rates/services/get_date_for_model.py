from datetime import datetime


def get_date_for_model(data_for_currency: dict) -> str:

    date = data_for_currency["Date"]
    date_object = datetime.fromisoformat(date)

    date_str_for_model = date_object.date().strftime('%Y-%m-%d')

    return date_str_for_model
