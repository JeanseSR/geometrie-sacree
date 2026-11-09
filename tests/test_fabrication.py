from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.fabrication import fabriquer


print("=" * 60)
print("TEST FABRICATION")
print("=" * 60)


# ==========================================================
# FIGURE
# ==========================================================

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2,
)

assert len(figure.cercles) == 19


# ==========================================================
# FABRICATION
# ==========================================================

modele = fabriquer(
    figure,
    support="plaque",
    largeur=30,
    hauteur=30,
    marge=1,
    epaisseur=2,
    operation="gravure",
    profondeur=1,
    largeur_trait=0.4,
)


# ==========================================================
# RESULTAT
# ==========================================================

print()
print("Type :", type(modele).__name__)

print(
    "Cercles :",
    len(modele.figure.cercles)
)

print(
    "Couronnes :",
    len(modele.figure.couronnes_geometriques)
)

print(
    "Support :",
    modele.support
)

print(
    "Dimensions :",
    modele.largeur,
    "×",
    modele.hauteur,
)

print(
    "Épaisseur :",
    modele.epaisseur,
)

print(
    "Opération :",
    modele.operation,
)

print(
    "Profondeur :",
    modele.profondeur,
)

print(
    "Trait :",
    modele.largeur_trait,
)


# ==========================================================
# VALIDATIONS
# ==========================================================

assert modele.support == "plaque"

assert modele.largeur == 30
assert modele.hauteur == 30

assert modele.epaisseur == 2

assert modele.operation == "gravure"

assert modele.profondeur == 1

assert modele.largeur_trait == 0.4

assert len(
    modele.figure.couronnes_geometriques
) == 19


print()
print("=" * 60)
print("TEST FABRICATION : OK")
print("=" * 60)