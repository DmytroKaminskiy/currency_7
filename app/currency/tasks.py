from decimal import Decimal

from celery import shared_task
import requests
from django.conf import settings
from django.core.mail import send_mail

from currency import model_choices as mch


def round_decimal(value: str) -> Decimal:
    """

    """
    places = Decimal(10) ** -2
    return Decimal(value).quantize(places)


@shared_task
def contact_us_async(subject, email_from, message_body):
    subject = f"Contact us: {subject}"
    message_body = f'''
            Support Email

            From: {email_from}
            Message: {message_body}
            '''
    email_from = settings.EMAIL_HOST_USER
    send_mail(
        subject,
        message_body,
        email_from,
        [email_from],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currencies = {
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
        'BTC': mch.RateType.BTC,
        'UAH': mch.RateType.UAH,
    }
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]

    for rate in rates:
        currency_type = available_currencies.get(rate['ccy'])
        if not currency_type:
            continue

        base_currency_type = available_currencies.get(rate['base_ccy'])

        sale = round_decimal(rate["sale"])
        buy = round_decimal(rate['buy'])

        last_rate = Rate.objects \
            .filter(source=source, type=currency_type) \
            .order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                base_type=base_currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_monobank():
    pass


@shared_task
def parse_vkurse():
    pass
