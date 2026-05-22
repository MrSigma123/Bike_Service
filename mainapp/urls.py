from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('rowery/', views.rowery, name='rowery'),
    path('rowery/dodaj/', views.dodaj_rower, name='dodaj_rower'),

    path('zgloszenia/', views.zgloszenia, name='zgloszenia'),
    path('zgloszenia/dodaj/', views.dodaj_zgloszenie, name='dodaj_zgloszenie'),

    path('czesci/', views.czesci, name='czesci'),
]
