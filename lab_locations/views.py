from rest_framework import generics
from rest_framework.response import Response
import requests
from django.conf import settings

class LabListView(generics.ListAPIView):
    def get(self, request):
        location = request.GET.get('location')
        api_key = settings.GOOGLE_MAPS_API_KEY
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=laboratory+in+{location}&radius=5000&key={api_key}"
        response = requests.get(url)
        data = response.json()
        return Response(data)

lab_location = LabListView.as_view()

class PharmacyListView(generics.ListAPIView):
    def get(self, request):
        location = request.GET.get('location')
        api_key = settings.GOOGLE_MAPS_API_KEY
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=pharmacy+in+{location}&radius=5000&key={api_key}"
        response = requests.get(url)
        data = response.json()
        return Response(data)

pharmacy_location = PharmacyListView.as_view()
# Create your views here.
