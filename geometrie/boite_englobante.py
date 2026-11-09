from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BoiteEnglobante:
    """
    Boîte englobante 2D.

    Elle est totalement indépendante du reste de la bibliothèque.
    """

    xmin: float
    ymin: float
    xmax: float
    ymax: float

    # ==========================================================
    # DIMENSIONS
    # ==========================================================

    @property
    def largeur(self) -> float:
        return self.xmax - self.xmin

    @property
    def hauteur(self) -> float:
        return self.ymax - self.ymin

    # ==========================================================
    # CENTRE
    # ==========================================================

    @property
    def centre_x(self) -> float:
        return (self.xmin + self.xmax) / 2

    @property
    def centre_y(self) -> float:
        return (self.ymin + self.ymax) / 2

    @property
    def centre(self) -> tuple[float, float]:
        return (
            self.centre_x,
            self.centre_y
        )

    # ==========================================================
    # TESTS
    # ==========================================================

    def contient(
        self,
        x: float,
        y: float
    ) -> bool:

        return (
            self.xmin <= x <= self.xmax
            and
            self.ymin <= y <= self.ymax
        )

    # ==========================================================
    # MARGE
    # ==========================================================

    def marge(
        self,
        valeur: float
    ) -> "BoiteEnglobante":

        return BoiteEnglobante(

            self.xmin - valeur,

            self.ymin - valeur,

            self.xmax + valeur,

            self.ymax + valeur

        )

    # ==========================================================
    # UNION
    # ==========================================================

    def union(
        self,
        autre: "BoiteEnglobante"
    ) -> "BoiteEnglobante":

        return BoiteEnglobante(

            min(self.xmin, autre.xmin),

            min(self.ymin, autre.ymin),

            max(self.xmax, autre.xmax),

            max(self.ymax, autre.ymax)

        )

    # ==========================================================
    # INTERSECTION
    # ==========================================================

    def intersecte(
        self,
        autre: "BoiteEnglobante"
    ) -> bool:

        return not (

            self.xmax < autre.xmin
            or

            self.xmin > autre.xmax
            or

            self.ymax < autre.ymin
            or

            self.ymin > autre.ymax

        )

    # ==========================================================
    # TRANSLATION
    # ==========================================================

    def translation(
        self,
        dx: float,
        dy: float
    ) -> "BoiteEnglobante":

        return BoiteEnglobante(

            self.xmin + dx,

            self.ymin + dy,

            self.xmax + dx,

            self.ymax + dy

        )

    # ==========================================================
    # REPRESENTATION
    # ==========================================================

    def __repr__(self):

        return (

            "BoiteEnglobante("

            f"xmin={self.xmin:.3f}, "

            f"ymin={self.ymin:.3f}, "

            f"xmax={self.xmax:.3f}, "

            f"ymax={self.ymax:.3f}"

            ")"

        )