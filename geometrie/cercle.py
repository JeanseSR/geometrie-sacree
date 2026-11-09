from dataclasses import dataclass
from .point import Point
from geometrie.boite_englobante import BoiteEnglobante
import math


@dataclass(frozen=True)
class Cercle:
    """
    Représente un cercle.

    Toutes les dimensions sont exprimées en millimètres.
    """

    centre: Point
    rayon: float

    def __post_init__(self):
        if self.rayon <= 0:
            raise ValueError("Le rayon doit être strictement positif.")

    @property
    def diametre(self) -> float:
        """Retourne le diamètre."""
        return self.rayon * 2

    @property
    def perimetre(self) -> float:
        """Retourne le périmètre."""
        return 2 * math.pi * self.rayon

    @property
    def aire(self) -> float:
        """Retourne l'aire."""
        return math.pi * self.rayon ** 2

    @property
    def boite_englobante(self):

        return BoiteEnglobante(

            self.centre.x - self.rayon,

            self.centre.y - self.rayon,

            self.centre.x + self.rayon,

            self.centre.y + self.rayon

        )

    def translation(self, dx: float, dy: float) -> "Cercle":
        """Retourne un nouveau cercle déplacé."""
        return Cercle(
            self.centre.translation(dx, dy),
            self.rayon
        )

    def contient(self, point: Point) -> bool:
        """Indique si un point est situé dans ou sur le cercle."""
        return self.centre.distance(point) <= self.rayon


    def rotation(self, angle):

        return Cercle(
            self.centre.rotation(angle),
            self.rayon
        )

    def rotation_autour(self, centre, angle):

        return Cercle(
            self.centre.rotation_autour(
                centre,
                angle
            ),
            self.rayon
        )

    def echelle( self, facteur: float ) -> "Cercle": 
        """ Homothétie par rapport à l'origine. """ 
        if facteur <= 0: 
            raise ValueError( "Le facteur d'échelle doit être positif." ) 
        return Cercle( 
            self.centre.echelle(facteur), 
            self.rayon * facteur 
        ) 
        
    def echelle_autour( self, centre: Point, facteur: float ) -> "Cercle": 
        """ Homothétie par rapport à un point. """ 
        if facteur <= 0: 
            raise ValueError( "Le facteur d'échelle doit être positif." ) 
        return Cercle( 
            self.centre.echelle_autour( centre, facteur ), 
            self.rayon * facteur 
        )

    def point(self, angle: float):

        a = math.radians(angle)

        return Point(
            self.centre.x + self.rayon * math.cos(a),
            self.centre.y + self.rayon * math.sin(a)
        )

    def contient(self, point):

        return (
            self.centre.distance(point)
            <= self.rayon
        )