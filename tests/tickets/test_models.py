import datetime

from django.core.exceptions import ValidationError
from mixer.backend.django import mixer, UTC
import pytest

from tickets.validators import validate_len, validate_price, validate_current_date, validate_limit_min_time


def test_ticket_name_length_51_raises_exception(db):
    ticket = mixer.blend('tickets.ticket', name='A'*51)
    with pytest.raises(ValidationError) as err:
        ticket.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)


def test_ticket_surname_length_51_raises_exception(db):
    ticket = mixer.blend('tickets.ticket', surname='A'*51)
    with pytest.raises(ValidationError) as err:
        ticket.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)


def test_ticket_departure_length_51_raises_exception(db):
    ticket = mixer.blend('tickets.ticket', departure='A' * 51)
    with pytest.raises(ValidationError) as err:
        ticket.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)


def test_ticket_destination_length_51_raises_exception(db):
    ticket = mixer.blend('tickets.ticket', destination='A' * 51)
    with pytest.raises(ValidationError) as err:
        ticket.full_clean()
    assert 'at most 50 characters' in '\n'.join(err.value.messages)


def test_validate_len():
    with pytest.raises(ValidationError):
        validate_len("")


def test_validate_price():
    with pytest.raises(ValidationError):
        validate_price(-1)


def test_validate_current_date():
    with pytest.raises(ValidationError):
        validate_current_date(datetime.datetime(2020, 1, 1, 0, 0, tzinfo=UTC))


def test_validate_limit_min_time():
    with pytest.raises(ValidationError):
        validate_limit_min_time(datetime.time(0, 20, 00))


