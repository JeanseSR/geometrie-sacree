from __future__ import annotations

from dataclasses import dataclass
import math
from .boite_englobante import BoiteEnglobante
from .vecteur import Vecteur

# CORRECTION étape 3 : Point devient figé (frozen=True).
#
# Avant : @dataclass + __init__ écrit à la main.
#   -> le point était modifiable (p.x = 5 possible)
#   -> et NON hachable : impossible de le mettre dans un set
#      ou de l'utiliser comme clé de dict (dataclass avec eq=True
#      et sans frozen met __hash__ à None).
#
# Après : frozen=True génère automatiquement
#   __init__(x, y), __eq__ et __hash__,
# et interdit toute modification (FrozenInstanceError).
# Toutes les transformations (translation, rotation...)
# renvoyaient déjà un NOUVEAU Point : rien ne change pour elles.
#
# Utilité : dédupliquer des points / segments avec un set
# (traits superposés du Métatron, à éviter au laser).
@dataclass(frozen=True)
class Point:
    """Représente un point du plan (immuable)."""

    x: float
    y: float

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