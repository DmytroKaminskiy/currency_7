from django.http import HttpResponse

from currency.models import Rate


def rate_list(request):
    rates = []
    for rate in Rate.objects.all():
        rates.append([rate.id, rate.sale, rate.buy])
    return HttpResponse(str(rates))
