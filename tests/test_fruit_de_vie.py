from geometrie.point import Point

from figures.fruit_de_vie import FruitDeVie

from affichage.affichage import Afficheur



print("=" * 60)
print("TEST DU FRUIT DE VIE")
print("=" * 60)



# ----------------------------------------------------------
# Création
# ----------------------------------------------------------

print("\n--- CREATION ---")


fruit = FruitDeVie(
    centre=Point(0, 0),
    rayon=10,
    couronnes=2
)



print("Nom :", fruit.nom)

print("Rayon :", fruit.rayon)

print("Couronnes :", fruit.couronnes)



print(
    "Nombre de cercles :",
    len(fruit.cercles)
)


print(
    "Nombre de points :",
    len(fruit.points)
)



# ----------------------------------------------------------
# Vérifications
# ----------------------------------------------------------

print("\n--- VERIFICATIONS ---")


assert len(fruit.cercles) == 19

print(
    "✓ Les 19 cercles de la Fleur de Vie sont présents"
)



assert len(fruit.points) > 0

print(
    "✓ Intersections détectées"
)



# ----------------------------------------------------------
# Points remarquables
# ----------------------------------------------------------

print("\n--- POINTS REMARQUABLES ---")


print(
    "Points centraux :",
    len(fruit.points_centraux)
)


print(
    "Points extérieurs :",
    len(fruit.points_exterieurs)
)



assert (
    len(fruit.points_centraux)
    +
    len(fruit.points_exterieurs)
    <=
    len(fruit.points)
)


print(
    "✓ Classification effectuée"
)



# ----------------------------------------------------------
# Affichage
# ----------------------------------------------------------

print("\n--- AFFICHAGE ---")


afficheur = Afficheur()


afficheur.figure(
    fruit
)


afficheur.afficher(
    "Fruit de Vie"
)



print(
    "\nTous les tests du Fruit de Vie sont terminés."
)