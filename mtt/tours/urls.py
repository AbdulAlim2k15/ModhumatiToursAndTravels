from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.service_view, name='services'),
    path('destinations/', views.destination_view, name='destination'),
    path('team/', views.team_view, name='team_members'),
    path('visa/', views.visa_view, name='visa'),
    path('contact/', views.contact_view, name='contact'),
]