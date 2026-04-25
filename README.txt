PROJEKT DJANGO - SERWIS ROWEROWY

Struktura zgodna z wytycznymi:
- project urls.py przekierowuje do mainapp.urls
- mainapp posiada własny urls.py
- views.py zawiera widok home
- szablony są w mainapp/templates
- home.html rozszerza base.html

URUCHOMIENIE:
1. Wejdź do katalogu z plikiem manage.py
2. Utwórz i aktywuj środowisko wirtualne:
   python3 -m venv venv
   source venv/bin/activate
3. Zainstaluj Django:
   pip install django
4. Wykonaj migracje:
   python manage.py makemigrations
   python manage.py migrate
5. Uruchom serwer:
   python manage.py runserver

ADRES:
http://127.0.0.1:8000/

UWAGA:
Plik models.py opisuje strukturę danych, a SQLite (db.sqlite3) jest faktyczną bazą danych tworzoną po migrate.
