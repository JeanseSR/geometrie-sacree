from __future__ import annotations

import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from matplotlib.patches import Polygon

from export.exporter import Exporter

from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.polygone import Polygone


class MatplotlibExporter(Exporter):
    """
    Exporteur Matplotlib.

    Permet :
        - d'afficher une figure
        - de sauvegarder une image PNG
    """

    def __init__(self):

        self.fig = None
        self.ax = None

        self.nom_fichier = None

    # ======================================================

    def export(
        self,
        figure,
        nom_fichier: str | None = None
    ):

        self.nom_fichier = nom_fichier

        super().export(figure)

    # ======================================================

    def debut_export(self, figure):

        self.fig, self.ax = plt.subplots()

        self.ax.set_aspect("equal")

        self.ax.grid(True)

    # ======================================================

    def export_point(self, point: Point):

        self.ax.plot(
            point.x,
            point.y,
            "ko",
            markersize=4
        )

    # ======================================================

    def export_segment(self, segment: Segment):

        self.ax.plot(
            [segment.debut.x, segment.fin.x],
            [segment.debut.y, segment.fin.y]
        )

    # ======================================================

    def export_cercle(self, cercle: Cercle):

        patch = Circle(

            (cercle.centre.x, cercle.centre.y),

            cercle.rayon,

            fill=False

        )

        self.ax.add_patch(patch)

    # ======================================================

    def export_polygone(self, polygone: Polygone):

        patch = Polygon(

            # CORRECTION étape 1 : `points` -> `sommets`
            [(p.x, p.y) for p in polygone.sommets],

            closed=True,

            fill=False

        )

        self.ax.add_patch(patch)

    # ======================================================

    # CORRECTION étape 1 : méthode manquante.
    # `export_couronne` est déclarée @abstractmethod dans Exporter :
    # sans elle, `MatplotlibExporter()` lève
    # "Can't instantiate abstract class".
    # Une couronne est dessinée comme ses deux cercles
    # (extérieur + intérieur), comme dans SVGExporter.
    def export_couronne(self, couronne):

        self.export_cercle(couronne.cercle_exterieur)

        self.export_cercle(couronne.cercle_interieur)

    # ======================================================

    def fin_export(self, figure):

        self.ax.relim()

        self.ax.autoscale_view()

        if self.nom_fichier is None:

            plt.show()

        else:

            plt.savefig(
                self.nom_fichier,
                dpi=300,
                bbox_inches="tight"
            )

            plt.close(self.fig)