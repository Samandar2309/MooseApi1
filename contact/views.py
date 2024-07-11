from rest_framework import generics
from .serializers import *


# Create your views here.

class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SubscribeView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = SubscribeSerializer
