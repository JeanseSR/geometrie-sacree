from pathlib import Path

from geometrie.point import Point

from figures.cube_metatron import CubeMetatron
from fabrication.fabrication import fabriquer
from export.freecad_gravure_exporter import (
    FreeCADGravureExporter
)


print("=" * 60)
print("TEST FREECAD GRAVURE — METATRON")
print("=" * 60)


# ==========================================================
# 1. METATRON
# ==========================================================

figure = CubeMetatron(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2,
)

assert len(figure.cercles) == 13
assert len(figure.segments_metatron) == 78


# ==========================================================
# 2. MODELE DE FABRICATION
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

    largeur_trait=0.6,
)


# ==========================================================
# 3. EXPORT
# ==========================================================

fichier = Path(
    "metatron_gravure_freecad.py"
)

exporteur = FreeCADGravureExporter()

exporteur.export(
    modele,
    fichier
)


# ==========================================================
# 4. VERIFICATIONS
# ==========================================================

assert fichier.exists()

contenu = fichier.read_text(
    encoding="utf-8"
)

assert "CubeMetatron" not in contenu
assert "FleurDeVie" not in contenu
assert "FruitDeVie" not in contenu

assert "Part.makeBox" in contenu
assert "Part.makeCylinder" in contenu

assert "PLAQUE_LARGEUR = 70" in contenu
assert "PLAQUE_HAUTEUR = 70" in contenu
assert "PLAQUE_EPAISSEUR = 2" in contenu
assert "PROFONDEUR_GRAVURE = 1" in contenu

assert "resultat = plaque.cut(outil_total)" in contenu

nombre_couronnes = contenu.count(
    "# Couronne"
)

nombre_bandes = contenu.count(
    "# Bande de segment"
)

print()
print("Fichier :", fichier)
print("Couronnes exportées :", nombre_couronnes)
print("Bandes exportées :", nombre_bandes)
print("Taille :", len(contenu), "caractères")


assert nombre_couronnes == 13
assert nombre_bandes == 78


print()
print("=" * 60)
print("TEST FREECAD GRAVURE METATRON : OK")
print("=" * 60)