from __future__ import annotations

from geometrie.point import Point
from geometrie.segment import Segment

from figures.figure import Figure
from figures.fruit_de_vie import FruitDeVie


class CubeMetatron(Figure):
    """
    Construction du Cube de Métatron.

    Il est constitué :

    - des 13 cercles du Fruit de Vie
    - des 13 centres
    - des segments reliant chaque centre
      à tous les autres centres.
    """

    def __init__(
        self,
        centre: Point,
        rayon: float,
        couronnes: int = 2
    ):

        super().__init__(
            nom="Cube de Métatron",
            description="Construction issue du Fruit de Vie.",
            tags={
                "géométrie sacrée",
                "métatron",
                "platon",
                "cube"
            },
            parametres={
                "rayon": rayon,
                "couronnes": couronnes
            }
        )

        self.centre = centre
        self.rayon = rayon
        self.couronnes = couronnes

        # Figure source
        self.fruit = None

        # Eléments remarquables
        self.centres = []

        self.segments_metatron = []

        self.construire()

    # ======================================================

    def construire(self):

        self.vider()

        self.centres.clear()
        self.segments_metatron.clear()

        #
        # Fruit de Vie
        #

        self.fruit = FruitDeVie(
            centre=self.centre,
            rayon=self.rayon,
            couronnes=self.couronnes
        )

        #
        # Conservation des cercles
        #

        for cercle in self.fruit.cercles:
            self.ajouter_cercle(cercle)

        #
        # Centres des cercles
        #

        self.centres.extend(
            self.fruit.centres
        )

        for point in self.centres:
            self.ajouter_point(point)

        #
        # Toutes les connexions
        #

        n = len(self.centres)

        for i in range(n):

            for j in range(i + 1, n):

                segment = Segment(
                    self.centres[i],
                    self.centres[j]
                )

                self.segments_metatron.append(
                    segment
                )

                self.ajouter_segment(
                    segment
                )