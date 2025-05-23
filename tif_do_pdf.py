from pathlib import Path
import argparse
import pandas as pd
from PIL import Image

#Sprawdzenie poprawności wprowadzonej ścieżki
def path_exists(path):

    try:
        path = Path(path)
        if path.exists():
            return path
        else:
            print(f'Podana ścieżka: {path} nie prowadzi do istniejącego pliku.')
            return path_exists(input('Podaj poprawną ścieżkę: '))
    except OSError as e:
        print(f'Podczas przetwarzania ścieżki: {path} wystąpił nieoczekiwany błąd: {e}.')
        return path_exists(input('Podaj poprawną ścieżkę: '))

#Konwerter plików tif(f) do pdf
def tif_converter(path):

    path_pdf = path.with_suffix('.pdf')
    try:
        image = Image.open(path)
        image.save(path_pdf, save_all=True)
        print(f'Zapisano plik: {path}')
    except Exception as e:
        print(f'Podczas przetwarzania pliku {path_pdf} wystąpił błąd: {e}.')

#Funkcja do obsługi plików Excela
def paths_from_excel(df):
    for row in df.itertuples():
        path_from_df = Path(str(row.path))
        path_from_df = path_exists(path_from_df)

        tif_files = []
        for ext in ('*.tif', '*.tiff'):
            tif_files.extend(path_from_df.rglob(ext))

        total = len(tif_files) #Licznik plików tiff pozostających do przetworzenia

        for i, file in enumerate(tif_files, start=1):
            file_path = path_from_df / file
            tif_converter(file_path)
            print(f'Przetworzyłem {i}/{total} plików tif z katalogu {path_from_df}.')

#Metafunkcja obsługująca pozostałe
def opener(path):

    path = path_exists(path)
    path_ext = path.suffix

    #Przypadek 1: otwieranie ścieżek z pliku excela
    if path_ext == '.xlsx':
        df = pd.read_excel(path)
        paths_from_excel(df)

    elif path_ext == '.csv':
        df = pd.read_csv(path, encoding='utf-8')
        paths_from_excel(df)

    #Przypadek 2: otwieranie plików z katalogu
    elif path.is_dir():

        tif_files = []
        for ext in ('*.tif', '*.tiff'):
            tif_files.extend(path.rglob(ext))

        total = len(tif_files) #Licznik plików tiff pozostających do przetworzenia

        for i, file in enumerate(tif_files, start=1):
            file_path = path / file
            tif_converter(file_path)
            print(f'Przetworzyłem {i}/{total} plików z katalogu {path}.')
    else:
        raise Exception(f'Wystąpił błąd podczas wykonywania ścieżki: {path}.')

#Funkcja umożliwiająca wczytanie skryptu bezpośrednio z cmd
def main():
    parser = argparse.ArgumentParser('Zamiana plików z rozszerzeniem tif na rozszerzenie pdf.')
    parser.add_argument('input_link', help='Ścieżka wejściowa')
    args = parser.parse_args()

    opener(args.input_link)

if __name__ == '__main__':
    main()