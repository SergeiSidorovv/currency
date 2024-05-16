from datetime import datetime


def check_date(date: str) -> bool:
    """
    Checks the correctness of the entered date.

    Keyword argument:
    date -- the date to check.

    Returns:
    Verification status, true or false.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
