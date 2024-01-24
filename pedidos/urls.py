from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.procesar_pedido, name="Pedidos"),
]