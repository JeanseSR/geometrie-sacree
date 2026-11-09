from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Plaque:
    """
    Plaque rectangulaire destinée à recevoir une fabrication.

    Toutes les dimensions sont exprimées en millimètres.

    La plaque est centrée sur l'origine (0, 0).
    """

    largeur: float
    hauteur: float
    epaisseur: float

    def __post_init__(self):

        if self.largeur <= 0:
            raise ValueError(
                "La largeur de la plaque doit être "
                "strictement positive."
            )

        if self.hauteur <= 0:
            raise ValueError(
                "La hauteur de la plaque doit être "
                "strictement positive."
            )

        if self.epaisseur <= 0:
            raise ValueError(
                "L'épaisseur de la plaque doit être "
                "strictement positive."
            )

    # ==========================================================
    # DIMENSIONS
    # ==========================================================

    @property
    def volume(self) -> float:
        """
        Retourne le volume théorique de la plaque.
        """

        return (
            self.largeur
            * self.hauteur
            * self.epaisseur
        )

    # ==========================================================
    # CENTRE
    # ==========================================================

    @property
    def centre(self) -> tuple[float, float]:
        """
        Centre géométrique de la plaque.
        """

        return (0.0, 0.0)

    # ==========================================================
    # BOÎTE ENGLOBANTE 2D
    # ==========================================================

    @property
    def xmin(self) -> float:
        return -self.largeur / 2

    @property
    def xmax(self) -> float:
        return self.largeur / 2

    @property
    def ymin(self) -> float:
        return -self.hauteur / 2

    @property
    def ymax(self) -> float:
        return self.hauteur / 2
        