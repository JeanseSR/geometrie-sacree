from geometrie.point import Point

from figures.cube_metatron import CubeMetatron
from fabrication.fabrication import fabriquer


print("=" * 60)
print("TEST FABRIQUER — CUBE DE METATRON")
print("=" * 60)


# ==========================================================
# 1. FIGURE
# ==========================================================

figure = CubeMetatron(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2,
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
# 2. FABRICATION COMPLETE
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

print()
print("MODELE FINAL")

print(
    f"Figure : "
    f"{modele.figure.boite_englobante.largeur:.6f} × "
    f"{modele.figure.boite_englobante.hauteur:.6f} mm"
)

print(
    f"Plaque : "
    f"{modele.plaque.largeur:.6f} × "
    f"{modele.plaque.hauteur:.6f} × "
    f"{modele.plaque.epaisseur:.6f} mm"
)

print(
    f"Gravure : "
    f"{modele.gravure.profondeur:.6f} mm"
)

print(
    "Couronnes :",
    len(modele.figure.couronnes_geometriques)
)

print(
    "Bandes :",
    len(modele.figure.bandes_segments)
)


# ==========================================================
# 4. VALIDATIONS
# ==========================================================

assert modele.plaque is not None
assert modele.gravure is not None

assert (
    modele.plaque.largeur
    == 70
)

assert (
    modele.plaque.hauteur
    == 70
)

assert (
    modele.plaque.epaisseur
    == 2
)

assert (
    modele.gravure.profondeur
    == 1
)

assert len(
    modele.figure.couronnes_geometriques
) == 13

assert len(
    modele.figure.bandes_segments
) == 78


boite = modele.figure.boite_englobante

assert boite.largeur <= 62 + 1e-9
assert boite.hauteur <= 62 + 1e-9


# ==========================================================
# 5. CENTRAGE
# ==========================================================

centre_x = (
    boite.xmin + boite.xmax
) / 2

centre_y = (
    boite.ymin + boite.ymax
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
# 6. FIGURE ORIGINALE INCHANGEE
# ==========================================================

assert len(figure.cercles) == 13
assert len(figure.segments) == 78


print()
print("=" * 60)
print("TEST FABRIQUER METATRON : OK")
print("=" * 60)