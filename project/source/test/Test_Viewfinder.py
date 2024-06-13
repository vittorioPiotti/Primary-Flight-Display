"""
Primary Flight Display v1.0.0 (https://github.com/vittorioPiotti/Primary-Flight-Display/releases/tag/1.0.0)
Copyright 2024 Vittorio Piotti, Diego Ciucaloni, Matteo Fabbioni, Luca Niccià
Licensed under GPL-3.0 (https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/LICENSE.md)
"""

"""
TKinter 8.6
-----------
TKinter is distributed as part of the Python Standard Library.

Python Software Foundation License Version 2

For the full license text, please visit:
https://docs.python.org/3/license.html
"""


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
