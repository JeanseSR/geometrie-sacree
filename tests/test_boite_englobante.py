from geometrie.point import Point
from figures.fleur_de_vie import FleurDeVie

print("=" * 60)
print("TEST BOITE ENGLOBANTE")
print("=" * 60)

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=50,
    couronnes=6
)

bbox = figure.boite_englobante

print(bbox)

print()

print("Largeur :", bbox.largeur)
print("Hauteur :", bbox.hauteur)
print("Centre  :", bbox.centre)

print()

print("xmin :", bbox.xmin)
print("ymin :", bbox.ymin)
print("xmax :", bbox.xmax)
print("ymax :", bbox.ymax)


figure2 = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

bbox2 = figure2.boite_englobante

print(bbox2)
print("Largeur :", bbox2.largeur)
print("Hauteur :", bbox2.hauteur)