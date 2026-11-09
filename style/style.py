from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Style:
    """
    Définit le style graphique d'un objet géométrique.

    Cette classe est indépendante des moteurs de rendu
    (Matplotlib, SVG, DXF, FreeCAD...).

    Chaque exporteur traduit ensuite ces propriétés
    dans son propre langage.
    """

    # ==========================================================
    # VISIBILITÉ
    # ==========================================================

    visible: bool = True

    # ==========================================================
    # COULEURS
    # ==========================================================

    couleur: str = "#000000"

    couleur_remplissage: str | None = None

    alpha: float = 1.0

    # ==========================================================
    # TRAIT
    # ==========================================================

    epaisseur: float = 1.0

    pointille: bool = False

    # ----------------------------------------------------------

    style_trait: str = "solid"
    """
    solid
    dashed
    dotted
    dashdot
    """

    # ==========================================================
    # REMPLISSAGE
    # ==========================================================

    remplir: bool = False

    # ==========================================================
    # CALQUES
    # ==========================================================

    calque: str = "0"

    # ==========================================================
    # NOM
    # ==========================================================

    nom: str = ""

    # ==========================================================
    # COPIE
    # ==========================================================

    def copie(self) -> "Style":
        """
        Retourne une copie indépendante du style.
        """

        return Style(

            visible=self.visible,

            couleur=self.couleur,

            couleur_remplissage=self.couleur_remplissage,

            alpha=self.alpha,

            epaisseur=self.epaisseur,

            pointille=self.pointille,

            style_trait=self.style_trait,

            remplir=self.remplir,

            calque=self.calque,

            nom=self.nom

        )

    # ==========================================================

    @property
    def matplotlib_linestyle(self) -> str:
        """
        Conversion vers Matplotlib.
        """

        if self.pointille:
            return "--"

        return self.style_trait

    # ==========================================================

    @property
    def svg_dasharray(self) -> str | None:
        """
        Conversion vers SVG.
        """

        if self.pointille:
            return "5,5"

        return None

    # ==========================================================

    def __repr__(self):

        return (

            "Style("

            f"couleur='{self.couleur}', "

            f"epaisseur={self.epaisseur}, "

            f"visible={self.visible}"

            ")"

        )