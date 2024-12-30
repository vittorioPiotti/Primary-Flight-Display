# Primary-Flight-Display

Soluzione software Primary Flight Display


> [!NOTE]
> Progetto scolastico 🎓 · Ⅴ




---

_La schermata è stata acquisita dal progetto realizzato._

<img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>



## Indice

1. [Prodotto](#prodotto)
2. [Riepilogo Tecnico](#riepilogo-tecnico)
3. [Crediti](#crediti)
4. [Sviluppi Futuri](#sviluppi-futuri)
5. [Licenze](#licenze)

---




## Prodotto

### Funzionalità

_Le schermata sono state acquisite dal progetto realizzato._



| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Viewfinder.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Horizon.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/PitchLadder.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Display.png" alt="Icona" width="200"/>| 
| ------------ | ------------ | ------------ | ------------ | 
|1| 2 | 3 |  4 |

1. Mirino `Viewfinder.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/src/Viewfinder.py))
2. Orizzonte `Horizon.py`([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/src/Horizon.py))
3. Scala del Pitch `PitchLadder.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/src/PitchLadder.py))
4. PFD Display Aereo `display.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/display.py))

### Copyright

> [!TIP]
> Il software è open-source

## Riepilogo Tecnico 


### Obbiettivo

Ricezione con una frequenza di 100 ms i dati in formato json dal server python.

Elaborazione dei dati di pitch e roll per la visualizzazione dei componenti grafici.


## Indice

1. [Soluzione](#soluzione)
2. [Tecnologie](#tecnologie)
3. [Note sul Codice](#note-sul-codice)
4. [Riferimenti Matematici](#riferimenti-matematici)
5. [Testing](#testing)
6. [Distribuzione Locale](#distribuzione-locale)
7. [Albero di Path](#albero-di-path)
---



### Soluzione 

#### Orizzonte



| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/schermo.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/orizzonte.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/terra.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Horizon.png" alt="Icona" width="200"/>|
| ------------ | ------------ | ------------ | ------------ | 
|1| 2 | 3 | 4 |

Dati due punti qualsiasi agli estremi della larghezza del display crea l'orizzonte come:
  1. Display quadrilatero di dimensione variabile
  2. Orizzonte come segmento tra i punti degli estremi del display
  3. Terra come quadrilatero compreso tra la base e l'orizzonte del display
  4. Componente Realizzato


#### Scala del Pitch


| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/perpendicolare.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/parallele.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/retta.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/PitchLadder.png" alt="Icona" width="200"/>| 
| ------------ | ------------ | ------------ | ------------ | 
|1| 2 | 3 |  4 |


1. Data la retta dell'orizzonte ed il centro del display si calcola la retta passante per il centro e perpendicolare all'orizzonte
2. Data la retta dell'orizzonte e la retta ad esso perpendicolare si determina il punto di intersezione tra le parallele dell'orizzonte e la perpendicolare all'orizzonte
3. Date le rette parallele ed i punti di intersezione con la perpendicolare si calcolano per ciascuno 2 punti equidistanti dal punto di intersezione
4. Componente Realizzato

### Tecnologie

Librerie, linguaggi e codice
  - Python v.3.12 ([link](https://www.python.org/doc/versions/))
  - TKinter v.8.6 ([link](https://www.tcl.tk/software/tcltk/8.6.html))
  - **Separazione dei compiti** per i componenti grafici in **classi autonome** garendo **la scalabilità e la facile manutenzione del codice.**
    
Comunicazione con server Python:
  -  Connessione alla porta dell'ip del server
  -  Comunicazione tramite socket
  -  Architettura Client-Server

### Note sul Codice

  1. Il codice è stato sviluppato in modo **compartimentato e modulare**.
  2. È stata garantita una corretta **separazione dei compiti**
  3. Sono stati sviluppati i **componenti grafici in classi autonome**
  4. Il codice ha quindi la qualità di essere **scalabile e facile da mantenere**



### Riferimenti Matematici



| Formula | Nome | Descrizione | 
| ------------ | ------------ | ------------ |
| $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$ | Equazione parametrica della retta |Calcola l’equazione delle rette dei segmenti | 
| $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ | Distanza euclidea tra due punti in un piano cartesiano |Calcola la lunghezza del segmento che collega due punti | 
| $y = y_0 + m(x - x_0)$ | Equazione del fascio di rette passante per un punto |Calcola l’equazione della retta dell’orizzonte | 








### Testing




> [!NOTE]
> Sono stati effettuati **Test Unitari** e **Test di Itergrazione** che hanno dato **esito positivo**
> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Viewfinder.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/Horizon.png" alt="Icona" width="200"/> | <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/PitchLadder.png" alt="Icona" width="200"/>| <img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/calcoli.png" alt="Icona" width="200"/>|
> | ------------ | ------------ | ------------ | ------------ | 
> |1| 2 | 3 | 4 |
> 
> 1. Mirino `Test_Viewfinder.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/test/Test_Viewfinder.py))
> 2. Orizzonte `Test_Horizon.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/test/Test_Horizon.py))
> 3. Scala del Pitch `Test_PitchLadder.py`  ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/test/Test_PitchLadder.py))
> 4. Calcoli `Test_Calc.py` ([link](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/source/test/Test_Calc.py))



> [!WARNING]
> MacOS ([video](https://drive.google.com/file/d/1O2NUyQX6dreFDlOx4WhHrVpao1NMTTvo/view))
> Tutti i test hanno dato **esito positivo** garantendo la **stabiità del software** solo se il **coefficiente è angolare valido**

> [!WARNING]
> Rivedere ed ottimizzare la logica dei componenti grafici per visualizzare il `PitchLadder.py`


> [!CAUTION]
> `Fatal Error` se il valore del **coefficiente angolare non valido** in quanto non è stato implementato **nessun controllo per gestire questo caso**




### Distribuzione Locale

1. Configura `Python v.3.12` ([link](https://www.python.org/doc/versions/))
2. Configura ambiente virtuale:
   
    2.1. Crea ambiente virtuale

          -m venv myenv

    2.2. attiva ambiente virtuale Mac:

          source myenv/bin/activate
   
    2.3. attiva ambiente virtuale Windows:
    
          .\myenv\Scripts\Activate

3. scarica `tkinter v.8.6` ([link](https://www.tcl.tk/software/tcltk/8.6.html))  in ambiente virtuale:

          pip install tk

3. Caricare i file sorgenti eventualmente sostituendo quelli già presenti


### Albero di Path

```bash
$ tree
.
├── src
│   ├── Calc.py
│   ├── Horizon.py
│   ├── PitchLadder.py
│   └── Viewfinder.py
├── test
│   ├── Test_Calc.py
│   ├── Test_Horizon.py
│   ├── Test_PitchLadder.py
│   └── Test_Viewfinder.py
├── client.py
├── server.py
└── display.py

```






## Crediti

- [Diego Ciucaloni](https://github.com/Diego-ciuck)
- [Luca Niccià](https://github.com/lucaniccia)
- [Matteo Fabbioni](https://github.com/MatteoFabbioni)
- [Vittorio Piotti](https://github.com/vittorioPiotti)

## Sviluppi Futuri


### Scala dello Yaw

<img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/yaw.png" alt="Icona" width="200"/>

### Scala del Roll

<img src="https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/project/screenshots/roll.png" alt="Icona" width="200"/>


## Licenze


### Primary Flight Display

**Copyright** 2024 Vittorio Piotti, Diego Ciucaloni, Matteo Fabbioni, Luca Niccià

**Version** [v1.0.0](https://github.com/vittorioPiotti/Primary-Flight-Display/releases/tag/1.0.0)

**License** [GPL-3.0](https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/LICENSE.md)

---

### TKinter

**Copyright** Python Software Foundation

**Version** [v.8.6](https://www.tcl.tk/software/tcltk/8.6.html)

**License** [PSF v2](https://docs.python.org/3/license.html)








