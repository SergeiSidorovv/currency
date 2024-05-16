import requests


def get_currency() -> dict:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    url = (
        "https://www.cbr-xml-daily.ru/daily_json.js"
    )
    response_currency = requests.get(url=url, headers=headers, timeout=5)

    json_data = response_currency.json()
    return json_data
