from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.dimensionnement import Dimensionnement
from fabrication.plaque import Plaque
from fabrication.gravure import Gravure
from fabrication.modelisation import Modelisation


print("=" * 60)
print("TEST MODELISATION")
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
).appliquer(figure)


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
# 4. PLAQUE
# ==========================================================

plaque = Plaque(
    largeur=70,
    hauteur=70,
    epaisseur=2,
)


# ==========================================================
# 5. GRAVURE
# ==========================================================

gravure = Gravure(
    profondeur=1,
)


# ==========================================================
# 6. MODELISATION
# ==========================================================

modele = Modelisation(
    figure=figure,
    plaque=plaque,
    gravure=gravure,
)


# ==========================================================
# 7. VERIFICATION
# ==========================================================

modele.verifier()


# ==========================================================
# 8. RESULTATS
# ==========================================================

print()
print("Modèle de fabrication")

print(
    f"Figure : "
    f"{modele.largeur_figure:.6f} × "
    f"{modele.hauteur_figure:.6f} mm"
)

print(
    f"Plaque : "
    f"{modele.largeur_plaque:.6f} × "
    f"{modele.hauteur_plaque:.6f} × "
    f"{modele.epaisseur_plaque:.6f} mm"
)

print(
    f"Gravure : "
    f"{modele.profondeur_gravure:.6f} mm"
)


# ==========================================================
# 9. VALIDATIONS
# ==========================================================

assert len(
    modele.figure.couronnes_geometriques
) == 127

assert abs(
    modele.largeur_figure - 62
) < 1e-9

assert (
    modele.hauteur_figure <= 62 + 1e-9
)

assert modele.largeur_plaque == 70
assert modele.hauteur_plaque == 70
assert modele.epaisseur_plaque == 2

assert modele.profondeur_gravure == 1


print()
print("=" * 60)
print("TEST MODELISATION : OK")
print("=" * 60)