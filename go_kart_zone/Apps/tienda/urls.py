from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from  go_kart_zone.Apps.tienda import views

urlpatterns = [
    path('', views.tienda, name = "tienda"),
]