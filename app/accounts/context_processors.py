from django.conf import settings


def product_info(request):
    return {
        'BASE_PRODUCT_PRICE': settings.BASE_PRODUCT_PRICE,
    }
