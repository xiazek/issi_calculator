# Zadanie na zaliczenie przedmiotu "Wybrane zagadnienia z inżynierii oprogramowania"
[![lint and test](https://github.com/xiazek/issi_calculator/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/xiazek/issi_calculator/actions/workflows/lint_and_test.yml)

 - [calculator.py](calculator.py)
 - [test_calculator.py](test_calculator.py)

## Zależności developerskie i testowanie

Brak zależności uruchomieniowych requirements.txt.


zainstaluj zależności developerskie i testowe
```bash
python3 -m venv .venv
activate .venv/bin/activate
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
### Raport z pokrycia testami coverage

 - [.github/workflows/lint_and_test.yml](Github action) jest skonfigurowane aby sprawdzać coverage
 - Raport jest wysyłany jako artefakt i dostępny z [poziomu Actions](https://github.com/xiazek/issi_calculator/actions/workflows/lint_and_test.yml) w zakładce Artefacts każdego "builda".
 - dodłem też ręcznie raport do [htmlcov/index.html](htmlcov/index.html)
 

## Uruchomienie

```bash
python3 calculator.py 2 3
```



