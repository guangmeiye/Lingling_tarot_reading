from django.urls import path
from tarot_drawing import views

urlpatterns = [
    path('', views.tarot_drawing, name='tarot_drawing'),
]