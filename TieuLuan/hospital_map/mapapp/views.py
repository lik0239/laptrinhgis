from django.shortcuts import render
from django.http import JsonResponse
from .models import Hospital

def index(request):
    return render(request, 'mapapp/index.html')

def map_view(request):
    return render(request, 'mapapp/map.html')

def get_hospitals(request):
    hospitals = Hospital.objects.all()
    data = [
        {"name": h.name, "lat": h.latitude, "lng": h.longitude}
        for h in hospitals
    ]
    return JsonResponse(data, safe=False)
