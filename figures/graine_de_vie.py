from math import cos, sin, radians

from geometrie.point import Point
from geometrie.cercle import Cercle

from figures.figure import Figure


class GraineDeVie(Figure):
    """
    Construction de la Graine de Vie.

    La figure est composée de 7 cercles :
    - un cercle central
    - six cercles autour
    """

    def __init__(
        self,
        centre: Point,
        rayon: float
    ):

        super().__init__(
            nom="Graine de Vie",
            description=(
                "Figure composée de sept cercles identiques "
                "disposés autour d'un cercle central."
            ),
            tags={
                "géométrie sacrée",
                "graine",
                "cercle"
            },
            parametres={
                "rayon": rayon
            }
        )

        self.centre = centre
        self.rayon = rayon

        self.cercle_central = None
        self.cercles_couronne = []

        self.construire()


    def construire(self):

        self.vider()

        self.cercles_couronne.clear()


        # --------------------------------------------------
        # Cercle central
        # --------------------------------------------------

        self.cercle_central = Cercle(
            self.centre,
            self.rayon
        )

        self.ajouter_cercle(
            self.cercle_central
        )


        # --------------------------------------------------
        # Six cercles autour
        # --------------------------------------------------

        for angle in range(0, 360, 60):

            centre = Point(
                self.centre.x +
                self.rayon * cos(radians(angle)),

                self.centre.y +
                self.rayon * sin(radians(angle))
            )


            cercle = Cercle(
                centre,
                self.rayon
            )


            self.cercles_couronne.append(
                cercle
            )


            self.ajouter_cercle(
                cercle
            )