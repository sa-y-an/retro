from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),

    # modalities

    path('ecg/', views.ecg , name='ecg'),
    path('eda/', views.eda , name='eda'),
    path('emg/', views.emg , name='emg'),
    path('resp/', views.resp , name='resp'),
    path('temp/', views.temp , name='temp'),

    # about section

    path('about/', views.about , name='about')

]