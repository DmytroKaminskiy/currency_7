from django.core.management.base import BaseCommand
from currency.models import Rate


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'

    def handle(self, *args, **options):
        # response = requests.get(url)
        # response_json = response.json()
        print('HELLO FROM CUSTOM COMMAND')
        print(f'Rate Count: {Rate.objects.count()}')
