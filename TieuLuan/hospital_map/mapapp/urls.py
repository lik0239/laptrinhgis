from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('map/', views.map_view, name='map'),
    path('api/hospitals/', views.get_hospitals, name='api_hospitals'),
]
