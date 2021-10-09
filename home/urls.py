from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home')
]