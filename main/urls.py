from django.urls import path, include
from . import views

urlpatterns = [
    path('data/', views.dataGet)
]
