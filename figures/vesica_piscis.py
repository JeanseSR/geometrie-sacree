from geometrie.point import Point
from geometrie.cercle import Cercle
from geometrie.intersection import cercle_cercle

from figures.figure import Figure


class VesicaPiscis(Figure):
    """
    Construction géométrique de la Vesica Piscis.

    Deux cercles de même rayon dont le centre
    de chacun appartient au cercle de l'autre.
    """

    def __init__(
        self,
        centre: Point,
        rayon: float
    ):

        super().__init__(
            nom="Vesica Piscis",
            description=(
                "Deux cercles identiques dont "
                "le centre de chacun appartient "
                "à la circonférence de l'autre."
            ),
            tags={
                "géométrie sacrée",
                "vesica",
                "cercle"
            },
            parametres={
                "rayon": rayon
            }
        )

        self.centre = centre
        self.rayon = rayon

        # éléments remarquables
        self.cercle_gauche = None
        self.cercle_droit = None

        self.intersection_haute = None
        self.intersection_basse = None

        self.construire()


    def construire(self):

        self.vider()

        # Premier cercle
        self.cercle_gauche = Cercle(
            self.centre,
            self.rayon
        )


        # Deuxième centre décalé d'un rayon
        centre_droit = self.centre.translation(
            self.rayon,
            0
        )

        self.cercle_droit = Cercle(
            centre_droit,
            self.rayon
        )


        # Ajout géométrie principale
        self.ajouter_cercle(
            self.cercle_gauche
        )

        self.ajouter_cercle(
            self.cercle_droit
        )


        # Calcul intersections
        intersections = cercle_cercle(
            self.cercle_gauche,
            self.cercle_droit
        )


        if intersections:

            # On suppose :
            # premier point = haut
            # second point = bas

            self.intersection_haute = intersections[0]
            self.intersection_basse = intersections[1]


            self.ajouter_point(
                self.intersection_haute
            )

            self.ajouter_point(
                self.intersection_basse
            )