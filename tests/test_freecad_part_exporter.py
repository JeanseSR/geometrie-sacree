from pathlib import Path

from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie

from fabrication.fabrication import fabriquer

from export.freecad_part_exporter import (
    FreeCADPartExporter
)


print("=" * 60)
print("TEST FREECAD PART EXPORTER")
print("=" * 60)


# ==========================================================
# 1. FIGURE
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=6,
)


# ==========================================================
# 2. FABRICATION COMPLETE
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
# 3. EXPORT
# ==========================================================

fichier = Path(
    "fleur_de_vie_3d_freecad.py"
)

exporteur = FreeCADPartExporter()

resultat = exporteur.export(
    modele,
    fichier,
)


# ==========================================================
# 4. VERIFICATIONS
# ==========================================================

assert resultat.exists()

contenu = resultat.read_text(
    encoding="utf-8"
)

assert "import FreeCAD as App" in contenu

assert "import Part" in contenu

assert "Part.makeBox(" in contenu

assert "Part.makeCylinder(" in contenu

assert ".cut(" in contenu

assert "from figures" not in contenu
assert "from fabrication" not in contenu
assert "import geometrie" not in contenu

assert contenu.count(
    "# Couronne "
) == 127


# ==========================================================
# RESULTAT
# ==========================================================

print()
print("Fichier :", resultat)

print(
    "Couronnes exportées :",
    contenu.count("# Couronne ")
)

print(
    "Taille :",
    len(contenu),
    "caractères"
)


print()
print("=" * 60)
print("TEST FREECAD PART EXPORTER : OK")
print("=" * 60)