from django.urls import path

from .views import home, zgloszenia_lista

urlpatterns = [
    path('', home, name='home'),
    path('zgloszenia/', zgloszenia_lista, name='zgloszenia_lista'),
]
