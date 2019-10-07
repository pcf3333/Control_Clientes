from django.urls import path

from . import views

urlpatterns = [
    path('', views.control_clientes, name='control_clientes'),
]