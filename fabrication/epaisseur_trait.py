from __future__ import annotations

from dataclasses import dataclass

from geometrie.cercle import Cercle
from geometrie.segment import Segment
from geometrie.couronne import Couronne
from geometrie.bande_segment import BandeSegment

from figures.figure import Figure


@dataclass(frozen=True)
class EpaisseurTrait:
    """
    Transforme les lignes géométriques en géométrie
    utilisable pour la fabrication.

    Cercle  -> Couronne
    Segment -> BandeSegment

    Toutes les dimensions sont exprimées en mm.
    """

    largeur: float

    def __post_init__(self):

        if self.largeur <= 0:
            raise ValueError(
                "La largeur du trait doit être "
                "strictement positive."
            )

    # ==========================================================
    # CERCLE
    # ==========================================================

    def _creer_couronne(
        self,
        cercle: Cercle
    ) -> Couronne:

        demi_largeur = self.largeur / 2

        rayon_interieur = (
            cercle.rayon - demi_largeur
        )

        rayon_exterieur = (
            cercle.rayon + demi_largeur
        )

        if rayon_interieur <= 0:
            raise ValueError(
                "L'épaisseur du trait est trop grande "
                "pour le rayon du cercle."
            )

        return Couronne(
            centre=cercle.centre,
            rayon_interieur=rayon_interieur,
            rayon_exterieur=rayon_exterieur
        )

    # ==========================================================
    # SEGMENT
    # ==========================================================

    def _creer_bande_segment(
        self,
        segment: Segment
    ) -> BandeSegment:

        return BandeSegment(
            debut=segment.debut,
            fin=segment.fin,
            largeur=self.largeur
        )

    # ==========================================================
    # APPLICATION
    # ==========================================================

    def appliquer(
        self,
        figure: Figure
    ) -> Figure:
        """
        Transforme une figure géométrique en figure
        adaptée à la fabrication.

        Cercle  -> Couronne
        Segment -> BandeSegment

        Les autres objets sont conservés tels quels.
        """

        resultat = Figure(
            nom=figure.nom,
            description=figure.description,
            auteur=figure.auteur,
            unite=figure.unite,
            tags=set(figure.tags),
            parametres=dict(figure.parametres)
        )

        for objet in figure:

            if isinstance(objet, Cercle):

                resultat.ajouter(
                    self._creer_couronne(objet)
                )

            elif isinstance(objet, Segment):

                resultat.ajouter(
                    self._creer_bande_segment(objet)
                )

            else:

                resultat.ajouter(objet)

        return resultat