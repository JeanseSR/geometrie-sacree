from __future__ import annotations

from pathlib import Path


class FreeCADPartExporter:
    """
    Exporte un modèle de fabrication sous forme
    de script Python exécutable dans FreeCAD.

    Le script généré crée :

    - une plaque rectangulaire ;
    - les volumes correspondant aux traits ;
    - une soustraction de ces volumes dans la plaque.

    Le résultat est donc une vraie géométrie 3D.
    """

    def export(
        self,
        modele,
        fichier: str | Path,
    ) -> Path:
        """
        Génère un script FreeCAD à partir d'un modèle
        de fabrication.
        """

        if modele.plaque is None:
            raise ValueError(
                "Un support plaque est nécessaire "
                "pour créer une pièce 3D."
            )

        if modele.gravure is None:
            raise ValueError(
                "Une opération de gravure est nécessaire."
            )

        plaque = modele.plaque
        profondeur = modele.gravure.profondeur

        if profondeur > plaque.epaisseur:
            raise ValueError(
                "La profondeur de gravure dépasse "
                "l'épaisseur de la plaque."
            )

        couronnes = (
            modele.figure.couronnes_geometriques
        )

        chemin = Path(fichier)

        script = self._generer_script(
            plaque=plaque,
            couronnes=couronnes,
            profondeur=profondeur,
        )

        chemin.write_text(
            script,
            encoding="utf-8",
        )

        return chemin

    # ==========================================================
    # GENERATION DU SCRIPT
    # ==========================================================

    def _generer_script(
        self,
        *,
        plaque,
        couronnes,
        profondeur,
    ) -> str:

        lignes = []

        lignes.append(
            "import FreeCAD as App"
        )

        lignes.append(
            "import Part"
        )

        lignes.append("")

        lignes.append(
            "doc = App.newDocument("
            "'FleurDeVieGravure'"
            ")"
        )

        lignes.append("")

        # ======================================================
        # PLAQUE
        # ======================================================

        x = -plaque.largeur / 2
        y = -plaque.hauteur / 2

        lignes.append(
            "# ================================================"
        )

        lignes.append(
            "# PLAQUE"
        )

        lignes.append(
            "# ================================================"
        )

        lignes.append("")

        lignes.append(
            f"plaque = Part.makeBox("
            f"{plaque.largeur}, "
            f"{plaque.hauteur}, "
            f"{plaque.epaisseur}, "
            f"App.Vector({x}, {y}, 0)"
            ")"
        )

        lignes.append("")

        # ======================================================
        # VOLUMES DE GRAVURE
        # ======================================================

        lignes.append(
            "# ================================================"
        )

        lignes.append(
            "# VOLUMES DE GRAVURE"
        )

        lignes.append(
            "# ================================================"
        )

        lignes.append("")

        lignes.append(
            "outils = []"
        )

        lignes.append("")

        # La gravure part de la face supérieure.
        z = plaque.epaisseur - profondeur

        for index, couronne in enumerate(couronnes):

            cx = couronne.centre.x
            cy = couronne.centre.y

            rayon_interieur = (
                couronne.rayon_interieur
            )

            rayon_exterieur = (
                couronne.rayon_exterieur
            )

            lignes.append(
                f"# Couronne {index + 1}"
            )

            lignes.append(
                f"centre_{index} = "
                f"App.Vector({cx}, {cy}, {z})"
            )

            lignes.append(
                f"exterieur_{index} = "
                f"Part.makeCylinder("
                f"{rayon_exterieur}, "
                f"{profondeur}, "
                f"centre_{index}"
                ")"
            )

            lignes.append(
                f"interieur_{index} = "
                f"Part.makeCylinder("
                f"{rayon_interieur}, "
                f"{profondeur}, "
                f"centre_{index}"
                ")"
            )

            lignes.append(
                f"anneau_{index} = "
                f"exterieur_{index}.cut("
                f"interieur_{index}"
                ")"
            )

            lignes.append(
                f"outils.append("
                f"anneau_{index}"
                ")"
            )

            lignes.append("")

        # ======================================================
        # FUSION DES OUTILS
        # ======================================================

        lignes.append(
            "# ================================================"
        )

        lignes.append(
            "# FUSION DES VOLUMES DE GRAVURE"
        )

        lignes.append(
            "# ================================================"
        )

        lignes.append("")

        lignes.append(
            "outil_gravure = outils[0]"
        )

        lignes.append("")

        lignes.append(
            "for outil in outils[1:]:"
        )

        lignes.append(
            "    outil_gravure = "
            "outil_gravure.fuse(outil)"
        )

        lignes.append("")

        # ======================================================
        # SOUSTRACTION
        # ======================================================

        lignes.append(
            "# ================================================"
        )

        lignes.append(
            "# GRAVURE"
        )

        lignes.append(
            "# ================================================"
        )

        lignes.append("")

        lignes.append(
            "resultat = plaque.cut("
            "outil_gravure"
            ")"
        )

        lignes.append("")

        # ======================================================
        # OBJET FREECAD
        # ======================================================

        lignes.append(
            "objet = doc.addObject("
            "'PartDesign::Feature', "
            "'FleurDeVieGravee'"
            ")"
        )

        lignes.append(
            "objet.Label = "
            "'Fleur de Vie gravée'"
        )

        lignes.append(
            "objet.Shape = resultat"
        )

        lignes.append("")

        # ======================================================
        # INFORMATIONS
        # ======================================================

        lignes.append(
            "objet.addProperty("
            "'App::PropertyString', "
            "'Fabrication', "
            "'Paramètres'"
            ")"
        )

        lignes.append(
            "objet.Fabrication = "
            "'Fleur de Vie - gravure'"
        )

        lignes.append(
            "objet.addProperty("
            "'App::PropertyLength', "
            "'ProfondeurGravure', "
            "'Paramètres'"
            ")"
        )

        lignes.append(
            f"objet.ProfondeurGravure = "
            f"{profondeur}"
        )

        lignes.append("")

        lignes.append(
            "objet.addProperty("
            "'App::PropertyLength', "
            "'LargeurPlaque', "
            "'Paramètres'"
            ")"
        )

        lignes.append(
            f"objet.LargeurPlaque = "
            f"{plaque.largeur}"
        )

        lignes.append("")

        lignes.append(
            "objet.addProperty("
            "'App::PropertyLength', "
            "'HauteurPlaque', "
            "'Paramètres'"
            ")"
        )

        lignes.append(
            f"objet.HauteurPlaque = "
            f"{plaque.hauteur}"
        )

        lignes.append("")

        lignes.append(
            "objet.addProperty("
            "'App::PropertyLength', "
            "'EpaisseurPlaque', "
            "'Paramètres'"
            ")"
        )

        lignes.append(
            f"objet.EpaisseurPlaque = "
            f"{plaque.epaisseur}"
        )

        lignes.append("")

        # ======================================================
        # AFFICHAGE
        # ======================================================

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
            "print("
            "'Fleur de Vie gravée créée : OK'"
            ")"
        )

        lignes.append("")

        return "\n".join(lignes)