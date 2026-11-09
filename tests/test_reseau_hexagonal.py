from geometrie.point import Point
from geometrie.reseau_hexagonal import ReseauHexagonal

from figures.figure import Figure
from affichage.affichage import Afficheur


print("=" * 60)
print("TEST DE LA CLASSE RESEAU HEXAGONAL")
print("=" * 60)

# ----------------------------------------------------------
# Réseau
# ----------------------------------------------------------

print("\n--- CREATION ---")

reseau = ReseauHexagonal(
    centre=Point(0, 0),
    pas=10,
    couronnes=2
)

print("Centre :", reseau.centre)
print("Pas :", reseau.pas)
print("Couronnes :", reseau.couronnes)

print("\nNombre de points :", len(reseau))


# ----------------------------------------------------------
# Liste des points
# ----------------------------------------------------------

print("\n--- POINTS ---")

for i, point in enumerate(reseau, start=1):
    print(f"{i:2d} : {point}")


# ----------------------------------------------------------
# Vérifications
# ----------------------------------------------------------

print("\n--- VERIFICATIONS ---")

assert len(reseau) == 19
print("✓ Nombre de points correct")

assert reseau.points[0] == Point(0, 0)
print("✓ Le premier point est le centre")

print("\nTous les points sont distincts...")

for i, p1 in enumerate(reseau.points):

    for p2 in reseau.points[i+1:]:

        assert p1 != p2

print("✓ Aucun doublon")

# -------------------
# Construction d'une Figure
# ----------------------------------------------------------

print("\n--- CONVERSION EN FIGURE ---")

figure = Figure(
    nom="Réseau hexagonal"
)

for point in reseau:
    figure.ajouter_point(point)

print(
    "Nombre de points dans la figure :",
    len(figure.points)
)


# ----------------------------------------------------------
# Affichage
# ----------------------------------------------------------

print("\n--- AFFICHAGE ---")

afficheur = Afficheur()

afficheur.figure(
    figure
)

afficheur.afficher(
    "Réseau hexagonal"
)

print("\nTous les tests du réseau hexagonal sont terminés.")