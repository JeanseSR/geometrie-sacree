from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.cercle import Cercle as CercleGeo
from geometrie.polygone import Polygone
from figures.figure import Figure


class Afficheur:

    def __init__(self):

        self.fig, self.ax = plt.subplots()

        self.ax.set_aspect("equal")

        self.ax.grid(True, linestyle="--", alpha=0.3)

    # -------------------------------------------------

    def point(self, point: Point,
              couleur="black",
              taille=25):

        self.ax.scatter(
            point.x,
            point.y,
            s=taille,
            color=couleur,
            zorder=5
        )

    # -------------------------------------------------

    def segment(self,
                segment: Segment,
                couleur="black",
                epaisseur=1.5):

        self.ax.plot(
            [segment.debut.x, segment.fin.x],
            [segment.debut.y, segment.fin.y],
            color=couleur,
            linewidth=epaisseur
        )

    # -------------------------------------------------

    def cercle(self,
                cercle: CercleGeo,
                couleur="black",
                epaisseur=1.5):

        patch = Circle(
            (cercle.centre.x, cercle.centre.y),
            cercle.rayon,
            fill=False,
            linewidth=epaisseur,
            edgecolor=couleur
        )

        self.ax.add_patch(patch)

    # -------------------------------------------------

    def polygone(self,
                 polygone: Polygone,
                 couleur="black",
                 epaisseur=1.5):

        x = [p.x for p in polygone.sommets]
        y = [p.y for p in polygone.sommets]

        x.append(polygone.sommets[0].x)
        y.append(polygone.sommets[0].y)

        self.ax.plot(
            x,
            y,
            color=couleur,
            linewidth=epaisseur
        )

    # -------------------------------------------------

    def figure(self,
               figure: Figure):

        for cercle in figure.cercles:
            self.cercle(cercle)

        for segment in figure.segments:
            self.segment(segment)

        for polygone in figure.polygones:
            self.polygone(polygone)

        for point in figure.points:
            self.point(point)

    # -------------------------------------------------

    def afficher(self,
                 titre="Géométrie"):

        self.ax.set_title(titre)

        self.ax.autoscale()

        plt.show()



# TODO V2
#
# - Styles de rendu
# - Couleurs
# - Épaisseur par défaut
# - Affichage des centres
# - Affichage des intersections
# - Affichage des axes
# - Affichage de la grille
# - Export PNG
# - Zoom automatique
# - Calques