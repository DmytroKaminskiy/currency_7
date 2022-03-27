from django.urls import path
from currency import views as currency_views

app_name = 'currency'

urlpatterns = [
    path('example/', currency_views.ExampleView.as_view(), name='example-delete-me'),

    # Rate
    path('rate/list/', currency_views.RateList.as_view(), name='rate_list'),
    path('rate/create/', currency_views.RateCreate.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', currency_views.RateUpdate.as_view(), name='rate_update'),
    path('rate/detail/<int:pk>/', currency_views.RateDetail.as_view(), name='rate_detail'),
    path('rate/delete/<int:pk>/', currency_views.RateDelete.as_view(), name='rate_delete'),

    # contactus
    path('contact-us/', currency_views.ContactUsCreate.as_view(), name='contactus_create'),
]
