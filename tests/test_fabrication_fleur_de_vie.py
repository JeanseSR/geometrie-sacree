from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.fabrication import fabriquer
from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST FABRICATION — FLEUR DE VIE 6 COURONNES")
print("=" * 60)


# ==========================================================
# 1. FIGURE
# ==========================================================

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=6,
)

print()
print("Figure originale")
print("Cercles :", len(figure.cercles))

assert len(figure.cercles) == 127


# ==========================================================
# 2. FABRICATION
# ==========================================================

modele = fabriquer(
    figure,

    support="plaque",

    largeur=70,
    hauteur=70,

    marge=4,

    epaisseur=2,

    operation="gravure",

    profondeur=1,

    largeur_trait=0.4,
)


# ==========================================================
# 3. RESULTAT
# ==========================================================

boite = modele.figure.boite_englobante

print()
print("Figure fabriquée")

print(
    f"Largeur : {boite.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite.hauteur:.6f} mm"
)

print(
    "Couronnes géométriques :",
    len(modele.figure.couronnes_geometriques)
)


# ==========================================================
# 4. VALIDATIONS
# ==========================================================

assert len(
    modele.figure.couronnes_geometriques
) == 127

assert (
    boite.largeur <= 62 + 1e-9
)

assert (
    boite.hauteur <= 62 + 1e-9
)

assert modele.epaisseur == 2

assert modele.profondeur == 1

assert modele.largeur_trait == 0.4

assert boite.largeur > 0
assert boite.hauteur > 0


print()
print("Zone utile : 62 × 62 mm")
print("Trait : 0.4 mm")
print("Plaque : 70 × 70 × 2 mm")
print("Gravure : 1 mm")

print()
print("=" * 60)
print("TEST FABRICATION FLEUR DE VIE : OK")
print("=" * 60)



from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.dimensionnement import Dimensionnement


figure_trait = EpaisseurTrait(
    largeur=0.4
).appliquer(figure)

boite_trait = figure_trait.boite_englobante

print()
print("AVANT DIMENSIONNEMENT")
print("Largeur :", boite_trait.largeur)
print("Hauteur :", boite_trait.hauteur)

dimensionnement = Dimensionnement(
    largeur_support=70,
    hauteur_support=70,
    marge=4,
)

print(
    "Facteur :",
    dimensionnement.facteur_echelle(
        boite_trait.largeur,
        boite_trait.hauteur
    )
)

figure_test = dimensionnement.appliquer(
    figure_trait
)

boite_test = figure_test.boite_englobante

print()
print("APRÈS DIMENSIONNEMENT DIRECT")
print("Largeur :", boite_test.largeur)
print("Hauteur :", boite_test.hauteur)