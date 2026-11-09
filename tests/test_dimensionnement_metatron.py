from geometrie.point import Point

from figures.cube_metatron import CubeMetatron
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST DIMENSIONNEMENT — CUBE DE MÉTATRON")
print("=" * 60)


# ==========================================================
# 1. FIGURE
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


# ==========================================================
# 2. DIMENSIONNEMENT
# ==========================================================

boite_avant = figure.boite_englobante

print()
print("Avant dimensionnement")

print(
    f"Largeur : {boite_avant.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite_avant.hauteur:.6f} mm"
)


dimensionnement = Dimensionnement(
    largeur_support=62,
    hauteur_support=62,
    marge=0
)


# ==========================================================
# 3. APPLICATION
# ==========================================================

figure_finale = dimensionnement.appliquer(
    figure
)


boite_apres = (
    figure_finale.boite_englobante
)


# ==========================================================
# 4. RESULTATS
# ==========================================================

print()
print("Après dimensionnement")

print(
    f"Largeur : {boite_apres.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite_apres.hauteur:.6f} mm"
)

print(
    f"Segments : {len(figure_finale.segments)}"
)

print(
    f"Cercles : {len(figure_finale.cercles)}"
)


# ==========================================================
# 5. VALIDATIONS
# ==========================================================

assert len(figure_finale.cercles) == 13

assert len(figure_finale.segments) == 78

assert (
    boite_apres.largeur
    <= 62 + 1e-9
)

assert (
    boite_apres.hauteur
    <= 62 + 1e-9
)


# La figure originale ne doit pas être modifiée.

assert len(figure.cercles) == 13

assert len(figure.segments) == 78


print()
print("=" * 60)
print("TEST DIMENSIONNEMENT MÉTATRON : OK")
print("=" * 60)