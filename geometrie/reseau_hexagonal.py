from __future__ import annotations

from dataclasses import dataclass, field
from math import cos, radians, sin
from typing import Iterator

from geometrie.point import Point


@dataclass
class ReseauHexagonal:
    """
    Générateur d'un réseau hexagonal.

    Le réseau est constitué des centres des cercles de la
    géométrie sacrée.

    Exemple :

        couronnes = 0 -> 1 point
        couronnes = 1 -> 7 points
        couronnes = 2 -> 19 points
        couronnes = 3 -> 37 points
    """

    centre: Point
    pas: float
    couronnes: int

    points: list[Point] = field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        self.construire()

    def __iter__(self) -> Iterator[Point]:
        return iter(self.points)

    def __len__(self) -> int:
        return len(self.points)

    def construire(self) -> None:
        """
        Construit le réseau.
        """

        self.points.clear()

        # Centre
        self.points.append(self.centre)

        for couronne in range(1, self.couronnes + 1):
            self._ajouter_couronne(couronne)

    def _ajouter_couronne(self, rayon_hex: int) -> None:
        """
        Ajoute une couronne complète.

        Version V1 :
        Les points sont répartis uniformément tous les
        60 / rayon_hex degrés.

        Cette implémentation sera remplacée par une version
        utilisant les coordonnées hexagonales.
        """

        nb_points = 6 * rayon_hex

        distance = rayon_hex * self.pas

        for i in range(nb_points):

            angle = i * (360 / nb_points)

            self.points.append(
                Point(
                    self.centre.x +
                    distance * cos(radians(angle)),

                    self.centre.y +
                    distance * sin(radians(angle))
                )
            )