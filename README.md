PROJEKT DJANGO

Struktura:
- serwis/ -> projekt Django
- app/    -> jedna aplikacja Django
- app/models.py -> modele
- app/views.py  -> widoki
- app/urls.py   -> adresy URL aplikacji
- app/templates/app/ -> szablony

Uruchomienie:
1. Aktywuj środowisko wirtualne
2. Zainstaluj Django, jeśli trzeba:
   pip install django
3. W folderze projektu wykonaj:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

Adresy:
- strona główna: http://127.0.0.1:8000/
- lista zgłoszeń: http://127.0.0.1:8000/zgloszenia/
- panel admina: http://127.0.0.1:8000/admin/

- Wszystkie modele są w jednym pliku models.py