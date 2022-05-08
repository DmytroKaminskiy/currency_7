
from rest_framework import generics, viewsets

from api.v1.filters import RateFilter
from api.v1.pagination import RatesPagination
from api.v1.serializers import RateSerializer
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


'''
serialize == json.dumps
desirialize == json.loads

1. Показать список всех объектов модели Source.
2. Создать CRUD операции для модели ContactUs (отправить письмо при создании) Serializer.create link

1.x
1.1 - no filters
1.2 - has filters
1.3

# response structure
2.x
2.1
2.2

'''