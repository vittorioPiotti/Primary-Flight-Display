# Importa il modulo sys per la gestione del percorso dei moduli
import sys
# Importa il modulo os per la gestione dei percorsi dei file
import os
# Importa il modulo tkinter per la creazione di interfacce grafiche
import tkinter as tk

# Aggiunge il percorso dei moduli src al percorso di ricerca dei moduli
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importa la classe Calc dal modulo Calc
from Calc import Calc

# Definisci le dimensioni della finestra
WIDTH = 600
HEIGHT = 600

# Classe per il test della classe Calc
class Test_Calc(tk.Tk):
    def __init__(self,width,height):
        super().__init__()
        self.title("Test Calc")  # Imposta il titolo della finestra
        self.calc = Calc()  # Crea un'istanza della classe Calc
        self.width = width  # Larghezza della finestra
        self.height = height  # Altezza della finestra
        self.geometry(f"{width}x{height}")  # Imposta le dimensioni della finestra
        self.create_widgets()  # Crea i widget
        self.run_tests()  # Esegue i test

    def create_widgets(self):
        # Crea un widget Text per visualizzare i risultati dei test
        self.text = tk.Text(self, wrap=tk.WORD, width=70, height=30)
        self.text.pack(pady=10)  # Aggiunge il widget alla finestra

    def run_tests(self):
        # Cancella il contenuto del widget Text
        self.text.delete(1.0, tk.END)
        # Definisci i parametri per i test
        m = 1.0
        cx, cy = 300, 300
        P1 = (100, 100)
        P2 = (200, 200)
        distanza = 50
        S = (100, 100)
        E = (200, 200)
        r1x, r1y = 0, 0
        r2x, r2y = 1, 1
        r3x, r3y = 0, 1
        r4x, r4y = 1, 0
        # Esegue i test e aggiorna il widget Text con i risultati
        self.log_method("intersezione_retta_circonferenza", f"m={m}, cx={cx}, cy={cy}", self.calc.intersezione_retta_circonferenza(m, cx, cy))
        self.log_method("lunghezza_segmento", f"P1={P1}, P2={P2}", self.calc.lunghezza_segmento(P1, P2))
        self.log_method("punti_equidistanti", f"P1={P1}, P2={P2}, distanza={distanza}", self.calc.punti_equidistanti(P1, P2, distanza))
        self.log_method("equazione_retta", f"S={S}, E={E}", Calc.equazione_retta(S, E))
        self.log_method("coefficiente_angolare", f"S={S}, E={E}", Calc.coefficiente_angolare(S, E))  # Correzione qui
        self.log_method("punto_intersezione", f"r1x={r1x}, r1y={r1y}, r2x={r2x}, r2y={r2y}, r3x={r3x}, r3y={r3y}, r4x={r4x}, r4y={r4y}", Calc.punto_intersezione(r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y))

    def log_method(self, method_name, params, result):
        # Aggiunge i risultati dei test al widget Text
        self.text.insert(tk.END, f"{method_name}\n")
        self.text.insert(tk.END, f"Parametri: {params}\n")
        self.text.insert(tk.END, f"Risultato: {result}\n\n")

# Avvia il test se il file viene eseguito come script principale
if __name__ == "__main__":
    testCalc = Test_Calc(WIDTH,HEIGHT)
    testCalc.mainloop()
