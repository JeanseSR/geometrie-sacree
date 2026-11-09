from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.fabrication import fabriquer


print("=" * 60)
print("TEST FABRIQUER — API COMPLETE")
print("=" * 60)


# ==========================================================
# FIGURE
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=6,
)


# ==========================================================
# FABRICATION COMPLETE
# ==========================================================

modele = fabriquer(
    fleur,
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
# RESULTATS
# ==========================================================

print()
print("MODELE FINAL")

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

print(
    "Couronnes :",
    len(modele.figure.couronnes_geometriques)
)


# ==========================================================
# VALIDATIONS
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

assert modele.plaque is not None

assert modele.plaque.largeur == 70
assert modele.plaque.hauteur == 70
assert modele.plaque.epaisseur == 2

assert modele.gravure is not None

assert modele.gravure.profondeur == 1

modele.verifier()


print()
print("=" * 60)
print("TEST FABRIQUER : OK")
print("=" * 60)