from django.contrib import admin

from .models import (
    Czesc,
    Diagnoza,
    Magazyn,
    Platnosc,
    Powiadomienie,
    RaportNaprawy,
    Rower,
    Uzytkownik,
    Zgloszenie,
    ZlecenieSerwisowe,
    ZuzytaCzesc,
)

admin.site.register(Uzytkownik)
admin.site.register(Rower)
admin.site.register(Zgloszenie)
admin.site.register(ZlecenieSerwisowe)
admin.site.register(Diagnoza)
admin.site.register(RaportNaprawy)
admin.site.register(Czesc)
admin.site.register(ZuzytaCzesc)
admin.site.register(Powiadomienie)
admin.site.register(Magazyn)
admin.site.register(Platnosc)
