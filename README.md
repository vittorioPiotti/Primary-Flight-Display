# Primary-Flight-Display

Soluzione software Primary Flight Display

---

_La schermata è stata acquisita dal progetto realizzato._

<img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>



## Indice

1. [Funzionalità](#casi-duso)
2. [Riepilogo Tecnico](#riepilogo-tecnico)
3. [Crediti](#crediti)

---




## Funzionalità

_Le schermata sono state acquisite dal progetto realizzato._

| Viewfinder| Horizon| PitchLadder | Display| 
| ------------ | ------------ | ------------ | ------------ | 
| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Viewfinder.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Horizon.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/PitchLadder.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>| 
|1| 2 | 3 |  4 |


1. Mirino 
2. Orizzonte 
3. Scala del Pitch
4. Display funzionante

## Riepilogo Tecnico 

### Obbiettivo

Ricezione con una frequenza di 100 ms i dati in formato json dal server python.

Elaborazione dei dati di pitch e roll per la visualizzazione dei componenti grafici.


### Soluzione 


#### Mirino

Dato il centro del display crea il mirino come:
  - un mirino quadrato centrale
  - due ali specchiate dal centro



#### Orizzonte

Dati due punti qualsiasi agli estremi della larghezza del display crea l'orizzonte come:
  - uno sfondo di colore cielo tutto schermo
  - una linea di colore bianco tra questi punti per separare il cielo dalla terra
  - Un quadrilatero di colore terra con massima altezza nei punti dati e base compresa tra i due margini bassi del display


#### Scala del Pitch



| Viewfinder| Horizon| PitchLadder | Display| 
| ------------ | ------------ | ------------ | ------------ | 
| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/perpendicolare.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/parallele.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/retta.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/segmento.png" alt="Icona" width="200"/>| 
|1| 2 | 3 |  4 |


Dati i due punti estremi dell'orrizonte:
  - calcolo centro del segmento compreso
  - calcolo due punti equidistanti dal centro ed appartenenti all'orizzonte
  - trasla 






## Crediti

- Teammate One
- Teammate Two
- Teammate Three
- Vittorio Piotti


