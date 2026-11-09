from geometrie.point import Point

from figures.fleur_de_vie import FleurDeVie

from affichage.affichage import Afficheur



print("=" * 60)
print("TEST DE LA FLEUR DE VIE")
print("=" * 60)



# ----------------------------------------------------------
# Création
# ----------------------------------------------------------

print("\n--- CREATION ---")


fleur = FleurDeVie(
    centre=Point(0, 0),
    rayon=10,
    couronnes=3
)



print("Nom :", fleur.nom)

print("Rayon :", fleur.rayon)

print("Couronnes :", fleur.couronnes)

print(
    "Nombre total de cercles :",
    len(fleur.cercles)
)



# ----------------------------------------------------------
# Vérifications générales
# ----------------------------------------------------------

# print("\n--- VERIFICATIONS ---")


# assert len(fleur.cercles) == 19

# print(
#     "✓ 19 cercles générés"
# )



# assert fleur.cercle_central is not None

# print(
#     "✓ Cercle central présent"
# )



# # ----------------------------------------------------------
# # Vérification des couronnes
# # ----------------------------------------------------------

# print("\n--- COURONNES ---")


# for numero, couronne in enumerate(
#     fleur.cercles_couronnes
# ):

#     print(
#         f"Couronne {numero} : {len(couronne)} cercles"
#     )



# assert len(
#     fleur.cercles_couronnes[0]
# ) == 1


# assert len(
#     fleur.cercles_couronnes[1]
# ) == 6


# assert len(
#     fleur.cercles_couronnes[2]
# ) == 12



# print(
#     "✓ Organisation des couronnes correcte"
# )



# # ----------------------------------------------------------
# # Réseau interne
# # ----------------------------------------------------------

# print("\n--- RESEAU ---")


# assert fleur.reseau is not None


# assert len(
#     fleur.reseau.couronnes_points
# ) == 3



# print(
#     "✓ Réseau hexagonal conservé"
# )



# ----------------------------------------------------------
# Affichage
# ----------------------------------------------------------

print("\n--- AFFICHAGE ---")


afficheur = Afficheur()


afficheur.figure(
    fleur
)


afficheur.afficher(
    "Fleur de Vie"
)



print(
    "\nTous les tests de la Fleur de Vie sont terminés."
)