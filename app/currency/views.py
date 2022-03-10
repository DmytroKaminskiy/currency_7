from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Rate


def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', context={'rates': rates})


def index(request):
    return render(request, 'index.html')


def status_code(request):
    '''
    1xx - Info
    2xx - Success
      200 - Ok
      201 - Created
      202 - Accepted
      204 - No Content
    3xx - Redirect
      301 - Permanent
      307 - Temporary
    4xx - Client Error
      404 - Page Not Found
      400 - Bad Request
      401 - Unauthorized
      403 - Forbidden
    5xx - Server Error
      500 - Server fault
      502 -	Bad Gateway
      504 - Gateway Timeout
    '''
    if request.GET['exit'] == '0':
        return HttpResponse('OK', status=200)
        # return HttpResponse('OK', status=301, headers={'Location': 'https://google.com'})
    elif not request.GET['exit'].isdigit():
        return HttpResponse('OK', status=400)
    else:
        return HttpResponse('Fail')
