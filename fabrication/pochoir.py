from __future__ import annotations

from dataclasses import dataclass

from geometrie.boite_englobante import BoiteEnglobante


@dataclass(frozen=True)
class Pochoir:
    """
    Support destiné à la réalisation d'un pochoir.

    Le pochoir est une plaque dans laquelle la géométrie
    de la figure pourra être évidée.

    Toutes les dimensions sont exprimées en mm.
    """

    largeur: float
    hauteur: float
    epaisseur: float

    def __post_init__(self):

        if self.largeur <= 0:
            raise ValueError(
                "La largeur du pochoir doit être "
                "strictement positive."
            )

        if self.hauteur <= 0:
            raise ValueError(
                "La hauteur du pochoir doit être "
                "strictement positive."
            )

        if self.epaisseur <= 0:
            raise ValueError(
                "L'épaisseur du pochoir doit être "
                "strictement positive."
            )

    # ==========================================================
    # DIMENSIONS
    # ==========================================================

    @property
    def volume(self) -> float:
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
        return (0.0, 0.0)

    # ==========================================================
    # BOITE ENGLOBANTE
    # ==========================================================

    @property
    def boite_englobante(self) -> BoiteEnglobante:

        return BoiteEnglobante(
            -self.largeur / 2,
            -self.hauteur / 2,
            self.largeur / 2,
            self.hauteur / 2,
        )

    # ==========================================================
    # REPRESENTATION
    # ==========================================================

    def __repr__(self):

        return (
            "Pochoir("
            f"largeur={self.largeur:.3f}, "
            f"hauteur={self.hauteur:.3f}, "
            f"epaisseur={self.epaisseur:.3f}"
            ")"
        )