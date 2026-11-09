from __future__ import annotations

from dataclasses import dataclass
import math
from geometrie.boite_englobante import BoiteEnglobante

from .point import Point
from .segment import Segment


@dataclass(frozen=True)
class Polygone:
    """
    Représente un polygone défini par une suite ordonnée de sommets.

    Les sommets doivent être fournis dans l'ordre du contour
    (horaire ou antihoraire).
    """

    sommets: tuple[Point, ...]

    # ==========================================================
    # INITIALISATION
    # ==========================================================

    def __post_init__(self) -> None:

        if len(self.sommets) < 3:
            raise ValueError(
                "Un polygone doit contenir au moins trois sommets."
            )

    # ==========================================================
    # PROPRIÉTÉS
    # ==========================================================

    @property
    def nombre_sommets(self) -> int:
        """Nombre de sommets."""
        return len(self.sommets)

    @property
    def segments(self) -> tuple[Segment, ...]:
        """
        Retourne tous les segments constituant le contour.
        """

        n = len(self.sommets)

        return tuple(
            Segment(
                self.sommets[i],
                self.sommets[(i + 1) % n]
            )
            for i in range(n)
        )

    @property
    def perimetre(self) -> float:
        """Retourne le périmètre."""

        return sum(
            segment.longueur
            for segment in self.segments
        )

    @property
    def centre(self) -> Point:
        """
        Retourne le barycentre des sommets.
        """

        n = len(self.sommets)

        return Point(
            sum(p.x for p in self.sommets) / n,
            sum(p.y for p in self.sommets) / n
        )

    @property
    def x_min(self) -> float:
        return min(p.x for p in self.sommets)

    @property
    def x_max(self) -> float:
        return max(p.x for p in self.sommets)

    @property
    def y_min(self) -> float:
        return min(p.y for p in self.sommets)

    @property
    def y_max(self) -> float:
        return max(p.y for p in self.sommets)

    @property
    def largeur(self) -> float:
        return self.x_max - self.x_min

    @property
    def hauteur(self) -> float:
        return self.y_max - self.y_min

    @property
    def cote(self) -> float:
        """
        Longueur du premier côté.

        Pour un polygone régulier, tous les côtés sont identiques.
        """
        return self.segments[0].longueur

    @property
    def rayon_circonscrit(self) -> float:
        """
        Distance entre le centre et un sommet.
        """
        return self.centre.distance(self.sommets[0])

    @property
    def rayon_inscrit(self) -> float:
        """
        Rayon du cercle inscrit (apothem).
        Valable pour un polygone régulier.
        """
        return self.rayon_circonscrit * math.cos(math.pi / self.nombre_sommets)
    

    # ==========================================================
    # BOITE ENGLOBANTE
    # ==========================================================

    @property
    def boite_englobante(self) -> BoiteEnglobante:

        # CORRECTION étape 1 : l'attribut s'appelle `sommets`
        # (`self.points` n'existe pas -> AttributeError).
        xs = [p.x for p in self.sommets]
        ys = [p.y for p in self.sommets]

        return BoiteEnglobante(

            min(xs),

            min(ys),

            max(xs),

            max(ys)

        )

    # ==========================================================
    # TRANSFORMATIONS
    # ==========================================================

    def translation(
        self,
        dx: float,
        dy: float
    ) -> "Polygone":

        return Polygone(
            tuple(
                p.translation(dx, dy)
                for p in self.sommets
            )
        )

    def rotation(
        self,
        angle: float
    ) -> "Polygone":

        return Polygone(
            tuple(
                p.rotation(angle)
                for p in self.sommets
            )
        )

    def rotation_autour(
        self,
        centre: Point,
        angle: float
    ) -> "Polygone":

        return Polygone(
            tuple(
                p.rotation_autour(
                    centre,
                    angle
                )
                for p in self.sommets
            )
        )

    def echelle(
        self,
        facteur: float
    ) -> "Polygone":
        """
        Homothétie par rapport à l'origine.
        """

        return Polygone(
            tuple(
                Point(
                    p.x * facteur,
                    p.y * facteur
                )
                for p in self.sommets
            )
        )

    def echelle_autour(
        self,
        centre: Point,
        facteur: float
    ) -> "Polygone":
        """
        Homothétie par rapport à un point.
        """

        return Polygone(
            tuple(
                Point(
                    centre.x + (p.x - centre.x) * facteur,
                    centre.y + (p.y - centre.y) * facteur
                )
                for p in self.sommets
            )
        )

    # ==========================================================
    # CONSTRUCTEURS
    # ==========================================================

    @classmethod
    def regulier(
        cls,
        centre: Point,
        rayon: float,
        nb_cotes: int,
        angle_depart: float = 0
    ) -> "Polygone":
        """
        Construit un polygone régulier.
        """

        if nb_cotes < 3:
            raise ValueError(
                "Un polygone régulier possède au moins trois côtés."
            )

        sommets = []

        for i in range(nb_cotes):

            angle = math.radians(
                angle_depart +
                i * 360 / nb_cotes
            )

            sommets.append(
                Point(
                    centre.x + rayon * math.cos(angle),
                    centre.y + rayon * math.sin(angle)
                )
            )

        return cls(tuple(sommets))

    # ==========================================================
    # UTILITAIRES
    # ==========================================================

    def __len__(self):
        return len(self.sommets)

    def __iter__(self):
        return iter(self.sommets)

    def __getitem__(self, index):
        return self.sommets[index]

    def __contains__(self, point: Point):
        return point in self.sommets

    def __repr__(self):

        return (
            f"Polygone("
            f"{self.nombre_sommets} sommets)"
        )