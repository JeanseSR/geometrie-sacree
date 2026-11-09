from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from fabrication.dimensionnement import Dimensionnement
from export.freecad_code_exporter import FreeCADCodeExporter


print("=" * 60)
print("TEST FREECAD + DIMENSIONNEMENT")
print("=" * 60)


# ==========================================================
# 1. CREATION DE LA FLEUR
# ==========================================================

fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

print()
print("Fleur originale")
print(
    f"Boîte : {fleur.boite_englobante}"
)


# ==========================================================
# 2. DIMENSIONNEMENT POUR LA PLAQUE EXISTANTE
# ==========================================================

dimensionnement = Dimensionnement(
    largeur_support=30,
    hauteur_support=30,
    marge=1
)

figure_finale = dimensionnement.appliquer(
    fleur
)


# ==========================================================
# 3. VERIFICATION
# ==========================================================

boite = figure_finale.boite_englobante

print()
print("Figure adaptée à la plaque")
print(
    f"Largeur : {boite.largeur:.6f} mm"
)

print(
    f"Hauteur : {boite.hauteur:.6f} mm"
)

print(
    f"Centre : "
    f"({(boite.xmin + boite.xmax) / 2:.6f}, "
    f"{(boite.ymin + boite.ymax) / 2:.6f})"
)


assert boite.largeur <= 28 + 1e-9
assert boite.hauteur <= 28 + 1e-9


# ==========================================================
# 4. EXPORT FREECAD
# ==========================================================

fichier = "fleur_de_vie_30x30.py"

exporteur = FreeCADCodeExporter()

exporteur.export(
    figure_finale,
    fichier
)


print()
print("Fichier FreeCAD généré :")
print(fichier)

print()
print("=" * 60)
print("TEST FREECAD + DIMENSIONNEMENT : OK")
print("=" * 60)