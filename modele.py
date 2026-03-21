from django.db import models


class Uzytkownik(models.Model):
    ROLE_CHOICES = (
        ("klient", "Klient"),
        ("mechanik", "Mechanik"),
        ("admin", "Admin"),
    )

    id_uzytkownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    login = models.CharField(max_length=50, unique=True)
    haslo = models.CharField(max_length=255)
    rola = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        db_table = "uzytkownicy"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Rower(models.Model):
    id_roweru = models.AutoField(primary_key=True)
    id_klienta = models.ForeignKey(
        Uzytkownik,
        on_delete=models.CASCADE,
        db_column="id_klienta",
        related_name="rowery",
    )
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    numer_seryjny = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "rowery"

    def __str__(self):
        return f"{self.marka} {self.model}"


class Zgloszenie(models.Model):
    STATUS_CHOICES = (
        ("nowe", "Nowe"),
        ("w_trakcie", "W trakcie"),
        ("zakonczone", "Zakończone"),
    )

    id_zgloszenia = models.AutoField(primary_key=True)
    id_klienta = models.ForeignKey(
        Uzytkownik,
        on_delete=models.CASCADE,
        db_column="id_klienta",
        related_name="zgloszenia",
    )
    id_roweru = models.ForeignKey(
        Rower,
        on_delete=models.CASCADE,
        db_column="id_roweru",
        related_name="zgloszenia",
    )
    data_zgloszenia = models.DateTimeField()
    opis_usterki = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        db_table = "zgloszenia"

    def __str__(self):
        return f"Zgloszenie {self.id_zgloszenia}"


class ZlecenieSerwisowe(models.Model):
    STATUS_CHOICES = (
        ("przyjete", "Przyjęte"),
        ("w_realizacji", "W realizacji"),
        ("zakonczone", "Zakończone"),
    )

    id_zlecenia = models.AutoField(primary_key=True)
    id_zgloszenia = models.ForeignKey(
        Zgloszenie,
        on_delete=models.CASCADE,
        db_column="id_zgloszenia",
        related_name="zlecenia_serwisowe",
    )
    id_mechanika = models.ForeignKey(
        Uzytkownik,
        on_delete=models.CASCADE,
        db_column="id_mechanika",
        related_name="zlecenia_mechanika",
    )
    data_przyjecia = models.DateTimeField()
    data_zakonczenia = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        db_table = "zlecenia_serwisowe"

    def __str__(self):
        return f"Zlecenie {self.id_zlecenia}"


class Diagnoza(models.Model):
    id_diagnozy = models.AutoField(primary_key=True)
    id_zlecenia = models.ForeignKey(
        ZlecenieSerwisowe,
        on_delete=models.CASCADE,
        db_column="id_zlecenia",
        related_name="diagnozy",
    )
    opis_diagnozy = models.TextField()
    data_diagnozy = models.DateTimeField()

    class Meta:
        db_table = "diagnozy"

    def __str__(self):
        return f"Diagnoza {self.id_diagnozy}"


class RaportNaprawy(models.Model):
    id_raportu = models.AutoField(primary_key=True)
    id_zlecenia = models.ForeignKey(
        ZlecenieSerwisowe,
        on_delete=models.CASCADE,
        db_column="id_zlecenia",
        related_name="raporty_napraw",
    )
    opis_czynnosci = models.TextField()
    data_raportu = models.DateTimeField()

    class Meta:
        db_table = "raporty_napraw"

    def __str__(self):
        return f"Raport {self.id_raportu}"


class Czesc(models.Model):
    id_czesci = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    stan_magazynowy = models.IntegerField()
    stan_minimalny = models.IntegerField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "czesci"

    def __str__(self):
        return self.nazwa


class ZuzytaCzesc(models.Model):
    id_zuzycia = models.AutoField(primary_key=True)
    id_zlecenia = models.ForeignKey(
        ZlecenieSerwisowe,
        on_delete=models.CASCADE,
        db_column="id_zlecenia",
        related_name="zuzyte_czesci",
    )
    id_czesci = models.ForeignKey(
        Czesc,
        on_delete=models.CASCADE,
        db_column="id_czesci",
        related_name="zuzycia",
    )
    ilosc = models.IntegerField()

    class Meta:
        db_table = "zuzyte_czesci"

    def __str__(self):
        return f"Zuzycie {self.id_zuzycia}"


class Powiadomienie(models.Model):
    id_powiadomienia = models.AutoField(primary_key=True)
    id_uzytkownika = models.ForeignKey(
        Uzytkownik,
        on_delete=models.CASCADE,
        db_column="id_uzytkownika",
        related_name="powiadomienia",
    )
    id_zlecenia = models.ForeignKey(
        ZlecenieSerwisowe,
        on_delete=models.CASCADE,
        db_column="id_zlecenia",
        related_name="powiadomienia",
    )
    tresc = models.TextField()
    data_wyslania = models.DateTimeField()

    class Meta:
        db_table = "powiadomienia"

    def __str__(self):
        return f"Powiadomienie {self.id_powiadomienia}"


class Magazyn(models.Model):
    TYP_OPERACJI_CHOICES = (
        ("przyjecie", "Przyjęcie"),
        ("wydanie", "Wydanie"),
        ("korekta", "Korekta"),
    )

    id_operacji = models.AutoField(primary_key=True)
    id_czesci = models.ForeignKey(
        Czesc,
        on_delete=models.CASCADE,
        db_column="id_czesci",
        related_name="operacje_magazynowe",
    )
    ilosc = models.IntegerField()
    typ_operacji = models.CharField(max_length=20, choices=TYP_OPERACJI_CHOICES)
    data_operacji = models.DateTimeField()

    class Meta:
        db_table = "magazyn"

    def __str__(self):
        return f"Operacja {self.id_operacji}"


class Platnosc(models.Model):
    STATUS_CHOICES = (
        ("oczekujaca", "Oczekująca"),
        ("oplacona", "Opłacona"),
        ("anulowana", "Anulowana"),
    )

    id_platnosci = models.AutoField(primary_key=True)
    id_zlecenia = models.ForeignKey(
        ZlecenieSerwisowe,
        on_delete=models.CASCADE,
        db_column="id_zlecenia",
        related_name="platnosci",
    )
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data_platnosci = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        db_table = "platnosci"

    def __str__(self):
        return f"Platnosc {self.id_platnosci}"
