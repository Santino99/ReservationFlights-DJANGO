import decimal
import datetime

from django.core.exceptions import ValidationError
from pytz import UTC


def validate_len(value: str) -> None:
    if len(value) == 0:
        raise ValidationError("Field must not be empty")


def validate_price(value: decimal) -> None:
    if value <= 0:
        raise ValidationError("Price must not be negative")


def validate_current_date(date_start: datetime) -> None:
    current_date = datetime.datetime.now()
    current_aware = datetime.datetime(current_date.year, current_date.month, current_date.day, current_date.hour, current_date.minute, current_date.second, current_date.microsecond, tzinfo=UTC)

    dt = (date_start - current_aware)
    if dt.days < 0:
        raise ValidationError("Start date is before of the current date")


def validate_limit_min_time(time: datetime.time()) -> None:
    current_time = datetime.time(00, 30, 00)
    if time < current_time:
        raise ValidationError("Time must not be less than 30 minutes")



