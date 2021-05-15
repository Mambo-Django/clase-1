from django.urls import path
from . import views

### sitioweb.com/encuestas/..

urlpatterns = [
    path('', views.index, name='index'),
    path('encuesta-usuario', views.otravista, name='otra_vista'),
    path('calculadora/<str:operacion>/<int:numero1>/<int:numero2>', views.calculadora, name='calculadora'),
    path('login', views.login, name='login'),
    path('verificar', views.verificar, name='verificarusuario'),

]