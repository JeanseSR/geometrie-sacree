from pathlib import Path

from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.epaisseur_trait import EpaisseurTrait
from export.svg_exporter import SVGExporter


print("=" * 60)
print("TEST SVG GRAVURE")
print("=" * 60)


# ==========================================================
# 1. FIGURE ORIGINALE
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

print()
print("Figure originale")
print("Cercles :", len(fleur.cercles))

assert len(fleur.cercles) == 19


# ==========================================================
# 2. TRANSFORMATION FABRICATION
# ==========================================================

epaisseur = EpaisseurTrait(
    largeur=0.4
)

gravure = epaisseur.appliquer(
    fleur
)

print()
print("Figure fabrication")
print(
    "Couronnes :",
    len(gravure.couronnes_geometriques)
)

assert len(
    gravure.couronnes_geometriques
) == 19


# ==========================================================
# 3. VERIFICATION DES COURONNES
# ==========================================================

for couronne in gravure.couronnes_geometriques:

    assert abs(
        couronne.largeur - 0.4
    ) < 1e-9

    assert (
        couronne.rayon_exterieur
        > couronne.rayon_interieur
    )


print(
    "Largeur des traits : 0.4 mm"
)


# ==========================================================
# 4. EXPORT SVG
# ==========================================================

fichier = Path(
    "fleur_de_vie_gravure.svg"
)

exporteur = SVGExporter(
    marge=1
)

exporteur.export(
    gravure,
    str(fichier)
)


# ==========================================================
# 5. VERIFICATION DU FICHIER
# ==========================================================

assert fichier.exists()

contenu = fichier.read_text(
    encoding="utf-8"
)

assert "<svg" in contenu
assert "</svg>" in contenu


# Chaque couronne possède :
#   - 1 cercle extérieur
#   - 1 cercle intérieur
#
# 19 couronnes = 38 cercles SVG

nombre_cercles_svg = contenu.count(
    "<circle "
)

print()
print("Fichier :", fichier)
print(
    "Cercles SVG :",
    nombre_cercles_svg
)

assert nombre_cercles_svg == 38


print()
print("=" * 60)
print("TEST SVG GRAVURE : OK")
print("=" * 60)
