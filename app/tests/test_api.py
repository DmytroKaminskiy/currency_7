from django.urls import reverse
from rest_framework.test import APIClient

from currency.models import Source, Rate


def test_rates_get_list():
    client = APIClient()
    response = client.get(reverse('api-v1:rate-list'))
    assert response.status_code == 200
    assert response.json()


def test_rates_post_empty_data():
    client = APIClient()
    response = client.post(reverse('api-v1:rate-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_rates_post_valid_data():
    client = APIClient()
    source = Source.objects.last()
    payload = {
        'sale': 23,
        'buy': 24,
        'source': source.id,
    }
    response = client.post(reverse('api-v1:rate-list'), data=payload)
    assert response.status_code == 201
    assert response.json()


def test_rates_patch_valid_data():
    client = APIClient()
    rate = Rate.objects.last()

    payload = {
        'sale': 9999,
    }
    response = client.patch(reverse('api-v1:rate-detail', args=[rate.id]), data=payload)
    assert response.status_code == 200
    assert response.json()['sale'] == '9999.00'


def test_rates_delete():
    client = APIClient()
    rate = Rate.objects.last()

    response = client.delete(reverse('api-v1:rate-detail', args=[rate.id]))
    assert response.status_code == 204
    assert response.content == b''
