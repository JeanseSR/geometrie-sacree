from __future__ import annotations

from export.exporter import Exporter
from export.writers.freecad_sketch_writer import FreeCADSketchWriter


class FreeCADCodeExporter(Exporter):

    def __init__(self):

        self.writer = FreeCADSketchWriter()

    def export(
        self,
        figure,
        fichier
    ):

        self.writer.begin()

        super().export(figure)

        self.writer.end()

        self.writer.save(fichier)

    def export_point(self, point):

        self.writer.point(point)

    def export_segment(self, segment):

        self.writer.segment(segment)

    def export_cercle(self, cercle):

        self.writer.cercle(cercle)

    def export_polygone(self, polygone):

        self.writer.polygone(polygone)
    
    def export_couronne(self, couronne):

        self.writer.couronne(couronne)
