from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from figures.figure import Figure
from fabrication.plaque import Plaque
from fabrication.gravure import Gravure


@dataclass(frozen=True)
class Modelisation:
    """
    Modèle complet d'une fabrication.

    Cette classe rassemble :

    - une figure géométrique ;
    - éventuellement une plaque support ;
    - éventuellement une opération de gravure.

    Elle reste indépendante de FreeCAD, STL, SVG ou DXF.
    """

    figure: Figure

    plaque: Optional[Plaque] = None

    gravure: Optional[Gravure] = None

    # ==========================================================
    # PROPRIÉTÉS DE LA FIGURE
    # ==========================================================

    @property
    def largeur_figure(self) -> float:
        return self.figure.boite_englobante.largeur

    @property
    def hauteur_figure(self) -> float:
        return self.figure.boite_englobante.hauteur

    # ==========================================================
    # PROPRIÉTÉS DE LA PLAQUE
    # ==========================================================

    @property
    def largeur_plaque(self) -> Optional[float]:

        if self.plaque is None:
            return None

        return self.plaque.largeur

    @property
    def hauteur_plaque(self) -> Optional[float]:

        if self.plaque is None:
            return None

        return self.plaque.hauteur

    @property
    def epaisseur_plaque(self) -> Optional[float]:

        if self.plaque is None:
            return None

        return self.plaque.epaisseur

    # ==========================================================
    # PROPRIÉTÉS DE LA GRAVURE
    # ==========================================================

    @property
    def profondeur_gravure(self) -> Optional[float]:

        if self.gravure is None:
            return None

        return self.gravure.profondeur

    # ==========================================================
    # VALIDATION
    # ==========================================================

    def verifier(self) -> None:
        """
        Vérifie que la fabrication est cohérente.
        """

        if self.plaque is None:
            return

        boite = self.figure.boite_englobante

        if boite.largeur > self.plaque.largeur:
            raise ValueError(
                "La figure est trop large pour la plaque."
            )

        if boite.hauteur > self.plaque.hauteur:
            raise ValueError(
                "La figure est trop haute pour la plaque."
            )

        if self.gravure is not None:

            if (
                self.gravure.profondeur
                > self.plaque.epaisseur
            ):
                raise ValueError(
                    "La profondeur de gravure dépasse "
                    "l'épaisseur de la plaque."
                )

    # ==========================================================
    # REPRESENTATION
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "Modelisation("
            f"figure={self.figure.__class__.__name__}, "
            f"plaque={self.plaque}, "
            f"gravure={self.gravure}"
            ")"
        )
        