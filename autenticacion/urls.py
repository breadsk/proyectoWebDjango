from django.urls import path
from .views import VRegistro

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion")
]