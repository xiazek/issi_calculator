# Zadanie na zaliczenie przedmiotu "Wybrane zagadnienia z inżynierii oprogramowania"

 - [calculator.py](calculator.py)
 - [test_calculator.py](test_calculator.py)

## Zależności developerskie i testowanie

Brak zależności uruchomieniowych requirements.txt.

zainstaluj zależności developerskie i testowe
```bash
pip3 install -r requirements-dev.txt
```

Uruchom testy jednostkowe
```bash
pytest -v
```
Po zmianach upewnij się, że pokrycie kodu jest 100% 
```bash
coverage run -m pytest
```
### Raport z pokrycia testami

 - [coverage.txt](coverage.txt)


## Uruchomienie

```bash
python3 calculator.py 2 3
```



