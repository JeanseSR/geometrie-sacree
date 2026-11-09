from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST DIMENSIONNEMENT COMPLET")
print("=" * 60)


# ==========================================================
# FLEUR DE VIE
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)


boite_originale = (
    fleur.boite_englobante
)


print()
print("Figure originale :")

print(
    f"Largeur : "
    f"{boite_originale.largeur:.6f} mm"
)

print(
    f"Hauteur : "
    f"{boite_originale.hauteur:.6f} mm"
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
# APPLICATION COMPLÈTE
# ==========================================================

figure_finale = (
    dimensionnement.appliquer(
        fleur
    )
)


boite_finale = (
    figure_finale.boite_englobante
)


# ==========================================================
# RESULTATS
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
print("Figure finale :")

print(
    f"Largeur : "
    f"{boite_finale.largeur:.6f} mm"
)

print(
    f"Hauteur : "
    f"{boite_finale.hauteur:.6f} mm"
)

print(
    f"Boîte : "
    f"({boite_finale.xmin:.6f}, "
    f"{boite_finale.ymin:.6f}) → "
    f"({boite_finale.xmax:.6f}, "
    f"{boite_finale.ymax:.6f})"
)

print()
print(
    f"Centre : "
    f"({centre_x:.6f}, "
    f"{centre_y:.6f})"
)


# ==========================================================
# VALIDATIONS
# ==========================================================

assert (
    boite_finale.largeur
    <= dimensionnement.largeur_disponible
    + 1e-9
)

assert (
    boite_finale.hauteur
    <= dimensionnement.hauteur_disponible
    + 1e-9
)


assert abs(centre_x) < 1e-9
assert abs(centre_y) < 1e-9


# La figure originale ne doit pas avoir changé.

assert abs(
    fleur.boite_englobante.largeur
    - boite_originale.largeur
) < 1e-9

assert abs(
    fleur.boite_englobante.hauteur
    - boite_originale.hauteur
) < 1e-9


print()
print("=" * 60)
print("TEST DIMENSIONNEMENT COMPLET : OK")
print("=" * 60)