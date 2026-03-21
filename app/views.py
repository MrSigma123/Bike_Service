from django.shortcuts import render

from .models import Zgloszenie


def home(request):
    ostatnie_zgloszenia = Zgloszenie.objects.select_related('klient', 'rower')[:5]
    context = {
        'ostatnie_zgloszenia': ostatnie_zgloszenia,
        'tytul': 'Strona główna',
    }
    return render(request, 'app/home.html', context)


def zgloszenia_lista(request):
    zgloszenia = Zgloszenie.objects.select_related('klient', 'rower')
    context = {
        'zgloszenia': zgloszenia,
        'tytul': 'Lista zgłoszeń',
    }
    return render(request, 'app/zgloszenia_lista.html', context)
