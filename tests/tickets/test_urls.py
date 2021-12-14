import datetime

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from pytz import UTC
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient


@pytest.fixture
def tickets(db):
    return [mixer.blend('tickets.ticket') for _ in range(3)]


def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def test_post_anon_user_get_nothing():
    path = reverse('tickets-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_get_ticket_user_logged(tickets):
    path = reverse('tickets-detail', kwargs={'pk': tickets[0].pk})
    client = get_client(User.objects.create_user('prova', 'prova@example.it', 'prova99'))
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


def test_update_ticket_user_not_author(tickets):
    path = reverse('tickets-detail', kwargs={'pk': tickets[0].pk})
    user = User.objects.create_user('prova', 'prova@example.it', 'prova99')
    client = get_client(tickets[0].author)
    timeFlight = datetime.time(10, 12, 0)
    response = client.put(path, data={'author': user.pk, 'name': 'Johnny', 'surname': 'Colombo', 'departure': 'Lamezia',
                                      'destination': 'Torino', 'price': 25,
                                      'departureDateTime': datetime.datetime(2021, 12, 25, tzinfo=UTC),
                                      'timeFlight': timeFlight})
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_update_ticket_user_author(tickets):
    path = reverse('tickets-detail', kwargs={'pk': tickets[0].pk})
    client = get_client(tickets[0].author)
    response = client.put(path, data={'author': tickets[0].author.pk, 'name': 'Johnny', 'surname': 'Colombo',
                                      'departure': 'Lamezia Terme',
                                      'destination': 'Torino', 'price': 25,
                                      'departureDateTime': datetime.datetime(2021, 12, 25, tzinfo=UTC),
                                      'timeFlight': datetime.time(1, 30)})
    assert response.status_code == HTTP_200_OK


def test_create_ticket_user_not_author(tickets):
    path = reverse('tickets-list')
    client = get_client(User.objects.create_user('prova', 'prova@example.it', 'prova99'))
    user = User.objects.create_user('prova2', 'prova2@example.it', 'prova299')
    response = client.post(path,
                           data={'author': user.pk, 'name': 'Johnny', 'surname': 'Colombo', 'departure': 'Lamezia',
                                 'destination': 'Torino', 'price': 25,
                                 'departureDateTime': datetime.datetime(2021, 12, 25, tzinfo=UTC),
                                 'timeFlight': datetime.time(1, 30)})
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_create_ticket_user_author(tickets):
    path = reverse('tickets-list')
    user = User.objects.create_user('prova', 'prova@example.it', 'prova99')
    client = get_client(user)
    response = client.post(path,
                           data={'author': user.pk, 'name': 'Johnny', 'surname': 'Colombo', 'departure': 'Lamezia Terme',
                                 'destination': 'Torino', 'price': 25,
                                 'departureDateTime': datetime.datetime(2021, 12, 25, tzinfo=UTC),
                                 'timeFlight': datetime.time(1, 30)})
    assert response.status_code == HTTP_200_OK
