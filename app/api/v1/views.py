from datetime import datetime, timezone

from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.timesince import timesince
from django.views.decorators.cache import cache_page
from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from api.v1.filters import RateFilter
from api.v1.pagination import RatesPagination
from api.v1.serializers import RateSerializer
from api.v1.throttles import AnonCurrencyThrottle
from currency.models import Rate

from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

# class RateView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, CSVRenderer)
    pagination_class = RatesPagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ('id', 'sale', 'buy')
    throttle_classes = [AnonCurrencyThrottle]

    @method_decorator(cache_page(60 * 60 * 24 * 7))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        delta = now - instance.created
        minutes_pass = delta.total_seconds() / 60
        if minutes_pass >= settings.MINUTES_BEFORE_ALLOW_DELETE_RATE:
            return Response(
                {'errors': ['Two minutes pass.']}, status=status.HTTP_400_BAD_REQUEST)

        super().perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




'''
serialize == json.dumps
desirialize == json.loads

1. Показать список всех объектов модели Source.
2. Создать CRUD операции для модели ContactUs (отправить письмо при создании) Serializer.create link
'''