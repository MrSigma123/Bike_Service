from django.db import models


class Uzytkownik(models.Model):
    ROLE_CHOICES = [
        ('klient', 'Klient'),
        ('mechanik', 'Mechanik'),
        ('admin', 'Admin'),
    ]

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    login = models.CharField(max_length=50, unique=True)
    haslo = models.CharField(max_length=255)
    rola = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        ordering = ['nazwisko', 'imie']

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Rower(models.Model):
    klient = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, related_name='rowery')
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    numer_seryjny = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['marka', 'model']

    def __str__(self):
        return f'{self.marka} {self.model}'


class Zgloszenie(models.Model):
    STATUS_CHOICES = [
        ('nowe', 'Nowe'),
        ('w_trakcie', 'W trakcie'),
        ('zakonczone', 'Zakończone'),
    ]

    klient = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, related_name='zgloszenia')
    rower = models.ForeignKey(Rower, on_delete=models.CASCADE, related_name='zgloszenia')
    data_zgloszenia = models.DateTimeField(auto_now_add=True)
    opis_usterki = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='nowe')

    class Meta:
        ordering = ['-data_zgloszenia']

    def __str__(self):
        return f'Zgłoszenie {self.id}'


class ZlecenieSerwisowe(models.Model):
    STATUS_CHOICES = [
        ('przyjete', 'Przyjęte'),
        ('diagnoza', 'Diagnoza'),
        ('naprawa', 'Naprawa'),
        ('gotowe', 'Gotowe'),
        ('wydane', 'Wydane'),
    ]

    zgloszenie = models.ForeignKey(Zgloszenie, on_delete=models.CASCADE, related_name='zlecenia')
    mechanik = models.ForeignKey(
        Uzytkownik,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='zlecenia_mechanika',
    )
    data_przyjecia = models.DateTimeField(auto_now_add=True)
    data_zakonczenia = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='przyjete')

    class Meta:
        ordering = ['-data_przyjecia']

    def __str__(self):
        return f'Zlecenie {self.id}'


class Diagnoza(models.Model):
    zlecenie = models.ForeignKey(ZlecenieSerwisowe, on_delete=models.CASCADE, related_name='diagnozy')
    opis_diagnozy = models.TextField()
    data_diagnozy = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Diagnoza {self.id}'


class RaportNaprawy(models.Model):
    zlecenie = models.ForeignKey(ZlecenieSerwisowe, on_delete=models.CASCADE, related_name='raporty')
    opis_czynnosci = models.TextField()
    data_raportu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Raport {self.id}'


class Czesc(models.Model):
    nazwa = models.CharField(max_length=100)
    stan_magazynowy = models.IntegerField(default=0)
    stan_minimalny = models.IntegerField(default=0)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['nazwa']

    def __str__(self):
        return self.nazwa


class ZuzytaCzesc(models.Model):
    zlecenie = models.ForeignKey(ZlecenieSerwisowe, on_delete=models.CASCADE, related_name='zuzyte_czesci')
    czesc = models.ForeignKey(Czesc, on_delete=models.CASCADE, related_name='zuzycia')
    ilosc = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.czesc} x {self.ilosc}'


class Powiadomienie(models.Model):
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, related_name='powiadomienia')
    zlecenie = models.ForeignKey(ZlecenieSerwisowe, on_delete=models.CASCADE, related_name='powiadomienia')
    tresc = models.TextField()
    data_wyslania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Powiadomienie {self.id}'


class Magazyn(models.Model):
    TYP_CHOICES = [
        ('przyjecie', 'Przyjęcie'),
        ('wydanie', 'Wydanie'),
    ]

    czesc = models.ForeignKey(Czesc, on_delete=models.CASCADE, related_name='operacje_magazynowe')
    ilosc = models.IntegerField()
    typ_operacji = models.CharField(max_length=20, choices=TYP_CHOICES)
    data_operacji = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.typ_operacji} - {self.czesc}'


class Platnosc(models.Model):
    STATUS_CHOICES = [
        ('oczekuje', 'Oczekuje'),
        ('oplacona', 'Opłacona'),
        ('anulowana', 'Anulowana'),
    ]

    zlecenie = models.ForeignKey(ZlecenieSerwisowe, on_delete=models.CASCADE, related_name='platnosci')
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data_platnosci = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='oczekuje')

    def __str__(self):
        return f'Płatność {self.id}'
