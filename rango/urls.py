from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
  path('', views.index, name='index'),
  path('/rango/about/, views.index, name='about'),
]

