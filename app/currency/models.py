from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5)  # noqa: A003
    source = models.CharField(max_length=64)
    created = models.DateTimeField()
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
