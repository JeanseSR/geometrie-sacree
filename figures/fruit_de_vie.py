from __future__ import annotations

import math

from geometrie.point import Point
from geometrie.intersection import cercle_cercle

from figures.figure import Figure
from figures.fleur_de_vie import FleurDeVie


class FruitDeVie(Figure):
    """
    Fruit de Vie classique à 13 cercles.

    Construction :

    - 1 cercle central ;
    - 6 cercles sur la première couronne ;
    - 6 cercles sur la deuxième couronne.

    Total : 13 cercles.

    Le Fruit de Vie est construit à partir de la
    Fleur de Vie comme figure source.
    """

    def __init__(
        self,
        centre: Point,
        rayon: float,
        couronnes: int = 2
    ):

        if rayon <= 0:
            raise ValueError(
                "Le rayon doit être strictement positif."
            )

        if couronnes < 2:
            raise ValueError(
                "Le Fruit de Vie nécessite au moins "
                "2 couronnes."
            )

        super().__init__(
            nom="Fruit de Vie",
            description=(
                "Construction à 13 cercles "
                "issue de la Fleur de Vie."
            ),
            tags={
                "géométrie sacrée",
                "fruit",
                "intersections"
            },
            parametres={
                "rayon": rayon,
                "couronnes": couronnes
            }
        )

        self.centre = centre
        self.rayon = rayon
        self.couronnes = couronnes

        # ======================================================
        # FIGURE SOURCE
        # ======================================================

        self.fleur = None

        # ======================================================
        # DONNÉES GÉOMÉTRIQUES
        # ======================================================

        self.intersections = []

        self.points_centraux = []

        self.points_exterieurs = []

        self.construire()

    # ==========================================================
    # CENTRES
    # ==========================================================

    @property
    def centres(self) -> list[Point]:
        """
        Renvoie les 13 centres des cercles
        constituant le Fruit de Vie.
        """

        return [
            cercle.centre
            for cercle in self.cercles
        ]

    # ==========================================================
    # CONSTRUCTION
    # ==========================================================

    def construire(self):

        self.vider()

        self.intersections.clear()

        self.points_centraux.clear()

        self.points_exterieurs.clear()

        # ======================================================
        # FLEUR DE VIE SOURCE
        # ======================================================

        self.fleur = FleurDeVie(
            centre=self.centre,
            rayon=self.rayon,
            couronnes=self.couronnes
        )

        # ======================================================
        # SÉLECTION DES 13 CERCLES
        # ======================================================

        cercles = self._selectionner_13_cercles(
            self.fleur.cercles
        )

        if len(cercles) != 13:
            raise RuntimeError(
                "Le Fruit de Vie doit contenir "
                f"13 cercles, obtenu : {len(cercles)}"
            )

        for cercle in cercles:

            self.ajouter_cercle(
                cercle
            )

        # ======================================================
        # INTERSECTIONS
        # ======================================================

        for i, cercle1 in enumerate(
            self.cercles
        ):

            for cercle2 in self.cercles[i + 1:]:

                points = cercle_cercle(
                    cercle1,
                    cercle2
                )

                if points:

                    for point in points:

                        if not self.contient_point(
                            point
                        ):

                            self.intersections.append(
                                point
                            )

                            self.ajouter_point(
                                point
                            )

        # ======================================================
        # CLASSIFICATION
        # ======================================================

        self.classer_points()

    # ==========================================================
    # SÉLECTION DES 13 CERCLES
    # ==========================================================

    def _selectionner_13_cercles(
        self,
        cercles
    ):
        """
        Extrait les 13 cercles classiques du Fruit de Vie :

        - 1 centre ;
        - 6 à distance rayon ;
        - 6 à distance 2 × rayon.
        """

        tolerance = 1e-7

        centre = None

        premiere_couronne = []

        deuxieme_couronne = []

        for cercle in cercles:

            distance = (
                self.distance_centre(
                    cercle.centre
                )
            )

            # --------------------------------------------------
            # Cercle central
            # --------------------------------------------------

            if abs(distance) < tolerance:

                centre = cercle

            # --------------------------------------------------
            # Première couronne
            # --------------------------------------------------

            elif abs(
                distance - self.rayon
            ) < tolerance:

                premiere_couronne.append(
                    cercle
                )

            # --------------------------------------------------
            # Deuxième couronne
            # --------------------------------------------------

            elif abs(
                distance - 2 * self.rayon
            ) < tolerance:

                deuxieme_couronne.append(
                    cercle
                )

        # ======================================================
        # VALIDATION
        # ======================================================

        if centre is None:

            raise RuntimeError(
                "Impossible de trouver le cercle central."
            )

        if len(premiere_couronne) != 6:

            raise RuntimeError(
                "La première couronne du Fruit de Vie "
                f"doit contenir 6 cercles, obtenu : "
                f"{len(premiere_couronne)}"
            )

        if len(deuxieme_couronne) != 6:

            raise RuntimeError(
                "La deuxième couronne du Fruit de Vie "
                f"doit contenir 6 cercles, obtenu : "
                f"{len(deuxieme_couronne)}"
            )

        # ======================================================
        # ORDRE STABLE
        # ======================================================

        def angle(cercle):

            dx = (
                cercle.centre.x
                - self.centre.x
            )

            dy = (
                cercle.centre.y
                - self.centre.y
            )

            return math.atan2(
                dy,
                dx
            )

        premiere_couronne.sort(
            key=angle
        )

        deuxieme_couronne.sort(
            key=angle
        )

        return [
            centre,
            *premiere_couronne,
            *deuxieme_couronne
        ]

    # ==========================================================
    # TEST DE PRÉSENCE
    # ==========================================================

    def contient_point(
        self,
        point: Point,
        precision: float = 1e-9
    ):

        for p in self.intersections:

            if (
                abs(
                    p.x - point.x
                ) < precision
                and
                abs(
                    p.y - point.y
                ) < precision
            ):

                return True

        return False

    # ==========================================================
    # DISTANCE AU CENTRE
    # ==========================================================

    def distance_centre(
        self,
        point: Point
    ):

        dx = (
            point.x
            - self.centre.x
        )

        dy = (
            point.y
            - self.centre.y
        )

        return math.sqrt(
            dx ** 2
            + dy ** 2
        )

    # ==========================================================
    # CLASSIFICATION
    # ==========================================================

    def classer_points(self):

        """
        Classe les points remarquables
        selon leur distance au centre.
        """

        seuil_centre = (
            self.rayon * 0.5
        )

        seuil_exterieur = (
            self.rayon * 2
        )

        for point in self.points:

            distance = (
                self.distance_centre(
                    point
                )
            )

            if distance <= seuil_centre:

                self.points_centraux.append(
                    point
                )

            elif distance >= seuil_exterieur:

                self.points_exterieurs.append(
                    point
                )