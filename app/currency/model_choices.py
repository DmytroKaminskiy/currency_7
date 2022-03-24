from django.db import models


class RateType(models.TextChoices):
    USD = 'USD', 'Dollar'
    EUR = 'EUR', 'Euro'


# RATE_TYPE_USD = 'USD'
# RATE_TYPE_EUR = 'EUR'
#
# RATE_TYPES = (
#     (RATE_TYPE_USD, 'Dollar'),
#     (RATE_TYPE_EUR, 'Euro'),
# )
