### Monopoli

```mermaid
 classDiagram
    Ruutu "*" <-- "1" Pelilauta
    Nappula <|-- Pelaaja
    Nappula <|-- Pelilauta
    Ruutu <|-- Nappula
    class Pelilauta{
        ruutujen_maara
    }
    class Ruutu{
        id
        seuraava_id
    }
    class Pelaaja{
        nimi
        nappula_id
    }
    class Nappula{
        pelaaja_id
        ruutu_id
    }
    class Noppa{
        määrä
    }
```