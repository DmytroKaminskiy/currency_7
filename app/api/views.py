
from rest_framework import generics, viewsets

from api.serializers import RateSerializer
from currency.models import Rate
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_csv.renderers import CSVRenderer

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

'''
serialize == json.dumps
desirialize == json.loads

1. Показать список всех объектов модели Source.
2. Создать CRUD операции для модели ContactUs (отправить письмо при создании) Serializer.create link
'''