import tkinter as tk

class Horizon:
    """
    Classe per creare l'orizzonte artificiale per il display di volo primario (PFD).

    Attributi:
        width (int): La larghezza della tela dell'orizzonte artificiale.
        height (int): L'altezza della tela dell'orizzonte artificiale.
        canvas (tk.Canvas): La tela su cui è disegnato l'orizzonte artificiale.
        skyCoords (list): Coordinate dei punti per il poligono che rappresenta il cielo.
        earthCoords (list): Coordinate dei punti per il poligono che rappresenta la terra.
        lineCoords (list): Coordinate dei punti per la linea dell'orizzonte.
        skyPolygon (tk.Polygon): Poligono che rappresenta il cielo.
        earthPolygon (tk.Polygon): Poligono che rappresenta la terra.
        line (tk.Line): Linea che rappresenta l'orizzonte.
    """

    def __init__(self, width, height, canvas):
        """
        Inizializza l'orizzonte artificiale.

        Argomenti:
            width (int): La larghezza della tela dell'orizzonte artificiale.
            height (int): L'altezza della tela dell'orizzonte artificiale.
            canvas (tk.Canvas): La tela su cui è disegnato l'orizzonte artificiale.
        """
        self.width = width
        self.height = height
        self.canvas = canvas
        self.skyCoords = [
            (0, 0), 
            (width, 0), 
            (width, height), 
            (0, height)
        ]  # Coordinate dei punti per il poligono che rappresenta il cielo
        self.earthCoords = [
            (0, height / 2),
            (width, height / 2),
            (width, height),
            (0, height)
        ]  # Coordinate dei punti per il poligono che rappresenta la terra
        self.lineCoords = [
            (0, height / 2),  
            (width, height / 2)  
        ]  # Coordinate dei punti per la linea dell'orizzonte
        self.skyPolygon = self.canvas.create_polygon(*self.skyCoords, fill='sky blue', outline='')
        self.earthPolygon = self.canvas.create_polygon(*self.earthCoords, fill='saddle brown', outline='')
        self.line = self.canvas.create_line(*self.lineCoords, fill='white', width=4)

    def newCoords(self, coordFs, coordNd, coords, left, right, element, state):
        """
        Aggiorna le coordinate di un elemento dell'orizzonte artificiale e calcola le nuove coordinate
        perpendicolari.

        Argomenti:
            coordFs (int): Indice del primo punto delle coordinate da aggiornare.
            coordNd (int): Indice del secondo punto delle coordinate da aggiornare.
            coords (list): Lista delle coordinate attuali dei punti.
            left (int): Spostamento verticale per il primo punto.
            right (int): Spostamento verticale per il secondo punto.
            element (tk.Element): L'elemento della tela da aggiornare.
            state (bool): Indica se lo spostamento è positivo o negativo.
        """
        coords[coordFs] = (coords[coordFs][0], coords[coordFs][1] + (left if not state else -left))  
        coords[coordNd] = (coords[coordNd][0], coords[coordNd][1] + (right if not state else -right)) 
        flat_coords = [coord for point in coords for coord in point]
        self.canvas.coords(element, *flat_coords)
        coords[coordFs] = (coords[coordFs][0], coords[coordFs][1] - (left if not state else -left))  
        coords[coordNd] = (coords[coordNd][0], coords[coordNd][1] - (right if not state else -right))  
        midpoint = ((coords[coordFs][0] + coords[coordNd][0]) / 2, (coords[coordFs][1] + coords[coordNd][1]) / 2)
        dx = coords[coordNd][0] - coords[coordFs][0]
        dy = coords[coordNd][1] - coords[coordFs][1]
        if dx == 0:
            perp_coords = [(midpoint[0] - self.width / 2, midpoint[1]), (midpoint[0] + self.width / 2, midpoint[1])]
        else:
            slope = dy / dx
            if dy == 0:
                perp_coords = [(midpoint[0], midpoint[1] - self.height / 2), (midpoint[0], midpoint[1] + self.height / 2)]
            else:
                perp_slope = -1 / slope
                x1 = midpoint[0] - self.width / 2
                y1 = midpoint[1] + perp_slope * (x1 - midpoint[0])
                x2 = midpoint[0] + self.width / 2
                y2 = midpoint[1] + perp_slope * (x2 - midpoint[0])
                perp_coords = [(x1, y1), (x2, y2)]
