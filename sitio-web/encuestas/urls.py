from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encuesta-usuario', views.otravista, name='otra_vista'),
    path('calculadora/<str:operacion>/<int:numero1>/<int:numero2>', views.calculadora, name='calculadora')
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]