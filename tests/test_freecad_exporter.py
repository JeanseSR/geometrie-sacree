from geometrie.point import Point
from figures.fleur_de_vie import FleurDeVie
from export.freecad_code_exporter import FreeCADCodeExporter


figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

FreeCADCodeExporter().export(
    figure,
    "fleur_de_vie_sketch.py"
)