import tkinter as tk
import math

import sys
import os

# Aggiusta il percorso per trovare i moduli src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.Viewfinder import Viewfinder
from src.Horizon import Horizon
from src.PitchLadder import PitchLadder
from src.Calc import Calc


# Classe per la visualizzazione dei componenti del display di volo primario
class Display:
    def __init__(self, width, height):
        self.width = width  # Larghezza finestra
        self.height = height  # Altezza finestra
        self.xFs = 0  # Larghezza minima
        self.xNd = width  # Larghezza massima
        self.calc = Calc()  # Istanza della classe Calc
        self.finestra = tk.Tk()  # Crea la finestra principale dell'applicazione
        self.finestra.geometry(f"{width}x{height}")  # Imposta le dimensioni della finestra
        self.finestra.title("Primary Flight Display")  # Imposta il titolo della finestra
        self.canvas = tk.Canvas(self.finestra, width=width, height=height)  # Crea un widget Canvas
        self.canvas.pack()  # Aggiunge il Canvas alla finestra
        self.horizon = Horizon(width, height, self.canvas)  # Crea un'istanza della classe Horizon
        self.pitchLadder = PitchLadder(width, height, self.canvas, self.calc)  # Crea un'istanza della classe PitchLadder
        self.viewfinder = Viewfinder(width, height, self.canvas)  # Crea un'istanza della classe Viewfinder

    def update_components(self, roll, pitch):
        # Converti pitch e roll in radianti
        radPitch = math.radians(pitch)
        radRoll = math.radians(roll)
        sinPitch = math.sin(radPitch)
        tanRoll = math.tan(radRoll)
        
        # Calcola le coordinate per il centro della linea dell'orizzonte
        xm = self.width / 2
        ym = (self.height) - ((sinPitch + 1) * self.height)
        
        # Calcola le coordinate della linea dell'orizzonte
        yFs = ym + (tanRoll * (-1)) * (self.xFs - xm)
        yNd = ym + (tanRoll * (-1)) * (self.xNd - xm)
        self.yFs, self.yNd = yFs, yNd  # Memorizza yFs e yNd come variabili di classe
        
        
        # Disegna tutte le linee della scala di beccheggio
        self.pitchLadder.draw_all_lines(pitch, roll, self.xFs, self.xNd, self.horizon.lineCoords)
        
        # Aggiorna le coordinate dell'orizzonte
        self.horizon.newCoords(0, 1, self.horizon.earthCoords, yFs, yNd, self.horizon.earthPolygon, True)
        self.horizon.newCoords(0, 1, self.horizon.lineCoords, yFs, yNd, self.horizon.line, True)


        

        
            

 