import math

class Calc:
    """
    Classe per calcolare varie proprietà geometriche, come intersezioni tra rette e circonferenze,
    lunghezza di segmenti e punti equidistanti.
    """

    def intersezione_retta_circonferenza(self, m, cx=300, cy=300):
        """
        Calcola le intersezioni di una retta con una circonferenza centrata in (300, 300).

        Argomenti:
            m (float): Coefficiente angolare della retta.
            cx (int): Coordinata x del centro della circonferenza (default: 300).
            cy (int): Coordinata y del centro della circonferenza (default: 300).

        Ritorna:
            tuple: Due punti di intersezione della retta con la circonferenza.
        """
        x = 1 / math.sqrt(1 + m**2)
        y = m / math.sqrt(1 + m**2)  
        P1 = (cx + x, cy + y)
        P2 = (cx - x, cy - y)  
        return P1, P2

    def lunghezza_segmento(self, P1, P2):
        """
        Calcola la lunghezza di un segmento tra due punti P1 e P2.

        Argomenti:
            P1 (tuple): Primo punto del segmento.
            P2 (tuple): Secondo punto del segmento.

        Ritorna:
            float: Lunghezza del segmento.
        """
        return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

    def punti_equidistanti(self, P1, P2, distanza):
        """
        Calcola due punti equidistanti dal centro del segmento P1P2 di una certa distanza.

        Argomenti:
            P1 (tuple): Primo punto del segmento.
            P2 (tuple): Secondo punto del segmento.
            distanza (float): Distanza dal centro del segmento ai punti da calcolare.

        Ritorna:
            tuple: Due punti equidistanti dal centro del segmento.
        """
        # Calcola il centro del segmento P1P2
        C = ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2) 
        # Calcola la direzione del segmento P1P2
        dx = P2[0] - P1[0]
        dy = P2[1] - P1[1]
        # Normalizza la direzione del segmento
        lunghezza = self.lunghezza_segmento(P1, P2)
        dx /= lunghezza
        dy /= lunghezza 
        # Calcola i punti A e B equidistanti dal centro C di una certa distanza
        A = (C[0] + distanza * dx, C[1] + distanza * dy)
        B = (C[0] - distanza * dx, C[1] - distanza * dy)
        return A, B

    @staticmethod
    def equazione_retta(S, E):
        """
        Calcola il coefficiente angolare di una retta passante per i punti S ed E.

        Argomenti:
            S (tuple): Primo punto della retta.
            E (tuple): Secondo punto della retta.

        Ritorna:
            float: Coefficiente angolare della retta.
        """
        x1, y1 = S
        x2, y2 = E
        if x2 == x1:
            return 0
        m = (y2 - y1) / (x2 - x1)
        return m

    @staticmethod
    def coefficiente_angolare(S, E):
        """
        Calcola il coefficiente angolare della retta passante per i punti S ed E.

        Argomenti:
            S (tuple): Primo punto della retta.
            E (tuple): Secondo punto della retta.

        Ritorna:
            float: Coefficiente angolare della retta.
        """
        x1, y1 = S
        x2, y2 = E
        if x2 == x1:
            return float('inf')  # La retta è verticale, restituisce l'infinito
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def punto_intersezione(r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y):
        """
        Calcola il punto di intersezione tra due rette definite dai punti (r1x, r1y)-(r2x, r2y) e (r3x, r3y)-(r4x, r4y).

        Argomenti:
            r1x (float): Coordinata x del primo punto della prima retta.
            r1y (float): Coordinata y del primo punto della prima retta.
            r2x (float): Coordinata x del secondo punto della prima retta.
            r2y (float): Coordinata y del secondo punto della prima retta.
            r3x (float): Coordinata x del primo punto della seconda retta.
            r3y (float): Coordinata y del primo punto della seconda retta.
            r4x (float): Coordinata x del secondo punto della seconda retta.
            r4y (float): Coordinata y del secondo punto della seconda retta.

        Ritorna:
            tuple: Punto di intersezione delle due rette.
        """
        if r2x - r1x == 0:  # Se la retta è verticale, il coefficiente angolare è indefinito
            m1 = float('inf')
        else:
            m1 = (r2y - r1y) / (r2x - r1x)
        if r4x - r3x == 0:  # Se la retta è verticale, il coefficiente angolare è indefinito
            m2 = float('inf')
        else:
            m2 = (r4y - r3y) / (r4x - r3x)

        b1 = r1y - m1 * r1x if m1 != float('inf') else r1x
        b2 = r3y - m2 * r3x if m2 != float('inf') else r3x

        if m1 == m2:  # Se i coefficienti angolari sono uguali, le rette sono parallele e non si intersecano
            return 0, 0

        if m1 == float('inf'):
            x_intersezione = r1x
            y_intersezione = m2 * x_intersezione + b2
        elif m2 == float('inf'):
            x_intersezione = r3x
            y_intersezione = m1 * x_intersezione + b1
        else:
            x_intersezione = (b2 - b1) / (m1 - m2)
            y_intersezione = m1 * x_intersezione + b1

        return x_intersezione, y_intersezione
