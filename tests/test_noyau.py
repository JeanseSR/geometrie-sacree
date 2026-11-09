from geometrie.point import Point
from geometrie.vecteur import Vecteur
from geometrie.segment import Segment
from geometrie.cercle import Cercle


print("=" * 60)
print("TEST DE LA BIBLIOTHEQUE GEOMETRIQUE")
print("=" * 60)

# ----------------------------------------------------------
# POINTS
# ----------------------------------------------------------

print("\n--- POINTS ---")

A = Point(0, 0)
B = Point(3, 4)

print("A =", A)
print("B =", B)
print("Distance AB =", A.distance(B))

# Translation

C = A.translation(10, 5)
print("Translation de A :", C)

# Rotation

D = B.rotation(90)
print("Rotation de B (90°) :", D)

# ----------------------------------------------------------
# VECTEURS
# ----------------------------------------------------------

print("\n--- VECTEURS ---")

v1 = Vecteur(3, 4)
v2 = Vecteur(-2, 5)

print("v1 =", v1)
print("v2 =", v2)

print("Norme v1 =", v1.norme)
print("Norme² v1 =", v1.norme2)
print("Angle v1 =", round(v1.angle, 2))

print("Unitaire =", v1.unitaire)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)

print("2 * v1 =", 2 * v1)

print("Produit scalaire =", v1.produit_scalaire(v2))
print("Produit vectoriel =", v1.produit_vectoriel(v2))

print("Angle entre les deux =", round(v1.angle_avec(v2), 2))

print("Rotation 60° =", v1.rotation(60))

print("Normale gauche =", v1.normale_gauche)
print("Normale droite =", v1.normale_droite)

# ----------------------------------------------------------
# POINT + VECTEUR
# ----------------------------------------------------------

print("\n--- POINT + VECTEUR ---")

E = A + v1

print("A + v1 =", E)

print("E - A =", E - A)

# ----------------------------------------------------------
# SEGMENTS
# ----------------------------------------------------------

print("\n--- SEGMENTS ---")

S = Segment(A, B)

print(S)

print("Longueur =", S.longueur)
print("Milieu =", S.milieu)
print("Vecteur =", S.vecteur)
print("Angle =", S.angle)

print("Translation =", S.translation(5, 5))
print("Rotation 90° =", S.rotation(90))

# ----------------------------------------------------------
# CERCLES
# ----------------------------------------------------------

print("\n--- CERCLES ---")

C1 = Cercle(A, 10)

print(C1)

print("Diamètre =", C1.diametre)
print("Périmètre =", round(C1.perimetre, 2))
print("Aire =", round(C1.aire, 2))

print("Point 0° =", C1.point(0))
print("Point 90° =", C1.point(90))
print("Point 180° =", C1.point(180))
print("Point 270° =", C1.point(270))

print("Contient (5,0) :", C1.contient(Point(5, 0)))
print("Contient (20,0) :", C1.contient(Point(20, 0)))

print("Translation =", C1.translation(20, 10))

print("\nTous les tests sont terminés.")