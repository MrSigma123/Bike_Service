from django.contrib import admin
from .models import (
    Uzytkownik, Rower, Zgloszenie, ZlecenieSerwisowe,
    Diagnoza, RaportNaprawy, Czesc, ZuzytaCzesc,
    Powiadomienie, Magazyn, Platnosc,
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
