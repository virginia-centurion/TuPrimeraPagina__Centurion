from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('curso/', views.curso, name='curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
]