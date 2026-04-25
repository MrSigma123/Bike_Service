from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rowery/', views.rowery, name='rowery'),
	path('zgloszenia/', views.zgloszenia, name='zgloszenia'),
	path('czesci/', views.czesci, name='czesci'),
]

