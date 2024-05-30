import tkinter as tk
import sys
import os

# Aggiungi il percorso per trovare i moduli src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importa il modulo Viewfinder
from Viewfinder import Viewfinder

WIDTH = 600
HEIGHT = 600

# Classe di test della classe Viewfinder per la visualizzazione del mirino del display di volo primario
class Test_Viewfinder(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width  # Larghezza della finestra
        self.height = height  # Altezza della finestra
        self.geometry(f"{width}x{height}")  # Imposta le dimensioni della finestra
        self.title("Test Viewfinder")  # Imposta il titolo della finestra
        self.canvas = tk.Canvas(self, width=width, height=height)  # Crea un widget Canvas
        self.canvas.pack()  # Aggiunge il Canvas alla finestra
        self.viewfinder = Viewfinder(width, height, self.canvas)  # Crea un'istanza della classe Viewfinder

# Crea un'istanza della classe Test_Viewfinder e avvia la finestra principale
if __name__ == "__main__":
    testViewfinder = Test_Viewfinder(WIDTH, HEIGHT)
    testViewfinder.mainloop()
