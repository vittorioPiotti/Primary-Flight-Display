# Importa il modulo tkinter per la creazione di interfacce grafiche
import tkinter as tk
# Importa il modulo sys per la gestione del percorso dei moduli
import sys
# Importa il modulo os per la gestione dei percorsi dei file
import os

# Aggiunge il percorso dei moduli src al percorso di ricerca dei moduli
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importa la classe Horizon dal modulo Horizon
from Horizon import Horizon

# Definisci le dimensioni della finestra
WIDTH = 600
HEIGHT = 600

# Definisci le coordinate Y di inizio e fine per la terra e la linea dell'orizzonte
YSTART = 50
YEND = -50

# Classe di test della classe Horizon per la visualizzazione dell'orizzonte del display di volo primario
class Test_Horizon(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width  # Larghezza della finestra
        self.height = height  # Altezza della finestra
        self.geometry(f"{width}x{height}")  # Imposta le dimensioni della finestra
        self.title("Test Horizon")  # Imposta il titolo della finestra
        self.canvas = tk.Canvas(self, width=width, height=height)  # Crea un widget Canvas
        self.canvas.pack()  # Aggiunge il Canvas alla finestra
        # Crea un'istanza della classe Horizon e aggiorna le coordinate della terra e della linea dell'orizzonte
        self.horizon = Horizon(width, height, self.canvas)
        self.horizon.newCoords(0, 1, self.horizon.earthCoords, YSTART, YEND, self.horizon.earthPolygon, True)
        self.horizon.newCoords(0, 1, self.horizon.lineCoords, YSTART, YEND, self.horizon.line, True)

# Avvia il test se il file viene eseguito come script principale
if __name__ == "__main__":
    testHorizon = Test_Horizon(WIDTH, HEIGHT)
    testHorizon.mainloop() 
