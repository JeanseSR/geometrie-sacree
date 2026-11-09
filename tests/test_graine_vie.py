from geometrie.point import Point

from figures.graine_de_vie import GraineDeVie

from affichage.affichage import Afficheur



print("=" * 60)
print("TEST DE LA GRAINE DE VIE")
print("=" * 60)



# ----------------------------------------------------------
# Création
# ----------------------------------------------------------

print("\n--- CREATION ---")


graine = GraineDeVie(
    centre=Point(0,0),
    rayon=10
)



print("Nom :", graine.nom)

print("\nDescription :")
print(graine.description)


print("\nParamètres :")

for cle, valeur in graine.parametres.items():
    print(
        f"  {cle} = {valeur}"
    )



# ----------------------------------------------------------
# Géométrie
# ----------------------------------------------------------

print("\n--- CERCLES ---")


print(
    "Nombre de cercles :",
    len(graine.cercles)
)


for cercle in graine.cercles:
    print(
        " ",
        cercle
    )



# ----------------------------------------------------------
# Vérifications
# ----------------------------------------------------------

print("\n--- VERIFICATIONS ---")


assert len(graine.cercles) == 7

print("✓ La graine possède 7 cercles")


assert graine.cercle_central in graine.cercles

print("✓ Le cercle central existe")


assert len(graine.cercles_couronne) == 6

print("✓ La couronne possède 6 cercles")



# ----------------------------------------------------------
# Affichage
# ----------------------------------------------------------

print("\n--- AFFICHAGE ---")


afficheur = Afficheur()

afficheur.figure(
    graine
)

afficheur.afficher(
    "Graine de Vie"
)



print("\nTous les tests de la Graine de Vie sont terminés.")