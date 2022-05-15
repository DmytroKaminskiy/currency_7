from datetime import datetime, timedelta

from django.conf import settings
from django.urls import reverse
from rest_framework.test import APIClient

from currency.models import Source, Rate


def test_rates_get_list(api_client):
    response = api_client.get(reverse('api-v1:rate-list'))
    assert response.status_code == 200
    assert response.json()


def test_rates_post_empty_data(api_client):
    response = api_client.post(reverse('api-v1:rate-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_rates_post_valid_data(api_client):
    source = Source.objects.last()
    payload = {
        'sale': 23,
        'buy': 24,
        'source': source.id,
    }
    response = api_client.post(reverse('api-v1:rate-list'), data=payload)
    assert response.status_code == 201
    assert response.json()


def test_rates_patch_valid_data(api_client):
    rate = Rate.objects.last()

    payload = {
        'sale': 9999,
    }
    response = api_client.patch(reverse('api-v1:rate-detail', args=[rate.id]), data=payload)
    assert response.status_code == 200
    assert response.json()['sale'] == '9999.00'


def test_rates_delete(api_client):
    rate = Rate.objects.last()

    response = api_client.delete(reverse('api-v1:rate-detail', args=[rate.id]))
    assert response.status_code == 204
    assert response.content == b''


def test_rates_delete_timeout(api_client):
    rate = Rate.objects.last()
    rate.created = datetime.now() - timedelta(minutes=settings.MINUTES_BEFORE_ALLOW_DELETE_RATE + 100)
    rate.save()

    response = api_client.delete(reverse('api-v1:rate-detail', args=[rate.id]))
    assert response.status_code == 400
    assert response.json()