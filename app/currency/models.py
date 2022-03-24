from django.db import models

# from currency.model_choices import RATE_TYPES
from currency import model_choices as mch


class Rate(models.Model):
    type = models.CharField(max_length=5, choices=mch.RateType.choices)  # noqa: A003
    source = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)


class ContactUs:
    pass


class Source:
    pass
