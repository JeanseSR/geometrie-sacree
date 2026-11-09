from __future__ import annotations

from export.exporter import Exporter
from export.writers.freecad_sketch_writer import FreeCADSketchWriter


class FreeCADCodeExporter(Exporter):

    def __init__(self):

        self.writer = None

    def export(
        self,
        figure,
        fichier
    ):

        # CORRECTION étape 3 : le writer est recréé à CHAQUE export.
        # Avant, il était créé une seule fois dans __init__ et sa
        # liste de lignes n'était jamais vidée : exporter deux fois
        # avec le même exporteur écrivait deux scripts à la suite
        # dans le second fichier.
        self.writer = FreeCADSketchWriter()

        self.writer.begin()

        super().export(figure)

        self.writer.end()

        self.writer.save(fichier)

    # MODIFICATION étape 3 : chaque méthode transmet au writer
    # `self.construction` (rempli par Exporter.export) pour que
    # le Sketch affiche les traits de construction en bleu pointillé.

    def export_point(self, point):

        self.writer.point(point)

    def export_segment(self, segment):

        self.writer.segment(segment, self.construction)

    def export_cercle(self, cercle):

        self.writer.cercle(cercle, self.construction)

    def export_polygone(self, polygone):

        self.writer.polygone(polygone, self.construction)

    def export_couronne(self, couronne):

        self.writer.couronne(couronne, self.construction)
