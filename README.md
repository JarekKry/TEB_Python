 # SimplePasswordManager

**Nazwa projektu**: SimplePasswordManager

**Wykonawca**: Jarek Krysztofiński

**Opis projektu**: Aplikacja ma na celu ułatwić  przechowywanie danych logowania w bezpieczny i uporządkowany sposób. Szyfrowanie jak i obsługa pliku bazy danych odbywa się przy użyciu własnych algorytmów opisanych dokładniej w [SimpleDB](Dokumentacja/SimpleDB.md) oraz [SimpleEncryption](Dokumentacja/SimpleEncryption.md). Interfejs graficzny aplikacji został oparty o bibliotekę [PyQt5](https://pypi.org/project/PyQt5) 

**GUI programu**:

![Interface](/Dokumentacja/Interface.png)

**Napotkane problemy algorytmiczne**:
* **GUI w PyQt5**: Samo zaprojektowanie GUI przebiegło dość gładko ale implementacja jego funkcjonalności zabrała mi dość sporo czasu
* **Czyszczenie schowka**: Funkcja czyszczenia schowka po 10 sekundach od skopiowania do niego hasła okazała się dość problematyczna i wymagająca zapoznania się z funkcjonnowaniem wątków w PyQt5
* **Szyfrowanie**: O ile algorytm szyfrujący ( [SimpleDB](Dokumentacja/SimpleDB.md) ) zdaje się działać prawidłowo, brak mi wiedzy z zakresu kryptografi by ocenić jego skuteczność :(

**Schemat blokowy procesu wczytywania bazy danych**:

![Interface](/Dokumentacja/Schematy%20blokowe/Wczytywanie%20bazy%20danych.svg)