from django.conf import settings

from currency.models import ContactUs


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_contact_us_get(admin_custom_client):
    response = admin_custom_client.get('/currency/contact-us/')
    assert response.status_code == 200


def test_contact_us_post_empty_data(admin_custom_client):
    response = admin_custom_client.post('/currency/contact-us/')
    assert response.status_code == 200  # when post 200 is error
    assert response.context_data['form'].errors == {
        'subject': ['This field is required.'],
        'email': ['This field is required.'],
        'message_body': ['This field is required.'],
    }


def test_contact_us_post_valid_data(admin_custom_client, mailoutbox):
    initial_count = ContactUs.objects.count()

    payload = {
        'subject': 'Subject Example',
        'email': 'emailcontactus@example.com',
        'message_body': 'Example Text\n' * 10,
    }
    response = admin_custom_client.post('/currency/contact-us/', data=payload)
    assert response.status_code == 302
    assert response.url == '/'

    assert len(mailoutbox) == 1
    assert mailoutbox[0].to == [settings.EMAIL_HOST_USER]
    assert mailoutbox[0].subject == 'Contact us: Subject Example'

    assert ContactUs.objects.count() == initial_count + 1


def test_contact_us_post_invalid_email(admin_custom_client, mailoutbox):
    initial_count = ContactUs.objects.count()
    payload = {
        'subject': 'Subject Example',
        'email': 'emailcontactus',
        'message_body': 'Example Text\n' * 10,
    }
    response = admin_custom_client.post('/currency/contact-us/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}
    assert len(mailoutbox) == 0
    assert ContactUs.objects.count() == initial_count
