"""proyecto_seminario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Funsocore'                    # default: "Django Administration"
admin.site.index_title = 'Admin'                 # default: "Site administration"
admin.site.site_title = 'Funsocore' # default: "Django site admin"

from funsocore.forms import LoginUserPersonalizado
from django.contrib.auth import views
from django.views.generic import TemplateView

urlpatterns = [
   
    path('',views.TemplateView.as_view(template_name='ppal.html'),name='ppal'),
    path('donar',views.TemplateView.as_view(template_name='collab.html'),name='collab'),
     path('admin/login/', views.LoginView.as_view(
        template_name='admin/login.html',
        authentication_form=LoginUserPersonalizado),
        name='login'
    ),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


"""
<div class="form-row">
    {{ form.username.errors }}
    <label class="username" for="{{form.username.id_for_label}}">Usuario:</label>
    {{ form.username }}
  </div>
  <div class="form-row">
    {{ form.password.errors }}
    <label class="login" for="{{form.password.id_for_label}}">Contraseña:</label>
    {{ form.password }}
    <input type="hidden" name="next" value="{{ next }}">
  </div>
"""