from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import QueryDict
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View
from django_filters.views import FilterView
from django.utils import timezone
from django.conf import settings

from currency.forms import RateForm, ContactUsForm
from currency.models import Rate, ContactUs
from currency.filters import RateFilter
from currency.tasks import contact_us_async



class RateList(FilterView):
    queryset = Rate.objects.all().order_by('-id').select_related('source')
    template_name = 'rate_list.html'
    paginate_by = 20
    filterset_class = RateFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        query_params = QueryDict(mutable=True)
        for key, value in self.request.GET.items():
            if key != 'page':
                query_params[key] = value

        context['filter_params'] = query_params.urlencode()
        return context


class RateDetail(DetailView):
    model = Rate
    template_name = 'rate_detail.html'


class RateCreate(CreateView):
    model = Rate
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateUpdate(UpdateView):
    model = Rate
    template_name = 'rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDelete(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class ContactUsCreate(LoginRequiredMixin, CreateView):
    '''
    SMTP - simple mail transfer protocol
    '''
    model = ContactUs
    template_name = 'contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        contact_us_async.delay(
            data['subject'],
            data['email'],
            data['message_body'],
        )
        return response

    def form_invalid(self, form):
        # print('FORM INVALID')
        return super().form_invalid(form)


class ExampleView(View):
    def get(self, request):
        from django.http import HttpResponse
        from django.contrib.sessions.models import Session
        from django.contrib.auth.models import User
        from threading import current_thread
        from multiprocessing import current_process
        print(f'Current Thread: {current_thread()}')
        print(f'Current Process: {current_process()}')

        from time import sleep
        sleep(3)


        return HttpResponse('OK')

        # print(request.COOKIES['sessionid'])
        session_id = request.COOKIES.get('sessionid')
        if session_id:
            print('SessionId is present:', session_id)

            try:
                session_obj = Session.objects.get(session_key=session_id)
            except Session.DoesNotExist:
                print('Session not found')
            else:
                print(f'Session found:', session_obj)
                user_id = session_obj.get_decoded().get('_auth_user_id')
                try:
                    user = User.objects.get(id=user_id)
                except User.DoesNotExist:
                    print('User Not Found')
                else:
                    print(f'Request user email is ', user.email)
                    print(f'Request user email is ', request.user.email)

        else:
            print('is not authenticated')

        if request.user.is_authenticated:
            if request.COOKIES.get('example_page_visited'):
                return HttpResponse('Already visited')
            else:
                response = HttpResponse('First Visit')
                response.set_cookie('example_page_visited', True)
                return response
        else:
            return HttpResponse('Please, log in.')

#
# class RateListApiExample(View):
#     def get(self, request):
#         import json
#         rates = Rate.objects.all()
#         rates_response = []
#         for rate in rates:
#             obj_dict = {
#                 'id': rate.id,
#                 'buy': str(rate.buy),
#                 'sale': str(rate.sale),
#             }
#             rates_response.append(obj_dict)
#
#         return HttpResponse(json.dumps(rates_response), content_type='application/json')
