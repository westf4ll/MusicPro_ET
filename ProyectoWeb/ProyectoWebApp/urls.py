from django.urls import path

from . import views
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('blog/', views.blog, name="Blog"),
    path('contact/', views.contact, name="Contact"),
    path('tienda/', views.tienda, name="Tienda"),
   
    path('pago/', views.pago, name="pago"),
    path('aprobado/', views.aprobado, name="aprobado"),
    path('error/', views.error, name='error'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)