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

# from __future__ import annotations

# from export.exporter import Exporter


# class FreeCADCodeExporter(Exporter):
#     """
#     Génère un script Python destiné à FreeCAD.

#     Les objets géométriques sont convertis en objets Draft.
#     """

#     def __init__(self):
#         self.lignes = []

#     # ==========================================================
#     # EXPORT
#     # ==========================================================

#     def export(
#         self,
#         figure,
#         fichier
#     ):
#         self.lignes = []

#         self.lignes.append(
#             "import FreeCAD as App"
#         )

#         self.lignes.append(
#             "import Draft"
#         )

#         self.lignes.append("")
#         self.lignes.append(
#             'doc = App.newDocument("Gravure")'
#         )

#         # Moteur générique
#         super().export(figure)

#         self.lignes.append("")
#         self.lignes.append(
#             "doc.recompute()"
#         )

#         self.lignes.append(
#             "Gui.activeDocument().activeView().viewTop()"
#         )

#         self.lignes.append(
#             "Gui.activeDocument().activeView().fitAll()"
#         )

#         with open(
#             fichier,
#             "w",
#             encoding="utf-8"
#         ) as f:

#             f.write(
#                 "\n".join(self.lignes)
#             )

#     # ==========================================================
#     # POINT
#     # ==========================================================

#     def export_point(
#         self,
#         point
#     ):

#         self.lignes.append(
#             f'Draft.makePoint('
#             f'{point.x}, '
#             f'{point.y}, '
#             f'0'
#             f')'
#         )

#     # ==========================================================
#     # SEGMENT
#     # ==========================================================

#     def export_segment(
#         self,
#         segment
#     ):

#         self.lignes.append(
#             "Draft.make_line("
#         )

#         self.lignes.append(
#             f"    App.Vector("
#             f"{segment.debut.x}, "
#             f"{segment.debut.y}, "
#             f"0"
#             f"),"
#         )

#         self.lignes.append(
#             f"    App.Vector("
#             f"{segment.fin.x}, "
#             f"{segment.fin.y}, "
#             f"0"
#             f")"
#         )

#         self.lignes.append(
#             ")"
#         )

#     # ==========================================================
#     # CERCLE
#     # ==========================================================

#     def export_cercle(
#         self,
#         cercle
#     ):

#         self.lignes.append(
#             "Draft.makeCircle("
#         )

#         self.lignes.append(
#             f"    radius={cercle.rayon},"
#         )

#         self.lignes.append(
#             "    placement=App.Placement("
#         )

#         self.lignes.append(
#             f"        App.Vector("
#             f"{cercle.centre.x}, "
#             f"{cercle.centre.y}, "
#             f"0"
#             f"),"
#         )

#         self.lignes.append(
#             "        App.Rotation()"
#         )

#         self.lignes.append(
#             "    )"
#         )

#         self.lignes.append(
#             ")"
#         )

#     # ==========================================================
#     # COURONNE
#     # ==========================================================

#     def export_couronne(
#         self,
#         couronne
#     ):
#         """
#         Exporte une couronne sous forme de deux
#         cercles concentriques.

#         Le cercle extérieur définit le diamètre
#         extérieur.

#         Le cercle intérieur définit le vide
#         central de la couronne.
#         """

#         self.export_cercle(
#             couronne.cercle_exterieur
#         )

#         self.export_cercle(
#             couronne.cercle_interieur
#         )

#     # ==========================================================
#     # POLYGONE
#     # ==========================================================

#     def export_polygone(
#         self,
#         polygone
#     ):

#         for segment in polygone.segments:

#             self.export_segment(
#                 segment
#             )
