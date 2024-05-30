
import tkinter as tk

class Viewfinder:

    """
    Classe per creare un mirino per il display di volo primario (PFD).

    Attributi:
        width (int): La larghezza della tela del mirino.
        height (int): L'altezza della tela del mirino.
        canvas (tk.Canvas): La tela su cui è disegnato il mirino.
        viewfinder (int): Il poligono che rappresenta il mirino centrale.
        rightWind (int): Il poligono che rappresenta l'indicatore del vento destro.
        leftWind (int): Il poligono che rappresenta l'indicatore del vento sinistro.
    """

    def __init__(self, width, height,canvas):
        """
        Inizializza il mirino.

        Argomenti:
            width (int): La larghezza della tela del mirino.
            height (int): L'altezza della tela del mirino.
            canvas (tk.Canvas): La tela su cui è disegnato il mirino.
        """
        self.width = width
        self.height = height
        self.canvas = canvas
        self.viewfinder = self.canvas.create_polygon(self.draw_viewfinder(), outline='white', fill='black', width=2)
        self.rightWind = self.canvas.create_polygon( self.draw_wind(True),outline='white', fill='black', width=2)
        self.leftWind = self.canvas.create_polygon(self.draw_wind(False),outline='white',fill='black',width=2 )

    def draw_wind(self, inverse):
        """
        Disegna gli indicatori del vento sul mirino.

        Argomenti:
            inverse (bool): Se True, disegna l'indicatore del vento destro. Se False, disegna l'indicatore del vento sinistro.

        Ritorna:
            list: Elenco di punti che rappresentano il poligono dell'indicatore del vento.
        """
        CC = (self.width // 2, self.height // 2)
        horizontal_offset = 120
        vertical_offset = 5
        lower_vertical_offset = 30
        side_offset = 15
        center_offset = 70
        A = (CC[0] - center_offset, CC[1] - vertical_offset)
        B = (CC[0] - center_offset - horizontal_offset, CC[1] - vertical_offset)
        C = (CC[0] - center_offset - horizontal_offset, CC[1] + 10)
        D = (CC[0] - center_offset - side_offset, CC[1] + 10)
        E = (CC[0] - center_offset - side_offset, CC[1] + lower_vertical_offset)
        F = (CC[0] - center_offset, CC[1] + lower_vertical_offset)
        points = [A, B, C, D, E, F]
        if inverse:
            points = [(self.width - x, y) for x, y in points]
        return points
        

    def draw_viewfinder(self):
        """
        Disegna il mirino centrale sulla tela.

        Ritorna:
            list: Elenco di punti che rappresentano il poligono del mirino centrale.
        """
        CC = (self.width // 2, self.height // 2)
        side_length = 17  
        points = [
            (CC[0] - side_length // 2, CC[1] - side_length // 2),
            (CC[0] + side_length // 2, CC[1] - side_length // 2),
            (CC[0] + side_length // 2, CC[1] + side_length // 2),
            (CC[0] - side_length // 2, CC[1] + side_length // 2)
        ]
        return points