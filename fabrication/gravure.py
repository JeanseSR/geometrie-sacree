from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Gravure:
    """
    Décrit une opération de gravure sur une figure géométrique.

    Cette classe ne crée aucune géométrie 3D.
    Elle définit uniquement les paramètres de fabrication.
    """

    profondeur: float

    def __post_init__(self):

        if self.profondeur <= 0:
            raise ValueError(
                "La profondeur de gravure doit être "
                "strictement positive."
            )

    def appliquer(self, figure):
        """
        Associe une profondeur de gravure à une figure.

        La figure originale n'est jamais modifiée.
        """

        return GravureGeometrique(
            figure=figure,
            profondeur=self.profondeur,
        )


@dataclass(frozen=True)
class GravureGeometrique:
    """
    Figure préparée pour une opération de gravure.

    La géométrie reste 2D.
    La profondeur indique la future extrusion 3D.
    """

    figure: object
    profondeur: float

    @property
    def boite_englobante(self):
        return self.figure.boite_englobante

    @property
    def largeur(self):
        return self.boite_englobante.largeur

    @property
    def hauteur(self):
        return self.boite_englobante.hauteur

    @property
    def couronnes(self):
        return self.figure.couronnes_geometriques