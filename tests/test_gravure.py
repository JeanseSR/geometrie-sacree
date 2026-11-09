from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.dimensionnement import Dimensionnement
from fabrication.gravure import Gravure


print("=" * 60)
print("TEST GRAVURE")
print("=" * 60)


# ==========================================================
# 1. FIGURE
# ==========================================================

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=6,
)

assert len(figure.cercles) == 127


# ==========================================================
# 2. EPAISSEUR DE TRAIT
# ==========================================================

figure = EpaisseurTrait(
    largeur=0.4
).appliquer(
    figure
)

assert len(
    figure.couronnes_geometriques
) == 127


# ==========================================================
# 3. DIMENSIONNEMENT
# ==========================================================

dimensionnement = Dimensionnement(
    largeur_support=70,
    hauteur_support=70,
    marge=4,
)

figure = dimensionnement.appliquer(
    figure
)


# ==========================================================
# 4. GRAVURE
# ==========================================================

gravure = Gravure(
    profondeur=1.0
)

modele = gravure.appliquer(
    figure
)


# ==========================================================
# 5. RESULTAT
# ==========================================================

print()
print("Gravure")

print(
    "Couronnes :",
    len(modele.couronnes)
)

print(
    f"Largeur : {modele.largeur:.6f} mm"
)

print(
    f"Hauteur : {modele.hauteur:.6f} mm"
)

print(
    f"Profondeur : {modele.profondeur:.6f} mm"
)


# ==========================================================
# 6. VALIDATIONS
# ==========================================================

assert len(modele.couronnes) == 127

assert (
    modele.largeur <= 62 + 1e-9
)

assert (
    modele.hauteur <= 62 + 1e-9
)

assert abs(
    modele.largeur - 62
) < 1e-9

assert (
    modele.profondeur == 1.0
)


print()
print("=" * 60)
print("TEST GRAVURE : OK")
print("=" * 60)