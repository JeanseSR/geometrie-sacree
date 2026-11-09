from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Iterator

from geometrie.point import Point


@dataclass
class ReseauHexagonalAxial:
    """
    Générateur d'un véritable réseau hexagonal
    basé sur les coordonnées axiales.

    Nombre de points :

        couronnes = 0 -> 1 point
        couronnes = 1 -> 7 points
        couronnes = 2 -> 19 points
        couronnes = 3 -> 37 points

    """

    centre: Point
    pas: float
    couronnes: int

    points: list[Point] = field(
        init=False,
        default_factory=list
    )

    couronnes_points: list[list[Point]] = field(
        init=False,
        default_factory=list
    )


    def __post_init__(self):

        self.construire()


    def __iter__(self) -> Iterator[Point]:

        return iter(self.points)


    def __len__(self):

        return len(self.points)


    def construire(self):

        self.points.clear()
        self.couronnes_points.clear()


        # Centre

        centre = self.convertir_point(
            0,
            0
        )

        self.points.append(
            centre
        )

        self.couronnes_points.append(
            [centre]
        )


        # Couronnes suivantes

        for rayon in range(
            1,
            self.couronnes + 1
        ):

            points_couronne = []


            for q, r in self.coordonnees_couronne(rayon):

                point = self.convertir_point(
                    q,
                    r
                )

                self.points.append(
                    point
                )

                points_couronne.append(
                    point
                )


            self.couronnes_points.append(
                points_couronne
            )


    def convertir_point(
        self,
        q: int,
        r: int
    ) -> Point:

        """
        Conversion coordonnées axiales
        vers coordonnées cartésiennes.

        Hexagones plats.
        """

        x = self.pas * (
            sqrt(3) * q
            +
            sqrt(3) / 2 * r
        )


        y = self.pas * (
            3 / 2 * r
        )


        return Point(
            self.centre.x + x,
            self.centre.y + y
        )

    def coordonnees_couronne(self, rayon: int ) :

        """
        Génère une couronne hexagonale complète.
        """

        directions = [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
        ]


        # Point de départ de la couronne
        q = -rayon
        r = rayon


        for dq, dr in directions:

            for _ in range(rayon):

                yield q, r

                q += dq
                r += dr