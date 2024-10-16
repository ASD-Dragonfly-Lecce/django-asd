from django.urls import path

from . import views

app_name = 'pagamenti'

urlpatterns = [
    path("", views.index, name="payment_index")
]