# Primary-Flight-Display

Soluzione software Primary Flight Display

---

_La schermata è stata acquisita dal progetto realizzato._

<img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>



## Indice

1. [Prodotto](#casi-duso)
2. [Riepilogo Tecnico](#riepilogo-tecnico)
3. [Crediti](#crediti)

---




## Prodotto

### Funzionalità

_Le schermata sono state acquisite dal progetto realizzato._

| Mirino| Orizzonte| Scala del Pitch | Display| 
| ------------ | ------------ | ------------ | ------------ | 
| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Viewfinder.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Horizon.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/PitchLadder.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>| 
|1| 2 | 3 |  4 |

1. Mirino 
2. Orizzonte 
3. Scala del Pitch
4. Display funzionante

### Copyright

> [!TIP]
> Il software è open-source

### Distribuzione Locale

1. Configura Python v.3.12
2. Configura ambiente virtuale:
    2.1. Crea ambiente virtuale

        -m venv myenv

   
    2.2 attiva ambiente virtuale:

   
     2.2.1     mac
    
                    -m venv myenv
   
       
      2.2.1     wind
    
                    -m venv myenv
   

3.scarica tkinter in ambiente virtuale:pip install tk

## Riepilogo Tecnico 

### Obbiettivo

Ricezione con una frequenza di 100 ms i dati in formato json dal server python.

Elaborazione dei dati di pitch e roll per la visualizzazione dei componenti grafici.


### Soluzione 

#### Orizzonte

| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/schermo.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/orizzonte.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/terra.png" alt="Icona" width="200"/>|
| ------------ | ------------ | ------------ | 
|1| 2 | 3 | 

Dati due punti qualsiasi agli estremi della larghezza del display crea l'orizzonte come:
  1. Display di dimensione variabile
  2. Orizzonte come segmento tra i punti degli estremi del display
  3. Terra come quadrilatero compreso tra la base e l'orizzonte del display


#### Scala del Pitch




| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/perpendicolare.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/parallele.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/retta.png" alt="Icona" width="200"/>|
| ------------ | ------------ | ------------ | 
|1| 2 | 3 | 

1. Data la retta dell'orizzonte ed il centro del display si calcola la retta passante per il centro e perpendicolare all'orizzonte
2. Data la retta dell'orizzonte e la retta ad esso perpendicolare si determina il punto di intersezione tra le parallele dell'orizzonte e la perpendicolare all'orizzonte
3. Date le rette parallele ed i punti di intersezione con la perpendicolare si calcolano per ciascuno 2 punti equidistanti dal punto di intersezione






## Crediti

- Teammate One
- Teammate Two
- Teammate Three
- Vittorio Piotti


