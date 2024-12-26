from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from go_kart_zone.Apps.sitio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('tienda', views.tienda, name = "tienda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)