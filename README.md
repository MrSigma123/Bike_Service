# System Serwisu Rowerowego

Aplikacja webowa wspierająca obsługę serwisu rowerowego. System umożliwia rejestrację klientów, dodawanie rowerów, tworzenie zgłoszeń serwisowych, obsługę zleceń przez mechaników, zarządzanie magazynem części oraz kontrolę płatności i powiadomień.

Projekt został wykonany w Django z wykorzystaniem Django ORM oraz bazy danych PostgreSQL.

---

## Autorzy

- Karol Czołpiński
- [uzupełnij pozostałe osoby z grupy]

---

## Technologie

- Python
- Django
- PostgreSQL
- Django ORM
- HTML / CSS
- Django Templates

---

## Główne funkcjonalności

System obsługuje cztery role użytkowników:

### Klient

Klient może:

- zarejestrować konto,
- zalogować się do systemu,
- dodać swój rower,
- utworzyć zgłoszenie serwisowe,
- przeglądać swoje rowery,
- przeglądać swoje zgłoszenia,
- przeglądać swoje zlecenia,
- sprawdzać historię statusów,
- sprawdzać powiadomienia,
- sprawdzać płatności.

### Mechanik

Mechanik może:

- przeglądać przypisane zlecenia,
- przyjąć zlecenie do realizacji,
- dodać diagnozę,
- dodać raport naprawy,
- zarejestrować zużytą część,
- zmienić status zlecenia,
- przeglądać części.

### Magazynier

Magazynier może:

- przeglądać części,
- dodawać części,
- przeglądać zamówienia części,
- dodawać zamówienia części,
- dodawać pozycje zamówienia.

### Administrator aplikacji

Administrator aplikacji może:

- korzystać z panelu administratora aplikacji,
- dodawać użytkowników i nadawać im role,
- przeglądać dane systemu,
- zarządzać głównymi obszarami aplikacji.

Dodatkowo dostępny jest techniczny panel Django Admin pod adresem:

```text
/admin/
```

Panel Django Admin służy do technicznego zarządzania danymi, modelami oraz użytkownikami Django.

---

## Główne adresy aplikacji

```text
/                                  strona główna
/login/                            logowanie
/logout/                           wylogowanie
/rejestracja/                      publiczna rejestracja klienta

/panel-klienta/                    panel klienta
/panel-mechanika/                  panel mechanika
/panel-magazyniera/                panel magazyniera
/panel-admin/                      panel administratora aplikacji

/rowery/                           lista rowerów
/rowery/dodaj/                     dodawanie roweru

/zgloszenia/                       lista zgłoszeń
/zgloszenia/dodaj/                 dodawanie zgłoszenia

/zlecenia/                         lista zleceń
/zlecenia/<id>/                    szczegóły zlecenia
/zlecenia/<id>/status/             zmiana statusu zlecenia
/zlecenia/przyjmij/<id>/           przyjęcie zlecenia

/diagnozy/dodaj/                   dodawanie diagnozy
/raporty/dodaj/                    dodawanie raportu naprawy
/zuzyte-czesci/dodaj/              rejestrowanie zużytej części

/czesci/                           lista części
/czesci/dodaj/                     dodawanie części

/zamowienia-czesci/                lista zamówień części
/zamowienia-czesci/dodaj/          dodawanie zamówienia części
/pozycje-zamowienia/dodaj/         dodawanie pozycji zamówienia

/powiadomienia/                    lista powiadomień
/platnosci/                        lista płatności
/platnosci/dodaj/                  dodawanie płatności
```

---

## Model danych

Projekt zawiera 25 encji:

1. `Uzytkownik`
2. `Rower`
3. `Zgloszenie`
4. `ZlecenieSerwisowe`
5. `Diagnoza`
6. `RaportNaprawy`
7. `Czesc`
8. `ZuzytaCzesc`
9. `Powiadomienie`
10. `Magazyn`
11. `Platnosc`
12. `Adres`
13. `Kontakt`
14. `ProducentRoweru`
15. `TypRoweru`
16. `KategoriaCzesci`
17. `Dostawca`
18. `ZamowienieCzesci`
19. `PozycjaZamowienia`
20. `HistoriaStatusu`
21. `TerminSerwisu`
22. `StanowiskoSerwisowe`
23. `UslugaSerwisowa`
24. `WykonanaUsluga`
25. `NotatkaSerwisowa`

Relacje pomiędzy encjami zostały odwzorowane za pomocą Django ORM, głównie przez pola `ForeignKey`.

Przykładowe relacje:

```text
Uzytkownik 1 --- wiele Rower
Uzytkownik 1 --- wiele Zgloszenie
Rower 1 --- wiele Zgloszenie
Zgloszenie 1 --- wiele ZlecenieSerwisowe
ZlecenieSerwisowe 1 --- wiele Diagnoza
ZlecenieSerwisowe 1 --- wiele RaportNaprawy
ZlecenieSerwisowe 1 --- wiele ZuzytaCzesc
ZlecenieSerwisowe 1 --- wiele HistoriaStatusu
Czesc 1 --- wiele ZuzytaCzesc
KategoriaCzesci 1 --- wiele Czesc
Dostawca 1 --- wiele ZamowienieCzesci
ZamowienieCzesci 1 --- wiele PozycjaZamowienia
```

---

## Statusy zlecenia serwisowego

Zlecenie serwisowe może mieć status:

```text
nowe
w_realizacji
diagnoza
naprawa
gotowe
zakonczone
anulowane
```

Każda ważna zmiana statusu zapisuje wpis w encji `HistoriaStatusu` oraz generuje powiadomienie dla klienta.

Przykładowy proces:

```text
Klient dodaje zgłoszenie
→ system tworzy zlecenie o statusie "nowe"
→ mechanik przyjmuje zlecenie
→ status zmienia się na "w_realizacji"
→ mechanik dodaje diagnozę
→ status zmienia się na "diagnoza"
→ mechanik rejestruje zużytą część
→ status zmienia się na "naprawa"
→ mechanik dodaje raport naprawy
→ status zmienia się na "gotowe"
```

---

## Instalacja lokalna

### 1. Sklonowanie projektu

```bash
git clone <adres_repozytorium>
cd Service
```

### 2. Utworzenie środowiska wirtualnego

Na macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Na Windowsie:

```powershell
py -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

Jeżeli plik `requirements.txt` jest pusty lub nieaktualny, można odtworzyć zależności lokalnie:

```bash
pip install django psycopg2-binary
pip freeze > requirements.txt
```

---

## Konfiguracja PostgreSQL

Projekt korzysta z bazy PostgreSQL.

Przykładowa konfiguracja lokalna:

```text
DB_NAME: serwis_rowerowy
DB_USER: serwis_user
DB_PASSWORD: serwis123
DB_HOST: localhost
DB_PORT: 5432
```

### Utworzenie bazy i użytkownika

Wejdź do PostgreSQL jako użytkownik administracyjny, np.:

```bash
psql -U postgres
```

Następnie wykonaj:

```sql
CREATE USER serwis_user WITH PASSWORD 'serwis123';
CREATE DATABASE serwis_rowerowy OWNER serwis_user;
GRANT ALL PRIVILEGES ON DATABASE serwis_rowerowy TO serwis_user;
```

Po wejściu do bazy:

```sql
\c serwis_rowerowy
GRANT ALL ON SCHEMA public TO serwis_user;
ALTER SCHEMA public OWNER TO serwis_user;
```

Wyjście z konsoli PostgreSQL:

```sql
\q
```

---

## Migracje bazy danych

Po skonfigurowaniu bazy uruchom:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Utworzenie superusera Django

Superuser służy do logowania do technicznego panelu Django Admin:

```bash
python manage.py createsuperuser
```

Panel Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## Uruchomienie aplikacji

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

---

## Konta użytkowników

W projekcie występują dwa poziomy użytkowników:

### 1. Użytkownik Django

Znajduje się w sekcji:

```text
Uwierzytelnianie i autoryzacja → Użytkownicy
```

Służy do:

```text
logowania,
haseł,
sesji,
panelu Django Admin.
```

### 2. Użytkownik aplikacji

Znajduje się w modelu:

```text
MAINAPP → Użytkownicy
```

Służy do:

```text
roli użytkownika,
powiązania z rowerami,
powiązania ze zgłoszeniami,
powiązania ze zleceniami.
```

Warunek poprawnego działania ról:

```text
Django User username = MAINAPP Uzytkownik login
```

Przykład:

```text
Django username: jkowalski
MAINAPP login: jkowalski
Rola: klient
```

---

## Rejestracja klienta

Klient może samodzielnie utworzyć konto pod adresem:

```text
/rejestracja/
```

Formularz tworzy:

```text
konto Django do logowania,
użytkownika aplikacji z rolą klient.
```

Użytkownik rejestrujący się publicznie zawsze otrzymuje rolę:

```text
klient
```

Role pracowników i administratorów są nadawane przez administratora aplikacji.

---

## Panel administratora aplikacji

Panel administratora aplikacji jest dostępny pod adresem:

```text
/panel-admin/
```

Dostęp ma użytkownik, który:

```text
jest zalogowany,
ma konto Django,
ma odpowiadający rekord w MAINAPP Uzytkownik,
ma rolę admin.
```

Administrator aplikacji może dodawać nowych użytkowników przez:

```text
/panel-admin/uzytkownicy/dodaj/
```

Formularz tworzy jednocześnie:

```text
konto Django,
użytkownika aplikacji z wybraną rolą.
```

---

## Dane testowe

Przykładowe role użytkowników:

```text
Klient:
login: jkowalski

Mechanik:
login: pzielinski

Magazynier:
login: mnowak

Administrator aplikacji:
login: adminapp
```

Przykładowe dane do systemu:

```text
Typ roweru:
MTB, Szosowy, Gravel, Miejski

Kategorie części:
Hamulce, Napęd, Koła, Opony

Producent roweru:
Kross, Trek, Giant

Przykładowa część:
Klocki hamulcowe Shimano B05S
Stan magazynowy: 12
Stan minimalny: 3
Cena: 49.99
```

---

## Sprawdzenie działania

Po uruchomieniu aplikacji warto przetestować proces:

```text
1. Klient rejestruje konto.
2. Klient dodaje rower.
3. Klient dodaje zgłoszenie.
4. System automatycznie tworzy zlecenie serwisowe.
5. Klient otrzymuje powiadomienie.
6. Mechanik przyjmuje zlecenie.
7. Mechanik dodaje diagnozę.
8. Mechanik rejestruje zużytą część.
9. Stan magazynowy części zostaje zmniejszony.
10. Mechanik dodaje raport naprawy.
11. Status zlecenia zmienia się na gotowe.
12. Klient widzi historię statusów i powiadomienia.
13. Administrator dodaje płatność.
14. Klient widzi płatność.
```

---

## Przygotowanie do wdrożenia

Przed wrzuceniem projektu na GitHub lub serwer nie należy dodawać:

```text
venv/
.git/
db.sqlite3
__pycache__/
*.pyc
.env
staticfiles/
.DS_Store
__MACOSX/
```

Plik `.gitignore` powinien zawierać:

```text
venv/
__pycache__/
*.pyc
db.sqlite3
.env
.DS_Store
staticfiles/
__MACOSX/
```

Przed wdrożeniem należy również upewnić się, że `requirements.txt` nie jest pusty:

```bash
pip freeze > requirements.txt
```

---

## Uwagi dotyczące bezpieczeństwa

Hasła użytkowników są przechowywane przez wbudowany system Django Auth. Model `Uzytkownik` przechowuje rolę i dane biznesowe użytkownika, ale nie powinien przechowywać jawnego hasła użytkownika.

W projekcie pole `haslo` w modelu `Uzytkownik` pełni funkcję techniczną/historyczną, natomiast właściwe logowanie realizowane jest przez `auth.User`.

---

## Status projektu

Aktualny zakres projektu obejmuje:

```text
25 encji w modelu danych,
logowanie i wylogowanie,
publiczną rejestrację klienta,
role użytkowników,
panele dla ról,
formularze dla klientów, mechaników, magazynierów i admina,
historię statusów,
powiadomienia,
płatności,
zamówienia części,
walidację zużycia części,
estetyczny interfejs użytkownika.
```

Projekt jest przygotowany do dalszego rozszerzenia o:

```text
Docker,
wdrożenie na zewnętrzny serwer,
generowanie PDF,
wykresy,
testy automatyczne,
procedury/funkcje/triggery PostgreSQL.
```
