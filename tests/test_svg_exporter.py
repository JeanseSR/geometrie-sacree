from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie
from export.svg_exporter import SVGExporter
from export.writers.svg_writer import SVGWriter

print("=" * 60)
print("TEST SVG EXPORTER")
print("=" * 60)

# ---------------------------------------------------------
# Création de la figure
# ---------------------------------------------------------

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=50
)

print("Figure créée.")
print()

print("Boîte englobante :", figure.boite_englobante)
print()

print("Cercles :", len(figure.cercles))
print("Points  :", len(figure.points))
print("Segments:", len(figure.segments))
print()

# ---------------------------------------------------------
# Export
# ---------------------------------------------------------

exporteur = SVGExporter()

exporteur.export(
    figure,
    "fleur_de_vie.svg"
)

print("Export terminé.")
print("Fichier créé : fleur_de_vie.svg")

print()
print("=" * 60)
print("TEST OK")
print("=" * 60)