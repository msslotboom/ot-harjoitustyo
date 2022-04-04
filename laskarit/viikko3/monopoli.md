### Monopoli

```mermaid
 classDiagram
    Pelilauta <|-- Ruutu
    class Pelilauta{
        ruutujen_maara
    }
    class Ruutu{
        id
        seuraava_id

    }
    class Noppa{
        määrä
    }
```