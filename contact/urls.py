from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', ContactInfoView.as_view(), name='contact2'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
