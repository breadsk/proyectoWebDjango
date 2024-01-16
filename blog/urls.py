from django.urls import path
from django.conf import settings

from . import views

from django.conf.urls.static import static

urlpatterns = [    
    path('', views.blog, name= "Blog"),
    path('categoria/<int:categoria_id>/', views.categoria , name= "categoria")
]     

