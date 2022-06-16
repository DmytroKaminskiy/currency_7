from django.db import models

# from currency.model_choices import RATE_TYPES
from currency import model_choices as mch



class Source(models.Model):
    name = models.CharField(max_length=64, unique=True)
    code_name = models.PositiveSmallIntegerField(choices=mch.SourceCodeName.choices, unique=True)

    def __str__(self):
        return self.name


class Rate(models.Model):
    type = models.CharField(max_length=5, choices=mch.RateType.choices)  # noqa: A003
    base_type = models.CharField(max_length=5, choices=mch.RateType.choices, default=mch.RateType.UAH)
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='rates')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # clear cache for rates

    # def delete(self, using=None, keep_parents=False):

class ContactUs(models.Model):
    subject = models.CharField(max_length=128)
    message_body = models.CharField(max_length=2048)  # models.AreaField
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)



'''
OneToOne - 0..1
OneToMany - 0..inf
ManyToMany - 
'''

'''

'''