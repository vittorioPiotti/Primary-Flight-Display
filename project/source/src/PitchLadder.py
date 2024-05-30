import tkinter as tk
import math

class PitchLadder:
    """
    Classe per creare una scala di inclinazione del pitch per il display di volo primario (PFD).

    Attributi:
        width (int): La larghezza della tela della scala di inclinazione del pitch.
        height (int): L'altezza della tela della scala di inclinazione del pitch.
        canvas (tk.Canvas): La tela su cui è disegnata la scala di inclinazione del pitch.
        lines (list): Linee di 10°, 20° e 30° sopra l'orizzonte.
        half_lines (list): Linee di 5°, 15° e 25° sopra l'orizzonte.
        quarter_lines (list): Linee di 2.5°, 7.5°, 12.5°, 17.5°, 22.5° e 27.5° sopra l'orizzonte.
        labels (list): Etichette dei gradi 10, 20 e 30 per le linee sopra l'orizzonte (una a destra e una a sinistra della linea).
        calc (oggetto): Oggetto che contiene funzioni di calcolo per le equazioni delle rette e intersezioni.
    """

    def __init__(self, width, height, canvas, calc):
        """
        Inizializza la scala di inclinazione del pitch.

        Argomenti:
            width (int): La larghezza della tela della scala di inclinazione del pitch.
            height (int): L'altezza della tela della scala di inclinazione del pitch.
            canvas (tk.Canvas): La tela su cui è disegnata la scala di inclinazione del pitch.
            calc (oggetto): Oggetto che contiene funzioni di calcolo per le equazioni delle rette e intersezioni.
        """
        self.width = width
        self.height = height
        self.canvas = canvas
        self.lines = []  # Linee di 10°, 20° e 30° sopra l'orizzonte
        self.half_lines = []  # Linee di 5°, 15° e 25° sopra l'orizzonte
        self.quarter_lines = []  # Linee di 2.5°, 7.5°, 12.5°, 17.5°, 22.5° e 27.5° sopra l'orizzonte
        self.labels = []  # Scritta dei gradi 10, 20 e 30 per le linee sopra l'orizzonte (una a destra della linea e una a sinistra)
        self.init_all_lines()
        self.calc = calc

    def init_lines(self):
        """
        Inizializza le linee principali della scala di inclinazione del pitch.
        """
        for _ in range(6):
            line = self.canvas.create_line(0, 0, 0, 0, fill='white', width=3)
            self.lines.append(line)

    def init_half_lines(self):
        """
        Inizializza le linee intermedie della scala di inclinazione del pitch.
        """
        for _ in range(6):
            line = self.canvas.create_line(0, 0, 0, 0, fill='white', width=3)
            self.half_lines.append(line)

    def init_quarter_lines(self):
        """
        Inizializza le linee minori della scala di inclinazione del pitch.
        """
        for _ in range(12):
            line = self.canvas.create_line(0, 0, 0, 0, fill='white', width=3)
            self.quarter_lines.append(line)

    def init_labels(self):
        """
        Inizializza le etichette dei gradi per le linee principali.
        """
        for i in range(12):
            c = (i % 3 + 1) * 10
            if c > 30:
                c = c - 30
            label = self.canvas.create_text(0, 0, text=c, fill="white", font=("Arial", 20))
            self.labels.append(label)

    def draw_lines(self, pitch, roll, xFs, xNd, lineCoords):
        """
        Disegna le linee principali sulla tela.

        Argomenti:
            pitch (float): L'inclinazione del pitch attuale.
            roll (float): Il rollio attuale.
            xFs (float): La coordinata x del punto iniziale.
            xNd (float): La coordinata x del punto finale.
            lineCoords (list): Coordinata delle linee sulla scala di inclinazione del pitch.
        """
        angles = [10, 20, 30, -10, -20, -30]
        for angle in angles:
            i = angles.index(angle)
            self.draw_line(angle, self.lines[i], self.labels[i], self.labels[6 + i], pitch, roll, xFs, xNd, lineCoords)

    def draw_half_lines(self, pitch, roll, xFs, xNd, lineCoords):
        """
        Disegna le linee intermedie sulla tela.

        Argomenti:
            pitch (float): L'inclinazione del pitch attuale.
            roll (float): Il rollio attuale.
            xFs (float): La coordinata x del punto iniziale.
            xNd (float): La coordinata x del punto finale.
            lineCoords (list): Coordinata delle linee sulla scala di inclinazione del pitch.
        """
        angles = [5, 15, 25, -5, -15, -25]
        for angle in angles:
            i = angles.index(angle)
            self.draw_line(angle, self.half_lines[i], "", "", pitch, roll, xFs, xNd, lineCoords)

    def draw_quarter_lines(self, pitch, roll, xFs, xNd, lineCoords):
        """
        Disegna le linee minori sulla tela.

        Argomenti:
            pitch (float): L'inclinazione del pitch attuale.
            roll (float): Il rollio attuale.
            xFs (float): La coordinata x del punto iniziale.
            xNd (float): La coordinata x del punto finale.
            lineCoords (list): Coordinata delle linee sulla scala di inclinazione del pitch.
        """
        angles = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5, -2.5, -7.5, -12.5, -17.5, -22.5, -27.5]
        for angle in angles:
            i = angles.index(angle)
            self.draw_line(angle, self.quarter_lines[i], "", "", pitch, roll, xFs, xNd, lineCoords)

    def init_all_lines(self):
        """
        Inizializza tutte le linee della scala di inclinazione del pitch.
        """
        self.init_lines()
        self.init_half_lines()
        self.init_quarter_lines()
        self.init_labels()

    def draw_all_lines(self, pitch, roll, xFs, xNd, lineCoords):
        """
        Disegna tutte le linee della scala di inclinazione del pitch sulla tela.

        Argomenti:
            pitch (float): L'inclinazione del pitch attuale.
            roll (float): Il rollio attuale.
            xFs (float): La coordinata x del punto iniziale.
            xNd (float): La coordinata x del punto finale.
            lineCoords (list): Coordinata delle linee sulla scala di inclinazione del pitch.
        """
        self.draw_lines(pitch, roll, xFs, xNd, lineCoords)
        self.draw_half_lines(pitch, roll, xFs, xNd, lineCoords)
        self.draw_quarter_lines(pitch, roll, xFs, xNd, lineCoords)

    def draw_line(self, angle_deg, line_element, label_element_left, label_element_right, pitch, roll, xFs, xNd, lineCoords):
        """
        Disegna una singola linea sulla tela.

        Argomenti:
            angle_deg (float): L'angolo della linea da disegnare in gradi.
            line_element (tk.Line): L'elemento della linea da disegnare.
            label_element_left (tk.Text): L'elemento dell'etichetta a sinistra.
            label_element_right (tk.Text): L'elemento dell'etichetta a destra.
            pitch (float): L'inclinazione del pitch attuale.
            roll (float): Il rollio attuale.
            xFs (float): La coordinata x del punto iniziale.
            xNd (float): La coordinata x del punto finale.
            lineCoords (list): Coordinata delle linee sulla scala di inclinazione del pitch.
        """
        rad_angle = math.radians(angle_deg)
        xm = self.width / 2
        ym = self.height - ((math.sin(math.radians(pitch)) + 1) * self.height)
        yFs = ym + (math.tan(math.radians(roll)) * (-1)) * (xFs - xm)
        yNd = ym + (math.tan(math.radians(roll)) * (-1)) * (xNd - xm)
        if xNd - xFs != 0:
            slope = (yNd - yFs) / (xNd - xFs)
            perp_slope = -1 / slope if slope != 0 else float('inf')
        else:
            perp_slope = 0
        xm, ym = self.width / 2, self.height / 2
        if perp_slope == float('inf'):
            x1, y1 = xm, self.height
            x2, y2 = xm, 0
        else:
            x1, y1 = self.width, ym - perp_slope * (self.width - xm)
            x2, y2 = 0, ym + perp_slope * xm
        S = (x1, y1)
        E = (x2, y2)
        m = self.calc.equazione_retta(S, E)
        distanza = 0
        if m != 0:
            cx, cy = self.width / 2, self.height / 2
            if angle_deg in [10, 20, 30, -10, -20, -30]: 
                distanza = 125
            if angle_deg in [5, 15, 25, -5, -15, -25]: 
                distanza = 75
            if angle_deg in [2.5, 7.5, 12.5, 17.5, 22.5, 27.5, -2.5, -7.5, -12.5, -17.5, -22.5, -27.5]: 
                distanza = 35
            r1x, r1y = lineCoords[0][0], self.width - ((self.width / 2) + yFs + self.width * math.sin(rad_angle))
            r2x, r2y = lineCoords[1][0], self.width - ((self.width / 2) + yNd + self.width * math.sin(rad_angle))
            r3x, r3y = x1, y1
            r4x, r4y = x2, y2
            cx, cy = self.calc.punto_intersezione(r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y)
            P1, P2 = self.calc.intersezione_retta_circonferenza(-1/m, cx, cy)
            A, B = self.calc.punti_equidistanti(P1, P2, distanza)
            self.canvas.coords(line_element, A[0], A[1], B[0], B[1])
            if angle_deg in [10, 20, 30, -10, -20, -30]:
                self.canvas.coords(label_element_right, B[0] + 12, B[1])
                self.canvas.coords(label_element_left, A[0] - 12, A[1])
