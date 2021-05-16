from django.urls import path
from . import views

### sitioweb.com/encuestas/..

urlpatterns = [
    path('', views.index, name='index'),
    
    path('login', views.login, name='login'),
    path('verificar', views.verificar, name='verificarusuario'),

    path('registrate', views.registrate, name="registrate")

]