from __future__ import annotations


class FreeCADWriter:
    """
    Génère un script Python exécutable dans FreeCAD.
    """

    def __init__(self):

        self.lignes: list[str] = []

    # ==========================================================
    # DOCUMENT
    # ==========================================================

    def begin(self):

        self.lignes.extend([
            "import FreeCAD as App",
            "import Draft",
            "",
            'doc = App.newDocument("GeometrieSacree")',
            ""
        ])

    def end(self):

        self.lignes.extend([
            "",
            "doc.recompute()",
            'App.ActiveDocument.recompute()',
            'print("Figure créée.")'
        ])

    # ==========================================================
    # OBJETS
    # ==========================================================

    def point(self, point):

        self.lignes.append(
            f"# Point ({point.x}, {point.y})"
        )

    def segment(self, segment):

        self.lignes.append(

            "Draft.makeLine("
            f"App.Vector({segment.debut.x}, {segment.debut.y}, 0), "
            f"App.Vector({segment.fin.x}, {segment.fin.y}, 0)"
            ")"

        )

    def cercle(self, cercle):

        self.lignes.append(

            "Draft.makeCircle("
            f"radius={cercle.rayon}, "
            f"placement=App.Placement("
            f"App.Vector({cercle.centre.x}, {cercle.centre.y}, 0), "
            "App.Rotation())"
            ")"

        )

    def polygone(self, polygone):

        self.lignes.append("points = [")

        # CORRECTION étape 1 : `points` -> `sommets`
        for p in polygone.sommets:

            self.lignes.append(
                f"    App.Vector({p.x}, {p.y}, 0),"
            )

        self.lignes.append("]")

        self.lignes.append(
            "Draft.makeWire(points, closed=True)"
        )

        self.lignes.append("")

    # ==========================================================
    # SAUVEGARDE
    # ==========================================================

    def save(
        self,
        fichier
    ):

        with open(
            fichier,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("\n".join(self.lignes))