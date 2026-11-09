from geometrie.point import Point
from geometrie.vecteur import Vecteur
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.polygone import Polygone


print("=" * 70)
print(" DEMONSTRATION DU MOTEUR GEOMETRIQUE ")
print("=" * 70)

# ==========================================================
# POINT
# ==========================================================

print("\nPOINT")

A = Point(10, 5)
B = Point(25, 18)

print("A :", A)
print("B :", B)
print("Distance :", A.distance(B))

# ==========================================================
# VECTEUR
# ==========================================================

print("\nVECTEUR")

v = B - A

print("Vecteur AB :", v)
print("Norme :", round(v.norme, 3))
print("Angle :", round(v.angle, 3))
print("Rotation 90° :", v.rotation(90))

# ==========================================================
# SEGMENT
# ==========================================================

print("\nSEGMENT")

segment = Segment(A, B)

print(segment)
print("Longueur :", round(segment.longueur, 3))
print("Milieu :", segment.milieu)

# ==========================================================
# CERCLE
# ==========================================================

print("\nCERCLE")

cercle = Cercle(A, 20)

print(cercle)
print("Diamètre :", cercle.diametre)
print("Périmètre :", round(cercle.perimetre, 3))
print("Aire :", round(cercle.aire, 3))

print("\nPoints remarquables :")

for angle in (0, 90, 180, 270):
    print(
        angle,
        "° ->",
        cercle.point(angle)
    )

# ==========================================================
# POLYGONES REGULIERS
# ==========================================================

print("\nPOLYGONES REGULIERS")

for n in [3, 4, 5, 6, 8]:

    poly = Polygone.regulier(
        centre=Point(0, 0),
        rayon=30,
        nb_cotes=n
    )

    print("\n-------------------------------")
    print(f"{n} côtés")
    print("-------------------------------")

    print(poly)

    print("Centre :", poly.centre)
    print("Périmètre :", round(poly.perimetre, 3))
    print("Largeur :", round(poly.largeur, 3))
    print("Hauteur :", round(poly.hauteur, 3))
    print("Longueur d'un côté :", round(poly.cote, 3))

    print("\nSommets :")

    for i, sommet in enumerate(poly, start=1):
        print(f" {i} -> {sommet}")

print("\n")
print("=" * 70)
print("TOUT LE MOTEUR GEOMETRIQUE FONCTIONNE.")
print("=" * 70)