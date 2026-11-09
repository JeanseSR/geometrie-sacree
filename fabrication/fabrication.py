from __future__ import annotations

from fabrication.dimensionnement import Dimensionnement
from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.plaque import Plaque
from fabrication.gravure import Gravure
from fabrication.modelisation import Modelisation


def fabriquer(
    figure,
    *,
    support=None,
    largeur=None,
    hauteur=None,
    marge=0.0,
    epaisseur=None,
    operation=None,
    profondeur=None,
    largeur_trait=None,
):
    """
    Construit un modèle de fabrication complet.

    Ordre des opérations :

        figure
          ↓
        épaisseur du trait
          ↓
        dimensionnement
          ↓
        plaque / support
          ↓
        opération de fabrication
          ↓
        Modelisation

    La figure originale n'est jamais modifiée.
    """

    # ==========================================================
    # VALIDATIONS GENERALES
    # ==========================================================

    if marge < 0:
        raise ValueError(
            "La marge doit être positive ou nulle."
        )

    if largeur is not None and largeur <= 0:
        raise ValueError(
            "La largeur doit être strictement positive."
        )

    if hauteur is not None and hauteur <= 0:
        raise ValueError(
            "La hauteur doit être strictement positive."
        )

    if epaisseur is not None and epaisseur <= 0:
        raise ValueError(
            "L'épaisseur doit être strictement positive."
        )

    if profondeur is not None and profondeur <= 0:
        raise ValueError(
            "La profondeur doit être strictement positive."
        )

    if largeur_trait is not None and largeur_trait <= 0:
        raise ValueError(
            "La largeur du trait doit être "
            "strictement positive."
        )

    if support not in (
        None,
        "plaque",
        "pochoir",
    ):
        raise ValueError(
            f"Support inconnu : {support}"
        )

    if operation not in (
        None,
        "gravure",
        "relief",
        "decoupe",
    ):
        raise ValueError(
            f"Opération inconnue : {operation}"
        )

    # ==========================================================
    # FIGURE DE TRAVAIL
    # ==========================================================

    resultat = figure

    # ==========================================================
    # 1. EPAISSEUR DE TRAIT
    # ==========================================================

    if largeur_trait is not None:

        resultat = EpaisseurTrait(
            largeur=largeur_trait
        ).appliquer(
            resultat
        )

    # ==========================================================
    # 2. DIMENSIONNEMENT
    # ==========================================================

    if largeur is not None or hauteur is not None:

        if largeur is None or hauteur is None:
            raise ValueError(
                "largeur et hauteur doivent être "
                "fournies ensemble."
            )

        dimensionnement = Dimensionnement(
            largeur_support=largeur,
            hauteur_support=hauteur,
            marge=marge,
        )

        resultat = dimensionnement.appliquer(
            resultat
        )

    # ==========================================================
    # 3. SUPPORT
    # ==========================================================

    plaque = None

    if support == "plaque":

        if epaisseur is None:
            raise ValueError(
                "L'épaisseur est obligatoire "
                "pour une plaque."
            )

        if largeur is None or hauteur is None:
            raise ValueError(
                "largeur et hauteur sont obligatoires "
                "pour une plaque."
            )

        plaque = Plaque(
            largeur=largeur,
            hauteur=hauteur,
            epaisseur=epaisseur,
        )

    # ==========================================================
    # 4. OPERATION
    # ==========================================================

    gravure = None

    if operation == "gravure":

        if profondeur is None:
            raise ValueError(
                "La profondeur est obligatoire "
                "pour une gravure."
            )

        gravure = Gravure(
            profondeur=profondeur
        )

    # ==========================================================
    # 5. MODELE COMPLET
    # ==========================================================

    modele = Modelisation(
        figure=resultat,
        plaque=plaque,
        gravure=gravure,
    )

    # ==========================================================
    # 6. VERIFICATION FINALE
    # ==========================================================

    modele.verifier()

    return modele