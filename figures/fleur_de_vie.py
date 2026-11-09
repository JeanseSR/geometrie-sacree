from __future__ import annotations

from math import sqrt

from geometrie.point import Point
from geometrie.cercle import Cercle
from figures.figure import Figure


class FleurDeVie(Figure):
    """
    Fleur de Vie construite sur une maille hexagonale.

    Chaque cercle possède le même rayon que la distance
    entre deux centres voisins.

    couronnes = 0 -> 1 cercle
    couronnes = 1 -> 7 cercles
    couronnes = 2 -> 19 cercles
    couronnes = 3 -> 37 cercles
    couronnes = 4 -> 61 cercles
    couronnes = 5 -> 91 cercles
    couronnes = 6 -> 127 cercles
    """

    def __init__(
        self,
        centre: Point,
        rayon: float,
        couronnes: int = 1,
    ):
        super().__init__(
            nom="Fleur de Vie",
            description="Fleur de Vie construite sur une maille hexagonale",
            unite="mm",
            tags={
                "géométrie sacrée",
                "fleur",
                "fleur de vie",
                "mandala",
            },
            parametres={
                "rayon": rayon,
                "couronnes": couronnes,
            },
        )

        if rayon <= 0:
            raise ValueError(
                "Le rayon doit être strictement positif."
            )

        if couronnes < 0:
            raise ValueError(
                "Le nombre de couronnes doit être positif ou nul."
            )

        if not isinstance(couronnes, int):
            raise TypeError(
                "couronnes doit être un entier."
            )

        self.centre = centre
        self.rayon = float(rayon)
        self._couronnes = couronnes

        self._construire()

    # ==========================================================
    # PROPRIÉTÉS
    # ==========================================================

    @property
    def couronnes(self) -> int:
        return self._couronnes

    @property
    def nombre_cercles_attendu(self) -> int:
        """
        Nombre total de cercles pour n couronnes.

        1 + 6(1 + 2 + ... + n)
        = 1 + 3n(n+1)
        """

        n = self.couronnes

        return 1 + 3 * n * (n + 1)

    # ==========================================================
    # CONSTRUCTION
    # ==========================================================

    def _construire(self) -> None:
        """
        Construit la Fleur de Vie sur une maille hexagonale.

        Les coordonnées utilisent des coordonnées axiales (q, r).
        Chaque centre voisin est distant exactement de `rayon`.
        """

        self.vider()

        r = self.rayon

        for q in range(-self.couronnes, self.couronnes + 1):

            for s in range(-self.couronnes, self.couronnes + 1):

                # Distance hexagonale depuis le centre.
                distance = max(
                    abs(q),
                    abs(s),
                    abs(q + s),
                )

                if distance > self.couronnes:
                    continue

                # Conversion coordonnées axiales -> cartésiennes.
                x = r * (
                    q + s / 2
                )

                y = r * (
                    sqrt(3) / 2 * s
                )

                point = Point(
                    self.centre.x + x,
                    self.centre.y + y,
                )

                self.ajouter_cercle(
                    Cercle(
                        centre=point,
                        rayon=r,
                    )
                )

    # ==========================================================
    # INFORMATIONS
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "FleurDeVie("
            f"centre={self.centre}, "
            f"rayon={self.rayon}, "
            f"couronnes={self.couronnes}, "
            f"cercles={len(self.cercles)}"
            ")"
        )