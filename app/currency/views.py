from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View

from currency.forms import RateForm, ContactUsForm
from currency.models import Rate, ContactUs

from django.conf import settings


class RateList(ListView):
    queryset = Rate.objects.all().order_by('-id').select_related('source')
    template_name = 'rate_list.html'


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


class ContactUsCreate(CreateView):
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
        subject = f"Contact us: {data['subject']}"
        message_body = f'''
        Support Email
        
        From: {data['email']}
        Message: {data['message_body']}
        '''
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message_body,
            email_from,
            [email_from],
            fail_silently = False,
        )

        return response

    def form_invalid(self, form):
        print('FORM INVALID')
        return super().form_invalid(form)


class ExampleView(View):
    def get(self, request):
        from django.http import HttpResponse
        from django.contrib.sessions.models import Session
        from django.contrib.auth.models import User

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
