from django.urls import path
from . import views


app_name = 'ricevute'

urlpatterns = [
    path('', views.prova, name='prova_pdf'),
]