
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('' , include('ProyectoWebApp.urls')),
] 
