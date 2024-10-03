from django.urls import path
from . import views


app_name = 'persone'

urlpatterns = [
    path('', views.PersonaListView.as_view(), name='persona_list'),
    path('<int:id>/', views.persona_detail, name='persona_detail'),
    path('iscrizione', views.tesserato_new, name='iscrizione'),
]