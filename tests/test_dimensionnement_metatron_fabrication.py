from geometrie.point import Point

from figures.cube_metatron import CubeMetatron
from fabrication.epaisseur_trait import EpaisseurTrait
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST DIMENSIONNEMENT FABRICATION — METATRON")
print("=" * 60)


# ==========================================================
# 1. METATRON
# ==========================================================

figure = CubeMetatron(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

print()
print("Figure originale")

print(
    "Cercles :",
    len(figure.cercles)
)

print(
    "Segments :",
    len(figure.segments)
)

assert len(figure.cercles) == 13
assert len(figure.segments) == 78


# ==========================================================
# 2. EPAISSEUR DE TRAIT
# ==========================================================

figure_trait = EpaisseurTrait(
    largeur=0.4
).appliquer(
    figure
)

print()
print("Après épaisseur de trait")

print(
    "Couronnes :",
    len(figure_trait.couronnes_geometriques)
)

print(
    "Bandes :",
    len(figure_trait.bandes_segments)
)

assert len(
    figure_trait.couronnes_geometriques
) == 13

assert len(
    figure_trait.bandes_segments
) == 78


# ==========================================================
# 3. AVANT DIMENSIONNEMENT
# ==========================================================

boite_avant = (
    figure_trait.boite_englobante
)

print()
print("Avant dimensionnement")

print(
    f"Largeur : {boite_avant.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite_avant.hauteur:.6f} mm"
)


# ==========================================================
# 4. DIMENSIONNEMENT
# ==========================================================

dimensionnement = Dimensionnement(
    largeur_support=62,
    hauteur_support=62,
    marge=0
)

figure_finale = (
    dimensionnement.appliquer(
        figure_trait
    )
)


# ==========================================================
# 5. RESULTAT
# ==========================================================

boite_finale = (
    figure_finale.boite_englobante
)

print()
print("Après dimensionnement")

print(
    f"Largeur : {boite_finale.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite_finale.hauteur:.6f} mm"
)

print(
    "Couronnes :",
    len(figure_finale.couronnes_geometriques)
)

print(
    "Bandes :",
    len(figure_finale.bandes_segments)
)


# ==========================================================
# 6. VALIDATIONS DIMENSIONS
# ==========================================================

assert (
    boite_finale.largeur
    <= 62 + 1e-9
)

assert (
    boite_finale.hauteur
    <= 62 + 1e-9
)


# ==========================================================
# 7. VALIDATIONS GEOMETRIE
# ==========================================================

assert len(
    figure_finale.couronnes_geometriques
) == 13

assert len(
    figure_finale.bandes_segments
) == 78


# ==========================================================
# 8. CENTRAGE
# ==========================================================

centre_x = (
    boite_finale.xmin
    + boite_finale.xmax
) / 2

centre_y = (
    boite_finale.ymin
    + boite_finale.ymax
) / 2


print()
print(
    f"Centre : "
    f"({centre_x:.9f}, "
    f"{centre_y:.9f})"
)


assert abs(centre_x) < 1e-9
assert abs(centre_y) < 1e-9


# ==========================================================
# 9. ORIGINAL INCHANGE
# ==========================================================

assert len(figure.cercles) == 13
assert len(figure.segments) == 78


print()
print("=" * 60)
print(
    "TEST DIMENSIONNEMENT FABRICATION "
    "METATRON : OK"
)
print("=" * 60)