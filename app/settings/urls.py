from django.contrib import admin
from django.urls import path
from currency import views as currency_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', currency_views.index),
    path('sc/', currency_views.status_code),
    path('rate/list/', currency_views.rate_list),
]
