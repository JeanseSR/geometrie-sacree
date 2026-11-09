from __future__ import annotations

from dataclasses import dataclass

from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.boite_englobante import BoiteEnglobante


@dataclass(frozen=True)
class BandeSegment:
    """
    Bande de largeur constante autour d'un segment.

    Cette primitive représente un trait destiné
    à la fabrication.

    Toutes les dimensions sont exprimées en mm.
    """

    debut: Point
    fin: Point
    largeur: float

    def __post_init__(self):

        if self.largeur <= 0:
            raise ValueError(
                "La largeur doit être strictement positive."
            )

        if self.debut == self.fin:
            raise ValueError(
                "Un segment ne peut pas avoir "
                "deux extrémités identiques."
            )

    # ==========================================================
    # SEGMENT SOURCE
    # ==========================================================

    @property
    def segment(self) -> Segment:

        return Segment(
            self.debut,
            self.fin
        )

    # ==========================================================
    # DIMENSIONS
    # ==========================================================

    @property
    def longueur(self) -> float:

        return self.segment.longueur

    @property
    def rayon(self) -> float:

        return self.largeur / 2

    # ==========================================================
    # BOITE ENGLOBANTE
    # ==========================================================

    @property
    def boite_englobante(self):

        marge = self.rayon

        boite = self.segment.boite_englobante

        return BoiteEnglobante(
            boite.xmin - marge,
            boite.ymin - marge,
            boite.xmax + marge,
            boite.ymax + marge
        )

    # ==========================================================
    # TRANSLATION
    # ==========================================================

    def translation(
        self,
        dx: float,
        dy: float
    ) -> "BandeSegment":

        return BandeSegment(
            self.debut.translation(dx, dy),
            self.fin.translation(dx, dy),
            self.largeur
        )

    # ==========================================================
    # ROTATION
    # ==========================================================

    def rotation(
        self,
        angle: float
    ) -> "BandeSegment":

        return BandeSegment(
            self.debut.rotation(angle),
            self.fin.rotation(angle),
            self.largeur
        )

    def rotation_autour(
        self,
        centre: Point,
        angle: float
    ) -> "BandeSegment":

        return BandeSegment(
            self.debut.rotation_autour(
                centre,
                angle
            ),
            self.fin.rotation_autour(
                centre,
                angle
            ),
            self.largeur
        )

    # ==========================================================
    # ECHELLE
    # ==========================================================

    def echelle(
        self,
        facteur: float
    ) -> "BandeSegment":

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return BandeSegment(
            self.debut.echelle(facteur),
            self.fin.echelle(facteur),
            self.largeur * facteur
        )

    def echelle_autour(
        self,
        centre: Point,
        facteur: float
    ) -> "BandeSegment":

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return BandeSegment(
            self.debut.echelle_autour(
                centre,
                facteur
            ),
            self.fin.echelle_autour(
                centre,
                facteur
            ),
            self.largeur * facteur
        )

    def mise_a_echelle(
        self,
        facteur: float,
        centre: Point = Point(0, 0)
    ) -> "BandeSegment":

        return self.echelle_autour(
            centre,
            facteur
        )