from geometrie import Point
from geometrie import Cercle
from tests.test_noyau import *

A = Point(0, 0)
B = Point(3, 4)

print(A)
print(B)

print(A.distance(B))


c1 = Cercle(
    centre=Point(0, 0),
    rayon=25
)

print(c1)

print("Diametre :", c1.diametre)
print("Perimetre :", round(c1.perimetre, 2))
print("Aire :", round(c1.aire, 2))

c2 = c1.translation(50, 30)

print(c2)

print(c1.contient(Point(10, 5)))
print(c1.contient(Point(40, 40)))


vesica = VesicaPiscis(
    centre=Point(0,0),
    rayon=50
)


print(vesica.nom)

print(
    vesica.informations
)


for objet in vesica:
    print(objet)