from django import forms

from .models import Rower, Zgloszenie


class RowerForm(forms.ModelForm):
    class Meta:
        model = Rower
        fields = ['klient', 'marka', 'model', 'typ', 'numer_seryjny']
        labels = {
            'klient': 'Klient',
            'marka': 'Marka',
            'model': 'Model',
            'typ': 'Typ roweru',
            'numer_seryjny': 'Numer seryjny',
        }


class ZgloszenieForm(forms.ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ['klient', 'rower', 'opis_usterki', 'status']
        labels = {
            'klient': 'Klient',
            'rower': 'Rower',
            'opis_usterki': 'Opis usterki',
            'status': 'Status',
        }
