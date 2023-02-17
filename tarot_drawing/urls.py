from django.conf import settings
from django.urls import path
from tarot_drawing import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.tarot_drawing, name='tarot_drawing'),
]

urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)