## Käyttöohje

### Asennus
Asenna pelin riippuvuudet komennolla
```bash
poetry install
```
Pelaa peliä komennolla:
```bash
poetry run invoke start
```

### Pelaaminen

Pelin tarkoitus on ohjata robotti maaliin. Robotin ohjaus onnistuu liikkumalla nuolilla vasemalle ja oikealle. Robotti voi hypätä panamalla nuolta ylös. Robotti voi hypätä toisen kerran ilmassa ("double jump").

![robotti](https://github.com/msslotboom/ot-harjoitustyo/blob/master/harjoitustyo/src/assets/robot.png) ![maali](https://github.com/msslotboom/ot-harjoitustyo/blob/master/harjoitustyo/src/assets/ovi.png)

Pelissä on esteitä, joiden läpi ei voi mennä. Näiden päälle voi hypätä. Esteet ovat mustan värisiä.

### Tasojen rakentaminen

Tasojen rakentaminen on vielä erittäin alkuvaiheessa. Taso luetaan .csv tiedostosta. Tällä hetkellä vain esteet voidaan lukea sieltä.

```
Barrier, levelwidth, barrierwidth, levelwidth/2, levelheight-barrierwidth/2
```
Tämä rivi tekee esteen pelinäyton alapuolelle. Ensimmäinen osa "Barrier" kertoo ohjelmalle että kyseessä on este. Toka ja kolmas osa kertovat esteen leveyden ja korkeuden. Neljäs ja viides osa kertovat esteen koordinaatit. Koordinaatit kertovat esteen keskipisteen koordinaatit.

Tiedostosssa voi olla kolme tekstimuotoista pituutta;
- levelwidth: tason leveys
- levelheight: tason korkeus
- barrierwidth: esteen leveys. Tämä on tällä hetkellä kovakoodattu mutta pitää tulevaisuudessa myös määritellä .csv tiedostossa
