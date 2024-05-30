import tkinter as tk
import sys
import os

# Aggiungi il percorso per trovare i moduli src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importa il modulo Calc e PitchLadder
from Calc import Calc
from PitchLadder import PitchLadder

WIDTH = 600
HEIGHT = 600

# Definisci le costanti per la posizione iniziale e finale della scala di beccheggio
XSTART = 250
XEND = 350

# Definisci gli angoli di beccheggio e rollio in gradi
PITCH = 0
ROLL = 1

# Classe di test della classe PitchLadder per la visualizzazione della scala del pitch del display di volo primario
class Test_PitchLadder(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width  # Larghezza della finestra
        self.height = height  # Altezza della finestra
        self.lineCoords = [  # Coordinare della linea orizzontale
            (0, height / 2),  # Punto iniziale della linea
            (width, height / 2)  # Punto finale della linea
        ]  
        self.calc = Calc()  # Istanzia la classe Calc per i calcoli
        self.geometry(f"{width}x{height}")  # Imposta le dimensioni della finestra
        self.title("Test PitchLadder")  # Imposta il titolo della finestra
        self.configure(bg='black')  # Imposta lo sfondo della finestra in nero
        self.canvas = tk.Canvas(self, width=width, height=height, bg='black')  # Crea un widget Canvas con sfondo nero
        self.canvas.pack()  # Aggiunge il Canvas alla finestra
        # Crea un'istanza della classe PitchLadder e disegna le linee di beccheggio sulla canvas
        self.pitchLadder = PitchLadder(width, height, self.canvas, self.calc)
        self.pitchLadder.draw_all_lines(PITCH, ROLL, XSTART, XEND, self.lineCoords)

# Crea un'istanza della classe Test_Horizon e avvia la finestra principale
if __name__ == "__main__":
    testPitchladder = Test_PitchLadder(WIDTH, HEIGHT)
    testPitchladder.mainloop() 
