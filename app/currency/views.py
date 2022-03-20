from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View

from currency.forms import RateForm
from currency.models import Rate


class RateList(ListView):
    queryset = Rate.objects.all().order_by('-id')
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


class ExampleView(View):
    def get(self, request):
        from django.http import HttpResponse
        a = 1 + 2
        return HttpResponse(f'Result {a}')
