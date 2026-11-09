from __future__ import annotations

from dataclasses import dataclass

from geometrie.point import Point
from geometrie.cercle import Cercle
from geometrie.boite_englobante import BoiteEnglobante


@dataclass(slots=True)
class Couronne:
    """
    Couronne (anneau) comprise entre deux cercles concentriques.
    """

    centre: Point

    rayon_interieur: float

    rayon_exterieur: float

    # ==========================================================
    # PROPRIÉTÉS
    # ==========================================================

    @property
    def largeur(self):

        return (
            self.rayon_exterieur
            - self.rayon_interieur
        )

    @property
    def cercle_interieur(self) -> Cercle:

        return Cercle(
            centre=self.centre,
            rayon=self.rayon_interieur
        )

    @property
    def cercle_exterieur(self) -> Cercle:

        return Cercle(
            centre=self.centre,
            rayon=self.rayon_exterieur
        )

    # ==========================================================
    # BOÎTE ENGLOBANTE
    # ==========================================================

    @property
    def boite_englobante(self):

        r = self.rayon_exterieur

        return BoiteEnglobante(
            self.centre.x - r,
            self.centre.y - r,
            self.centre.x + r,
            self.centre.y + r
        )

    # ==========================================================
    # TRANSLATION
    # ==========================================================

    def translation(
        self,
        dx: float,
        dy: float
    ) -> "Couronne":

        return Couronne(
            centre=self.centre.translation(dx, dy),
            rayon_interieur=self.rayon_interieur,
            rayon_exterieur=self.rayon_exterieur,
        )


    # ==========================================================
    # ROTATION
    # ==========================================================

    def rotation(
        self,
        angle: float
    ) -> "Couronne":

        return Couronne(
            centre=self.centre.rotation(angle),
            rayon_interieur=self.rayon_interieur,
            rayon_exterieur=self.rayon_exterieur,
        )


    # ==========================================================
    # ROTATION AUTOUR D'UN CENTRE
    # ==========================================================

    def rotation_autour(
        self,
        centre: Point,
        angle: float
    ) -> "Couronne":

        return Couronne(
            centre=self.centre.rotation_autour(
                centre,
                angle
            ),
            rayon_interieur=self.rayon_interieur,
            rayon_exterieur=self.rayon_exterieur,
        )


    # ==========================================================
    # ÉCHELLE
    # ==========================================================

    def echelle(
        self,
        facteur: float
    ) -> "Couronne":

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return Couronne(
            centre=self.centre.echelle(facteur),
            rayon_interieur=self.rayon_interieur * facteur,
            rayon_exterieur=self.rayon_exterieur * facteur,
        )


    # ==========================================================
    # ÉCHELLE AUTOUR D'UN CENTRE
    # ==========================================================

    def echelle_autour(
        self,
        centre: Point,
        facteur: float
    ) -> "Couronne":

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        return Couronne(
            centre=self.centre.echelle_autour(
                centre,
                facteur
            ),
            rayon_interieur=self.rayon_interieur * facteur,
            rayon_exterieur=self.rayon_exterieur * facteur,
        )