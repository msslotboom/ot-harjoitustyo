# Ohjelmistotekniikka
Course for the **University of Helsinki**, 2022 
## Peli
Pelissä voi liikuttaa hahmoa. Pelin tarkoitus on päästä maaliin vihollisten ja esteiden ohi.

[Vaatimusmäärittely](https://github.com/msslotboom/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/msslotboom/ot-harjoitustyo/blob/master/harjoitustyo/changelog.md)

[Tuntikirjanpito](https://github.com/msslotboom/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/msslotboom/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Ohje

Asenna pelin riippuvuudet komennolla
```bash
poetry install
```
Pelaa peliä komennolla:
```bash
poetry run invoke start
```
Testit tekee komennolla:
```bash
poetry run invoke test
```
Coverage reportin tekee komennolla:
```bash
poetry run invoke coverage-report
```
Html tiedosto syntyy kansioon /htmlcov

Pylintin antamat pisteet näkee komennolla:
```bash
poetry run invoke lint
```
