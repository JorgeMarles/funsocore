from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
    
    path('blog/<int:pk>', views.post_detalle, name='post_detalle'),
    path('nv', views.nov_lista, name='nov_lista'),
    path('novedad/<int:pk>', views.post_detalle, name='nov_detalle'),
    # More patterns to come later
] 

