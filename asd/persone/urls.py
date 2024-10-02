from django.urls import path
from . import views


app_name = 'persone'

urlspatterns = [
    path('', views.persona_list, name='persona_list'),
    path('<int:id>/', views.persona_detail, name='persona_detail')
]