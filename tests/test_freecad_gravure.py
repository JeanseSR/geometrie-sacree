from pathlib import Path

from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.epaisseur_trait import EpaisseurTrait
from export.freecad_code_exporter import FreeCADCodeExporter


print("=" * 60)
print("TEST FREECAD GRAVURE")
print("=" * 60)


# ==========================================================
# 1. FLEUR DE VIE
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
# 2. EPAISSEUR DE TRAIT
# ==========================================================

epaisseur = EpaisseurTrait(
    largeur=0.6
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
# 3. VERIFICATION EPAISSEUR
# ==========================================================

for couronne in gravure.couronnes_geometriques:

    assert abs(
        couronne.largeur - 0.6
    ) < 1e-9

print(
    "Largeur des traits : 0.6 mm"
)


# ==========================================================
# 4. EXPORT FREECAD
# ==========================================================

fichier = Path(
    "fleur_de_vie_gravure_freecad.py"
)

exporteur = FreeCADCodeExporter()

exporteur.export(
    gravure,
    str(fichier)
)


# ==========================================================
# 5. VERIFICATION DU SCRIPT
# ==========================================================

assert fichier.exists()

contenu = fichier.read_text(
    encoding="utf-8"
)

# 19 couronnes × 2 cercles
nombre_cercles = contenu.count(
    "sketch.addGeometry("
)

print()
print("Fichier :", fichier)
print(
    "Géométries Sketcher :",
    nombre_cercles
)

assert nombre_cercles == 38

assert "Sketcher::SketchObject" in contenu
assert "Part.Circle(" in contenu


print()
print("=" * 60)
print("TEST FREECAD GRAVURE : OK")
print("=" * 60)