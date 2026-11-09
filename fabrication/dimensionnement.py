from __future__ import annotations

from dataclasses import dataclass
from geometrie.point import Point


@dataclass(frozen=True)
class Dimensionnement:
    """
    Calcule les dimensions disponibles sur un support
    existant et le facteur d'échelle nécessaire pour
    y faire tenir une figure.

    Le support n'est jamais créé ni modifié.
    """

    largeur_support: float
    hauteur_support: float

    marge: float = 1.0

    def __post_init__(self):

        if self.largeur_support <= 0:
            raise ValueError(
                "La largeur du support doit être positive."
            )

        if self.hauteur_support <= 0:
            raise ValueError(
                "La hauteur du support doit être positive."
            )

        if self.marge < 0:
            raise ValueError(
                "La marge ne peut pas être négative."
            )

        if (
            2 * self.marge
            >= self.largeur_support
        ):
            raise ValueError(
                "La marge est trop grande "
                "pour la largeur du support."
            )

        if (
            2 * self.marge
            >= self.hauteur_support
        ):
            raise ValueError(
                "La marge est trop grande "
                "pour la hauteur du support."
            )

    # ==========================================================
    # ZONE DISPONIBLE
    # ==========================================================

    @property
    def largeur_disponible(self) -> float:

        return (
            self.largeur_support
            - 2 * self.marge
        )

    @property
    def hauteur_disponible(self) -> float:

        return (
            self.hauteur_support
            - 2 * self.marge
        )

    # ==========================================================
    # FACTEUR D'ÉCHELLE
    # ==========================================================

    def facteur_echelle(
        self,
        largeur_figure: float,
        hauteur_figure: float
    ) -> float:
        """
        Retourne le facteur d'échelle maximal permettant
        à la figure de rentrer dans la zone disponible.

        Le rapport largeur/hauteur est conservé.
        """

        if largeur_figure <= 0:
            raise ValueError(
                "La largeur de la figure doit être positive."
            )

        if hauteur_figure <= 0:
            raise ValueError(
                "La hauteur de la figure doit être positive."
            )

        facteur_largeur = (
            self.largeur_disponible
            / largeur_figure
        )

        facteur_hauteur = (
            self.hauteur_disponible
            / hauteur_figure
        )

        return min(
            facteur_largeur,
            facteur_hauteur
        )

    # ==========================================================
    # DIMENSIONS FINALES
    # ==========================================================

    def dimensions_finales(
        self,
        largeur_figure: float,
        hauteur_figure: float
    ) -> tuple[float, float]:
        """
        Retourne les dimensions de la figure après
        mise à l'échelle.
        """

        facteur = self.facteur_echelle(
            largeur_figure,
            hauteur_figure
        )

        return (
            largeur_figure * facteur,
            hauteur_figure * facteur
        )

# ==========================================================
# CENTRAGE
# ==========================================================

    def translation_centrage(
        self,
        boite
    ) -> tuple[float, float]:
        """
        Calcule la translation nécessaire pour centrer
        une figure sur l'origine du support.

        Le support est supposé centré sur (0, 0).
        """

        centre_figure_x = (
            boite.xmin + boite.xmax
        ) / 2

        centre_figure_y = (
            boite.ymin + boite.ymax
        ) / 2

        dx = -centre_figure_x
        dy = -centre_figure_y

        return dx, dy

    # ==========================================================
    # APPLICATION COMPLÈTE
    # ==========================================================

    def appliquer(
        self,
        figure
    ):
        """
        Adapte une figure au support :

        1. calcule le facteur d'échelle ;
        2. réduit ou agrandit la figure ;
        3. la centre sur le support ;
        4. conserve la marge définie.

        La figure originale n'est jamais modifiée.
        """

        # ------------------------------------------------------
        # 1. Boîte originale
        # ------------------------------------------------------

        boite = figure.boite_englobante

        # ------------------------------------------------------
        # 2. Facteur d'échelle
        # ------------------------------------------------------

        facteur = self.facteur_echelle(
            boite.largeur,
            boite.hauteur
        )

        # ------------------------------------------------------
        # 3. Mise à l'échelle autour de l'origine
        # ------------------------------------------------------

        figure_adaptee = figure.echelle_autour(
            Point(0, 0),
            facteur
        )

        # ------------------------------------------------------
        # 4. Boîte après mise à l'échelle
        # ------------------------------------------------------

        boite = (
            figure_adaptee.boite_englobante
        )

        # ------------------------------------------------------
        # 5. Calcul du centrage
        # ------------------------------------------------------

        dx, dy = self.translation_centrage(
            boite
        )

        # ------------------------------------------------------
        # 6. Translation
        # ------------------------------------------------------

        figure_adaptee = (
            figure_adaptee.translation(
                dx,
                dy
            )
        )

        return figure_adaptee