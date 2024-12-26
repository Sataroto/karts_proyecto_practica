from django.urls import path
from django.conf import settings

from go_kart_zone.Apps.Servicios import views
urlpatterns = [
    path('',views.servicios, name='servicios')
]
