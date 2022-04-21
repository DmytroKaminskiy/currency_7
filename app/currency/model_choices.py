from django.db import models


class RateType(models.TextChoices):
    UAH = 'UAH', 'Hrivna'
    USD = 'USD', 'Dollar'
    EUR = 'EUR', 'Euro'
    BTC = 'BTC', 'Bitcoin'



class SourceCodeName(models.IntegerChoices):
    PRIVATBANK = 1, 'PrivatBank'
    MONOBANK = 2, 'MonoBank'

# RATE_TYPE_USD = 'USD'
# RATE_TYPE_EUR = 'EUR'
#
# RATE_TYPES = (
#     (RATE_TYPE_USD, 'Dollar'),
#     (RATE_TYPE_EUR, 'Euro'),
# )
