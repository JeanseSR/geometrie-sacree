from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST CENTRAGE")
print("=" * 60)


# ==========================================================
# FLEUR
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)


# ==========================================================
# DIMENSIONNEMENT
# ==========================================================

dimensionnement = Dimensionnement(
    largeur_support=30,
    hauteur_support=30,
    marge=1
)


# ==========================================================
# ÉCHELLE
# ==========================================================

boite = fleur.boite_englobante

facteur = dimensionnement.facteur_echelle(
    boite.largeur,
    boite.hauteur
)

fleur_reduite = fleur.echelle_autour(
    Point(0, 0),
    facteur
)


# ==========================================================
# TRANSLATION DE CENTRAGE
# ==========================================================

boite_reduite = (
    fleur_reduite.boite_englobante
)

dx, dy = dimensionnement.translation_centrage(
    boite_reduite
)


print()
print("Translation de centrage :")
print(f"dx = {dx:.6f} mm")
print(f"dy = {dy:.6f} mm")


# ==========================================================
# APPLICATION
# ==========================================================

fleur_centree = fleur_reduite.translation(
    dx,
    dy
)


boite_finale = (
    fleur_centree.boite_englobante
)


centre_final_x = (
    boite_finale.xmin
    + boite_finale.xmax
) / 2

centre_final_y = (
    boite_finale.ymin
    + boite_finale.ymax
) / 2


print()
print("Boîte finale :")
print(
    f"x = {boite_finale.xmin:.6f} "
    f"→ {boite_finale.xmax:.6f}"
)

print(
    f"y = {boite_finale.ymin:.6f} "
    f"→ {boite_finale.ymax:.6f}"
)

print()
print("Centre final :")
print(
    f"({centre_final_x:.6f}, "
    f"{centre_final_y:.6f})"
)


# ==========================================================
# VALIDATION
# ==========================================================

assert abs(centre_x) < 1e-9
assert abs(centre_y) < 1e-9


assert (
    boite_finale.xmin >= 1 - 1e-9
)

assert (
    boite_finale.xmax <= 29 + 1e-9
)

assert (
    boite_finale.ymin >= 1 - 1e-9
)

assert (
    boite_finale.ymax <= 29 + 1e-9
)


print()
print("=" * 60)
print("TEST CENTRAGE : OK")
print("=" * 60)