# Tiff-converter
Tiff->pdf converter - both from path and from excel file

Prosty konwerter plików '.tif' i '.tiff' do '.pdf', napisany w Pythonie. Program obsługuje zarówno foldery z obrazami, jak i pliki '.xlsx' lub '.csv' zawierające listę ścieżek do folderów. Pliki '.pdf' zapisywane są w tym samym katalogu, w którym znajduje się plik '.tif'/'.tiff'.

---

## Wymagania

- Python 3.8 lub nowszy
- Zainstalowane biblioteki:
  - 'pandas'
  - 'openpyxl'
  - 'Pillow'

Można je zainstalować z poziomu terminala poleceniem:

pip install -r requirements.txt


## Jak używać

### Przetwarzanie folderu z plikami '.tif' / '.tiff':

python tif_to_pdf.py "C:\ścieżka\do\katalogu"

### Przetwarzanie pliku Excel/CSV z listą folderów:

Plik musi zawierać kolumnę 'path' ze ścieżkami do folderów zawierających pliki '.tif'.

python tif_to_pdf.py "C:\ścieżka\do\plik.xlsx"

Działa również dla plików '.csv'.


## Przykład pliku wejściowego (.xlsx lub .csv)

| path                          |
|------------------------------|
| C:\obrazy\skanowane_2024     |
| D:\archiwum\umowy_tif        |


## Funkcje

- Obsługa formatów '.tif' i '.tiff'
- Obsługa folderów, plików '.xlsx' i '.csv'
- Automatyczne sprawdzanie poprawności ścieżek
- Licznik przetworzonych plików
- Prosta obsługa z wiersza poleceń


##  Struktura projektu

tif-to-pdf/
├── tif_to_pdf.py
├── requirements.txt
└── README.md


## Autor

Projekt stworzony przez KayaKazuyoshi w 2025 roku.
