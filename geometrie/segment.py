from dataclasses import dataclass
from .point import Point
from geometrie.boite_englobante import BoiteEnglobante
import math

@dataclass(frozen=True)
class Segment:
    """Représente un segment défini par deux points."""

    debut: Point
    fin: Point

    @property
    def longueur(self) -> float:
        """Longueur du segment."""
        return self.debut.distance(self.fin)

    @property
    def milieu(self) -> Point:
        """Retourne le milieu du segment."""
        return Point(
            (self.debut.x + self.fin.x) / 2,
            (self.debut.y + self.fin.y) / 2
        )

    @property
    def boite_englobante(self):

        return BoiteEnglobante(

            min(self.debut.x, self.fin.x),

            min(self.debut.y, self.fin.y),

            max(self.debut.x, self.fin.x),

            max(self.debut.y, self.fin.y)

        )

    def translation(self, dx: float, dy: float) -> "Segment":
        """Retourne un nouveau segment translaté."""
        return Segment(
            self.debut.translation(dx, dy),
            self.fin.translation(dx, dy)
        )

    @property
    def vecteur(self):
        from .vecteur import Vecteur
        return Vecteur.depuis_points(
            self.debut,
            self.fin
        )

    @property
    def angle(self):
        return self.vecteur.angle

    def rotation(self, angle: float):

        return Segment(
            self.debut.rotation(angle),
            self.fin.rotation(angle)
        )


    def rotation_autour(self, centre, angle):

        return Segment(
            self.debut.rotation_autour(centre, angle),
            self.fin.rotation_autour(centre, angle)
        )

    def echelle(
        self,
        facteur: float
    ) -> "Segment":
        """
        Homothétie par rapport à l'origine.
        """

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return Segment(
            self.debut.echelle(facteur),
            self.fin.echelle(facteur)
        )


    def echelle_autour(
        self,
        centre: Point,
        facteur: float
    ) -> "Segment":
        """
        Homothétie par rapport à un point.
        """

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return Segment(
            self.debut.echelle_autour(
                centre,
                facteur
            ),
            self.fin.echelle_autour(
                centre,
                facteur
            )
        )