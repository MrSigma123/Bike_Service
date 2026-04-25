from django.shortcuts import render
from .models import Zgloszenie, Rower, Czesc


def home(request):
    context = {
        'liczba_zgloszen': Zgloszenie.objects.count(),
        'liczba_rowerow': Rower.objects.count(),
        'liczba_czesci': Czesc.objects.count(),
    }
    return render(request, 'home.html', context)
