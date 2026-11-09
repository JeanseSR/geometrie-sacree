from geometrie.point import Point
from figures.vesica_piscis import VesicaPiscis
from affichage.affichage import Afficheur


print("=" * 60)
print("TEST DE LA FIGURE VESICA PISCIS")
print("=" * 60)


# ----------------------------------------------------------
# Création
# ----------------------------------------------------------

print("\n--- CREATION ---")

vesica = VesicaPiscis(
    centre=Point(0, 0),
    rayon=10
)


print("Nom :", vesica.nom)

print("Description :")
print(vesica.description)

print("\nParamètres :")
for cle, valeur in vesica.parametres.items():
    print(f"  {cle} = {valeur}")


# ----------------------------------------------------------
# Géométrie contenue
# ----------------------------------------------------------

print("\n--- OBJETS GEOMETRIQUES ---")

print("Nombre total d'objets :", len(vesica))


print("\nCercles :")

for cercle in vesica.cercles:
    print(" ", cercle)


print("\nPoints d'intersection :")

for point in vesica.points:
    print(" ", point)



# ----------------------------------------------------------
# Eléments remarquables
# ----------------------------------------------------------

print("\n--- ELEMENTS REMARQUABLES ---")


print(
    "Centre :",
    vesica.centre
)


print(
    "Cercle gauche :",
    vesica.cercle_gauche
)


print(
    "Cercle droit :",
    vesica.cercle_droit
)


print(
    "Intersection haute :",
    vesica.intersection_haute
)


print(
    "Intersection basse :",
    vesica.intersection_basse
)



# ----------------------------------------------------------
# Vérifications
# ----------------------------------------------------------

print("\n--- VERIFICATIONS ---")


assert len(vesica.cercles) == 2

print("✓ Deux cercles présents")


assert len(vesica.points) == 2

print("✓ Deux intersections présentes")


assert vesica.cercle_gauche.rayon == vesica.cercle_droit.rayon

print("✓ Les deux rayons sont identiques")


assert vesica.cercle_gauche.centre != vesica.cercle_droit.centre

print("✓ Les centres sont distincts")



# ----------------------------------------------------------
# Affichage
# ----------------------------------------------------------

print("\n--- AFFICHAGE ---")


afficheur = Afficheur()

afficheur.figure(vesica)

afficheur.afficher(
    "Vesica Piscis"
)


print("\nTous les tests Vesica Piscis sont terminés.")