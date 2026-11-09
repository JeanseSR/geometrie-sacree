from __future__ import annotations

from export.exporter import Exporter
from export.writers.svg_writer import SVGWriter


class SVGExporter(Exporter):
    """
    Export d'une Figure au format SVG.
    """

    def __init__(
        self,
        marge: float = 5
    ):

        self.marge = marge
        self.writer = None

    # ==========================================================
    # EXPORT
    # ==========================================================

    def export(
        self,
        figure,
        fichier
    ):

        boite = figure.boite_englobante.marge(
            self.marge
        )

        self.writer = SVGWriter(
            boite
        )

        self.writer.begin()

        # Le moteur d'export ne prend que la figure
        super().export(
            figure
        )

        self.writer.end()

        self.writer.save(
            fichier
        )

    # ==========================================================
    # EXPORT DES OBJETS
    # ==========================================================

    def export_point(
        self,
        point
    ):

        self.writer.point(point)

    def export_segment(
        self,
        segment
    ):

        self.writer.segment(segment)

    def export_cercle(
        self,
        cercle
    ):

        self.writer.cercle(cercle)

    def export_polygone(
        self,
        polygone
    ):

        self.writer.polygone(polygone)

    def export_couronne(
        self,
        couronne
    ):

        self.writer.cercle(
            couronne.cercle_exterieur
        )

        self.writer.cercle(
            couronne.cercle_interieur
        )
