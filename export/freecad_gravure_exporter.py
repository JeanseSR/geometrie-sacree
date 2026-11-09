from __future__ import annotations

from pathlib import Path


class FreeCADGravureExporter:
    """
    Exporte un modèle de fabrication avec gravure
    vers un script Python exécutable dans FreeCAD.

    Le fichier généré est autonome :
    il ne dépend ni de la bibliothèque Géométrie,
    ni de CubeMetatron, ni de ses classes.
    """

    def export(
        self,
        modele,
        fichier: str | Path,
    ) -> Path:

        fichier = Path(fichier)

        if modele.plaque is None:
            raise ValueError(
                "Une plaque est nécessaire pour une gravure."
            )

        if modele.gravure is None:
            raise ValueError(
                "Une opération de gravure est nécessaire."
            )

        contenu = self._generer_script(modele)

        fichier.write_text(
            contenu,
            encoding="utf-8"
        )

        return fichier

    # ==========================================================
    # SCRIPT FREECAD
    # ==========================================================

    def _generer_script(self, modele) -> str:

        plaque = modele.plaque
        profondeur = modele.gravure.profondeur

        boite = modele.figure.boite_englobante

        lignes = []

        lignes.append(
            "# ======================================================"
        )
        lignes.append(
            "# MODELE FREECAD — GRAVURE"
        )
        lignes.append(
            "# Généré automatiquement"
        )
        lignes.append(
            "# ======================================================"
        )
        lignes.append("")
        lignes.append("import FreeCAD as App")
        lignes.append("import Part")
        lignes.append("import math")
        lignes.append("")
        lignes.append(
            'doc = App.newDocument("Gravure")'
        )
        lignes.append("")

        # ======================================================
        # PARAMETRES
        # ======================================================

        lignes.append("# Paramètres")
        lignes.append(
            f"PLAQUE_LARGEUR = {plaque.largeur!r}"
        )
        lignes.append(
            f"PLAQUE_HAUTEUR = {plaque.hauteur!r}"
        )
        lignes.append(
            f"PLAQUE_EPAISSEUR = {plaque.epaisseur!r}"
        )
        lignes.append(
            f"PROFONDEUR_GRAVURE = {profondeur!r}"
        )
        lignes.append("")

        # ======================================================
        # PLAQUE
        # ======================================================

        lignes.append("# Plaque")
        lignes.append(
            "plaque = Part.makeBox("
        )
        lignes.append(
            "    PLAQUE_LARGEUR,"
        )
        lignes.append(
            "    PLAQUE_HAUTEUR,"
        )
        lignes.append(
            "    PLAQUE_EPAISSEUR,"
        )
        lignes.append(
            "    App.Vector("
        )
        lignes.append(
            "        -PLAQUE_LARGEUR / 2,"
        )
        lignes.append(
            "        -PLAQUE_HAUTEUR / 2,"
        )
        lignes.append(
            "        0"
        )
        lignes.append(
            "    )"
        )
        lignes.append(")")
        lignes.append("")

        # ======================================================
        # OUTILS DE GRAVURE
        # ======================================================

        lignes.append("# Outils de gravure")
        lignes.append("outils = []")
        lignes.append("")

        # ======================================================
        # COURONNES
        # ======================================================

        for couronne in modele.figure.couronnes_geometriques:

            cx = couronne.centre.x
            cy = couronne.centre.y

            ri = couronne.rayon_interieur
            re = couronne.rayon_exterieur

            lignes.append(
                "# Couronne"
            )

            lignes.append(
                f"centre = App.Vector({cx!r}, {cy!r}, "
                f"PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)"
            )

            lignes.append(
                f"exterieur = Part.makeCylinder("
                f"{re!r}, PROFONDEUR_GRAVURE, centre)"
            )

            lignes.append(
                f"interieur = Part.makeCylinder("
                f"{ri!r}, PROFONDEUR_GRAVURE, centre)"
            )

            lignes.append(
                "outil = exterieur.cut(interieur)"
            )

            lignes.append(
                "outils.append(outil)"
            )

            lignes.append("")

        # ======================================================
        # BANDES DE SEGMENTS
        # ======================================================

        for bande in modele.figure.bandes_segments:

            x1 = bande.debut.x
            y1 = bande.debut.y

            x2 = bande.fin.x
            y2 = bande.fin.y

            largeur = bande.largeur

            lignes.append(
                "# Bande de segment"
            )

            lignes.append(
                f"x1 = {x1!r}"
            )
            lignes.append(
                f"y1 = {y1!r}"
            )
            lignes.append(
                f"x2 = {x2!r}"
            )
            lignes.append(
                f"y2 = {y2!r}"
            )
            lignes.append(
                f"largeur = {largeur!r}"
            )

            lignes.append(
                "dx = x2 - x1"
            )
            lignes.append(
                "dy = y2 - y1"
            )
            lignes.append(
                "longueur = math.hypot(dx, dy)"
            )
            lignes.append(
                "angle = math.degrees(math.atan2(dy, dx))"
            )

            # Rectangle central du trait
            lignes.append(
                "rectangle = Part.makeBox("
            )
            lignes.append(
                "    longueur,"
            )
            lignes.append(
                "    largeur,"
            )
            lignes.append(
                "    PROFONDEUR_GRAVURE,"
            )
            lignes.append(
                "    App.Vector("
            )
            lignes.append(
                "        0,"
            )
            lignes.append(
                "        -largeur / 2,"
            )
            lignes.append(
                "        PLAQUE_EPAISSEUR "
                "- PROFONDEUR_GRAVURE"
            )
            lignes.append(
                "    )"
            )
            lignes.append(")")

            lignes.append(
                "rectangle.rotate("
            )
            lignes.append(
                "    App.Vector(0, 0, 0),"
            )
            lignes.append(
                "    App.Vector(0, 0, 1),"
            )
            lignes.append(
                "    angle"
            )
            lignes.append(
                ")"
            )

            lignes.append(
                "rectangle.translate("
            )
            lignes.append(
                f"    App.Vector({x1!r}, {y1!r}, 0)"
            )
            lignes.append(
                ")"
            )

            # Extrémité 1
            lignes.append(
                "r = largeur / 2"
            )

            lignes.append(
                "bout1 = Part.makeCylinder("
            )
            lignes.append(
                "    r,"
            )
            lignes.append(
                "    PROFONDEUR_GRAVURE,"
            )
            lignes.append(
                "    App.Vector("
            )
            lignes.append(
                "        x1,"
            )
            lignes.append(
                "        y1,"
            )
            lignes.append(
                "        PLAQUE_EPAISSEUR "
                "- PROFONDEUR_GRAVURE"
            )
            lignes.append(
                "    )"
            )
            lignes.append(
                ")"
            )

            # Extrémité 2
            lignes.append(
                "bout2 = Part.makeCylinder("
            )
            lignes.append(
                "    r,"
            )
            lignes.append(
                "    PROFONDEUR_GRAVURE,"
            )
            lignes.append(
                "    App.Vector("
            )
            lignes.append(
                "        x2,"
            )
            lignes.append(
                "        y2,"
            )
            lignes.append(
                "        PLAQUE_EPAISSEUR "
                "- PROFONDEUR_GRAVURE"
            )
            lignes.append(
                "    )"
            )
            lignes.append(
                ")"
            )

            lignes.append(
                "outil = rectangle.fuse(bout1).fuse(bout2)"
            )

            lignes.append(
                "outils.append(outil)"
            )

            lignes.append("")

        # ======================================================
        # UNION DES OUTILS
        # ======================================================

        lignes.append(
            "# Union des outils de gravure"
        )
        lignes.append(
            "outil_total = None"
        )
        lignes.append("")

        lignes.append(
            "for outil in outils:"
        )
        lignes.append(
            "    if outil_total is None:"
        )
        lignes.append(
            "        outil_total = outil"
        )
        lignes.append(
            "    else:"
        )
        lignes.append(
            "        outil_total = "
            "outil_total.fuse(outil)"
        )

        lignes.append("")

        # ======================================================
        # SOUSTRACTION
        # ======================================================

        lignes.append(
            "# Gravure dans la plaque"
        )
        lignes.append(
            "resultat = plaque.cut(outil_total)"
        )
        lignes.append("")

        # ======================================================
        # OBJET FINAL
        # ======================================================

        lignes.append(
            'objet = doc.addObject("PartDesign::Feature", '
            '"MetatronGrave")'
        )
        lignes.append(
            "objet.Label = "
            '"Cube de Métatron — gravure"'
        )
        lignes.append(
            "objet.Shape = resultat"
        )
        lignes.append("")

        # ======================================================
        # OBJET PLAQUE OPTIONNEL
        # ======================================================

        lignes.append(
            'info = doc.addObject("App::FeaturePython", '
            '"Informations")'
        )

        lignes.append(
            'info.addProperty("App::PropertyString", '
            '"Type", "Fabrication")'
        )
        lignes.append(
            'info.Type = "Cube de Métatron gravé"'
        )

        lignes.append(
            'info.addProperty("App::PropertyLength", '
            '"ProfondeurGravure", "Fabrication")'
        )
        lignes.append(
            "info.ProfondeurGravure = "
            "PROFONDEUR_GRAVURE"
        )

        lignes.append(
            'info.addProperty("App::PropertyLength", '
            '"LargeurPlaque", "Fabrication")'
        )
        lignes.append(
            "info.LargeurPlaque = PLAQUE_LARGEUR"
        )

        lignes.append(
            'info.addProperty("App::PropertyLength", '
            '"HauteurPlaque", "Fabrication")'
        )
        lignes.append(
            "info.HauteurPlaque = PLAQUE_HAUTEUR"
        )

        lignes.append("")

        # ======================================================
        # VUE
        # ======================================================

        lignes.append(
            "objet.ViewObject.ShapeColor = "
            "(0.82, 0.82, 0.82)"
        )
        lignes.append(
            "objet.ViewObject.LineColor = "
            "(0.15, 0.15, 0.15)"
        )

        lignes.append("")

        lignes.append(
            "doc.recompute()"
        )

        lignes.append(
            "Gui.activeDocument().activeView()"
            ".viewAxonometric()"
        )

        lignes.append(
            "Gui.activeDocument().activeView()"
            ".fitAll()"
        )

        lignes.append("")

        lignes.append(
            "# Pour enregistrer directement :"
        )
        lignes.append(
            '# doc.saveAs("metatron_gravure.FCStd")'
        )

        return "\n".join(lignes) + "\n"