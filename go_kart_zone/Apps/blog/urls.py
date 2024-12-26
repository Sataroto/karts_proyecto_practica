from django.urls import path
from django.conf import settings

from go_kart_zone.Apps.blog import views

urlpatterns = [
    path('', views.blog, name = 'blog' ),
    path('categoria/<int:categoria_id>', views.categorias, name="categoria")
]
