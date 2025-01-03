Jest to projekt semestralny na zaliczenie przedmiotu "Wstęp do programowania" mgr Grzegorza Madejskiego.
Fabiański Hubert, informatyka praktyczna I rok, grupa IV, 295853.

Jest to projekt zawierający grafową bazę danych, która przetrzymuje wszystkie możliwe numery telefonów 9-cyfrowych,
czyli od 000 000 000 do 999 999 999, wraz z przypisanymi do nich losowo cenami. Struktura danych pozwala na bardzo
szybkie odzyskanie danych nt. danego numeru telefonu.

Repozytorium wymaga do działania conajmniej 24gb wolnego miejsca na dysku, oraz instalacji numpy, psutil za pomocą pip:
pip install numpy
pip install psutil

Aby wygenerować dummy data należy najpierw uruchomić skrypt generate.py znajdujący się w folderze database.
Generowanie danych można przerwać i dokończyć kiedy indziej, następnie do testowania odzyskiwania danych należy
użyć uruchomić skrypt main.py, który znajduje się w folderze głównym.
