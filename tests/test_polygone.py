from geometrie.point import Point
from geometrie.polygone import Polygone

print("=" * 60)
print("TEST DE LA CLASSE POLYGONE")
print("=" * 60)

# ----------------------------------------------------------
# Triangle
# ----------------------------------------------------------

triangle = Polygone((
    Point(0, 0),
    Point(4, 0),
    Point(2, 3)
))

print("\n--- TRIANGLE ---")

print("Nombre de sommets :", triangle.nombre_sommets)

print("\nSommets :")
for p in triangle:
    print(" ", p)

print("\nSegments :")
for s in triangle.segments:
    print(" ", s)

print("\nPérimètre :", round(triangle.perimetre, 3))
print("Centre :", triangle.centre)

# ----------------------------------------------------------
# Translation
# ----------------------------------------------------------

print("\n--- TRANSLATION ---")

t2 = triangle.translation(10, 5)

print("Original :", triangle.centre)
print("Translaté :", t2.centre)

# ----------------------------------------------------------
# Rotation
# ----------------------------------------------------------

print("\n--- ROTATION 90° ---")

t3 = triangle.rotation(90)

for p in t3:
    print(p)

# ----------------------------------------------------------
# Rotation autour du centre
# ----------------------------------------------------------

print("\n--- ROTATION AUTOUR DU CENTRE ---")

t4 = triangle.rotation_autour(
    triangle.centre,
    180
)

for p in t4:
    print(p)

# ----------------------------------------------------------
# Hexagone
# ----------------------------------------------------------

print("\n--- HEXAGONE REGULIER ---")

hexagone = Polygone.regulier(
    centre=Point(0, 0),
    rayon=10,
    nb_cotes=6
)

print("Nombre de sommets :", hexagone.nombre_sommets)
print("Périmètre :", round(hexagone.perimetre, 3))
print("Centre :", hexagone.centre)

print("\nSommets :")

for p in hexagone:
    print(p)

print("\nSegments :")

for s in hexagone.segments:
    print(s)

print("\nTous les tests du polygone sont terminés.")