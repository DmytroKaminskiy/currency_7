import uuid

import pytest
from django.core.management import call_command
from rest_framework.test import APIClient

from accounts.models import User


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'sources.json',
            'rates.json',
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')


@pytest.fixture()
def api_client():
    client = APIClient()
    # print('BEFORE EACH TEST')
    yield client
    # print('AFTER EACH TEST')


@pytest.fixture(scope='session')
def admin_custom_client(django_db_setup, django_db_blocker):
    from django.test.client import Client

    with django_db_blocker.unblock():
        print('BEFORE EACH TEST')

        email = str(uuid.uuid4()).replace('-', '') + '@mail.com'
        user = User.objects.create(email=email, is_staff=True, is_superuser=True, is_active=True)

        client = Client()
        client.force_login(user)
        yield client

        user.delete()
        print('AFTER EACH TEST')
