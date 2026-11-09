from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.dimensionnement import Dimensionnement


print("=" * 60)
print("TEST ECHELLE FIGURE")
print("=" * 60)


# ==========================================================
# 1. FLEUR DE VIE ORIGINALE
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

boite = fleur.boite_englobante

print()
print("Figure originale")

print(
    f"Largeur : {boite.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite.hauteur:.6f} mm"
)


# ==========================================================
# 2. DIMENSIONNEMENT DU SUPPORT
# ==========================================================

dimensionnement = Dimensionnement(
    largeur_support=30,
    hauteur_support=30,
    marge=1
)

facteur = dimensionnement.facteur_echelle(
    boite.largeur,
    boite.hauteur
)

print()
print("Support")
print("Dimensions : 30 × 30 mm")
print("Marge :", dimensionnement.marge, "mm")

print()
print(
    "Zone disponible : "
    f"{dimensionnement.largeur_disponible:.6f} × "
    f"{dimensionnement.hauteur_disponible:.6f} mm"
)

print()
print(
    f"Facteur d'échelle : {facteur:.9f}"
)


# ==========================================================
# 3. MISE À L'ÉCHELLE
# ==========================================================

fleur_echelle = fleur.echelle_autour(
    Point(0, 0),
    facteur
)

boite2 = fleur_echelle.boite_englobante


print()
print("Figure après mise à l'échelle")

print(
    f"Largeur : {boite2.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite2.hauteur:.6f} mm"
)


# ==========================================================
# 4. VERIFICATIONS
# ==========================================================

assert (
    boite2.largeur
    <= dimensionnement.largeur_disponible + 1e-9
)

assert (
    boite2.hauteur
    <= dimensionnement.hauteur_disponible + 1e-9
)


# La proportion doit être conservée.

rapport_original = (
    boite.largeur / boite.hauteur
)

rapport_final = (
    boite2.largeur / boite2.hauteur
)

assert abs(
    rapport_original - rapport_final
) < 1e-9


# La fleur originale ne doit pas être modifiée.

boite_originale_apres = (
    fleur.boite_englobante
)

assert abs(
    boite_originale_apres.largeur
    - boite.largeur
) < 1e-9

assert abs(
    boite_originale_apres.hauteur
    - boite.hauteur
) < 1e-9


print()
print("=" * 60)
print("TEST ECHELLE FIGURE : OK")
print("=" * 60)