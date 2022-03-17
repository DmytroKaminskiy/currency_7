from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from currency.forms import RateForm
from currency.models import Rate


def rate_list(request):
    rates = Rate.objects.all().order_by('-id')
    return render(request, 'rate_list.html', context={'rates': rates})


def rate_create(request):
    if request.method == 'POST':  # validate user data
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    else:  # get empty form
        form = RateForm()

    return render(request, 'rate_create.html', context={'form': form})


def rate_update(request, pk):
    # try:
    #     instance = Rate.objects.get(pk=pk)
    # except Rate.DoesNotExist:
    #     raise Http404(f'Object does not exist.')
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':  # validate user data
        form = RateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    else:  # get empty form
        form = RateForm(instance=instance)

    return render(request, 'rate_update.html', context={'form': form})


def rate_delete(request, pk):
    instance = get_object_or_404(Rate, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/rate/list/')
    else:
        return render(request, 'rate_delete.html', context={'rate': instance})


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
