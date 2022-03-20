from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('currency/', include('currency.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
