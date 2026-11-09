from geometrie.point import Point
from geometrie.reseau_hexagonal_axial import ReseauHexagonalAxial

from figures.figure import Figure
from affichage.affichage import Afficheur



print("=" * 60)
print("TEST DU RESEAU HEXAGONAL AXIAL")
print("=" * 60)



# ----------------------------------------------------------
# Création
# ----------------------------------------------------------

print("\n--- CREATION ---")


reseau = ReseauHexagonalAxial(
    centre=Point(0, 0),
    pas=1                   0,
    couronnes=2
)


print("Centre :", reseau.centre)
print("Pas :", reseau.pas)
print("Couronnes :", reseau.couronnes)


print(
    "\nNombre de points :",
    len(reseau)
)



# ----------------------------------------------------------
# Points
# ----------------------------------------------------------

print("\n--- POINTS ---")


for index, point in enumerate(
    reseau,
    start=1
):

    print(
        f"{index:2d} : {point}"
    )



# ----------------------------------------------------------
# Vérifications
# ----------------------------------------------------------

print("\n--- VERIFICATIONS ---")


assert len(reseau) == 19

print(
    "✓ Couronne 2 = 19 points"
)


assert len(reseau.points) == 19

print(
    "✓ Liste interne correcte"
)


print("\n--- COURONNES ---")


for numero, couronne in enumerate(
    reseau.couronnes_points
):

    print(
        f"Couronne {numero} : {len(couronne)} points"
    )


assert len(reseau.couronnes_points[0]) == 1

assert len(reseau.couronnes_points[1]) == 6

assert len(reseau.couronnes_points[2]) == 12


print(
    "✓ Structure des couronnes correcte"
)



print(
    "\nVérification des doublons..."
)


for i, p1 in enumerate(reseau.points):

    for p2 in reseau.points[i+1:]:

        assert p1 != p2


print(
    "✓ Aucun point doublon"
)


for i, p1 in enumerate(reseau.points):

    for p2 in reseau.points[i+1:]:

        assert not (
            abs(p1.x - p2.x) < 1e-9
            and
            abs(p1.y - p2.y) < 1e-9
        )

print("✓ Aucun doublon géométrique")



# ----------------------------------------------------------
# Conversion en Figure
# ----------------------------------------------------------

print("\n--- FIGURE ---")


figure = Figure(
    nom="Réseau hexagonal axial"
)


for point in reseau:

    figure.ajouter_point(
        point
    )


print(
    "Points dans la figure :",
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
    "Réseau hexagonal axial"
)



print(
    "\nTous les tests du réseau hexagonal axial sont terminés."
)