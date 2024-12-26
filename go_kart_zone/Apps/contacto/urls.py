from django.urls import path
from django.conf import settings

from go_kart_zone.Apps.contacto import views

urlpatterns = [
    path('', views.contacto, name='contacto')
]
