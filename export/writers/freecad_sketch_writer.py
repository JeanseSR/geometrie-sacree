from __future__ import annotations


class FreeCADSketchWriter:
    """
    Génère un script Python créant une esquisse Sketcher.
    """

    def __init__(self):

        self.lines: list[str] = []

    # ==========================================================
    # DOCUMENT
    # ==========================================================

    def begin(self):

        self.lines.extend([

            "import FreeCAD as App",
            "import FreeCADGui as Gui",
            "import Part",
            "import Sketcher",
            "",

            'doc = App.newDocument("GeometrieSacree")',

            "",

            'sketch = doc.addObject(',
            '    "Sketcher::SketchObject",',
            '    "Esquisse"',
            ")",

            ""
        ])

    # ==========================================================
    # POINT
    # ==========================================================

    def point(self, point):
        pass

    # ==========================================================
    # SEGMENT
    # ==========================================================

    def segment(self, segment):

        self.lines.extend([

            "sketch.addGeometry(",

            "    Part.LineSegment(",

            f"        App.Vector({segment.debut.x}, {segment.debut.y}, 0),",

            f"        App.Vector({segment.fin.x}, {segment.fin.y}, 0)",

            "    ),",

            "    False",

            ")",

            ""

        ])

    # ==========================================================
    # CERCLE
    # ==========================================================

    def cercle(self, cercle):

        self.lines.extend([

            "sketch.addGeometry(",

            "    Part.Circle(",

            f"        App.Vector({cercle.centre.x}, {cercle.centre.y}, 0),",

            "        App.Vector(0,0,1),",

            f"        {cercle.rayon}",

            "    ),",

            "    False",

            ")",

            ""

        ])

    # ==========================================================
    # POLYGONE
    # ==========================================================

    def polygone(self, polygone):

        # CORRECTION étape 1 : `points` -> `sommets`
        pts = polygone.sommets

        for i in range(len(pts)):

            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]

            self.lines.extend([

                "sketch.addGeometry(",

                "    Part.LineSegment(",

                f"        App.Vector({p1.x}, {p1.y}, 0),",

                f"        App.Vector({p2.x}, {p2.y}, 0)",

                "    ),",

                "    False",

                ")",

                ""

            ])

    # ==========================================================
    # COURONNE
    # ==========================================================

    def couronne(self, couronne):

        self.cercle(
            couronne.cercle_exterieur
        )

        self.cercle(
            couronne.cercle_interieur
        )

    # ==========================================================
    # FIN
    # ==========================================================

    def end(self):

        self.lines.extend([

            "",

            "doc.recompute()",

            "Gui.ActiveDocument.ActiveView.fitAll()",

            'Gui.SendMsgToActiveView("ViewFit")',

            ""

        ])

    # ==========================================================
    # SAUVEGARDE
    # ==========================================================

    def save(self, fichier):

        with open(
            fichier,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("\n".join(self.lines))