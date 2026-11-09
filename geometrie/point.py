from __future__ import annotations

from dataclasses import dataclass
import math
from .boite_englobante import BoiteEnglobante
from .vecteur import Vecteur

@dataclass
class Point:
    """Représente un point du plan."""

    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def boite_englobante(self):

        return BoiteEnglobante(
            self.x,
            self.y,
            self.x,
            self.y
        )

    def distance(self, autre):

        return math.hypot(
            autre.x - self.x,
            autre.y - self.y
        )

    def translation(self, dx: float, dy: float) -> "Point":
        """Retourne un nouveau point translaté."""
        return Point(
            self.x + dx,
            self.y + dy
        )

    def rotation(self, angle: float) -> "Point":
        a = math.radians(angle)

        c = math.cos(a)
        s = math.sin(a)

        return Point(
            self.x * c - self.y * s,
            self.x * s + self.y * c
        )

    def rotation_autour(self, centre: "Point", angle: float) -> "Point":

        return (
            self
            .translation(-centre.x, -centre.y)
            .rotation(angle)
            .translation(centre.x, centre.y)
        )

    def echelle( self, facteur: float ) -> "Point": 
        """ Homothétie par rapport à l'origine. """ 
        if facteur <= 0: 
            raise ValueError( "Le facteur d'échelle doit être positif." ) 
        return Point( 
            self.x * facteur, 
            self.y * facteur 
        ) 

    def echelle_autour( self, centre: "Point", facteur: float ) -> "Point": 
        """ Homothétie par rapport à un point. """ 
        if facteur <= 0: 
            raise ValueError( "Le facteur d'échelle doit être positif." ) 
        return Point( 
            centre.x + (self.x - centre.x) * facteur,
            centre.y + (self.y - centre.y) * facteur 
        )
    
    def __add__(self, vecteur: Vecteur) -> "Point":
        return Point(
            self.x + vecteur.x,
            self.y + vecteur.y
        )

    def __sub__(self, autre):
        from .vecteur import Vecteur

        if isinstance(autre, Point):
            return Vecteur(
                self.x - autre.x,
                self.y - autre.y
            )

        elif isinstance(autre, Vecteur):
            return Point(
                self.x - autre.x,
                self.y - autre.y
            )

        return NotImplemented