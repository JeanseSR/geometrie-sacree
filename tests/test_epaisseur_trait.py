# from geometrie.point import Point

# from figures.fleur_de_vie import FleurDeVie

# from fabrication.epaisseur_trait import (
#     EpaisseurTrait
# )

# print("=" * 60)
# print("EPAISSEUR DE TRAIT")
# print("=" * 60)

# figure = FleurDeVie(

#     centre=Point(0, 0),

#     rayon=3.14,

#     couronnes=2

# )

# print()

# print("Figure originale")

# print("Cercles :", len(figure.cercles))

# print()

# fabrication = EpaisseurTrait(
#     largeur=0.4
# )

# figure2 = fabrication.appliquer(
#     figure
# )

# print("Figure fabrication")

# print("Cercles :", len(figure2.cercles))

# print()

# assert len(figure.cercles) == 19

# assert len(figure2.cercles) == 38

# print("OK")


from geometrie.point import Point
from geometrie.couronne import Couronne

from figures.fleur_de_vie import FleurDeVie
from fabrication.epaisseur_trait import EpaisseurTrait


print("=" * 60)
print("EPAISSEUR DE TRAIT")
print("=" * 60)

# ==========================================================
# FIGURE ORIGINALE
# ==========================================================

figure = FleurDeVie(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)

print()
print("Figure originale")
print("Cercles :", len(figure.cercles))

assert len(figure.cercles) == 19


# ==========================================================
# TRANSFORMATION
# ==========================================================

fabrication = EpaisseurTrait(
    largeur=0.4
)

figure2 = fabrication.appliquer(
    figure
)


# ==========================================================
# RESULTAT
# ==========================================================

print()
print("Figure fabrication")

print("Cercles  :", len(figure2.cercles))
print("Couronnes :", len(figure2.couronnes_geometriques))


# ==========================================================
# TESTS
# ==========================================================

assert len(figure2.cercles) == 0

assert len(figure2.couronnes_geometriques) == 19

for couronne in figure2.couronnes_geometriques:

    assert isinstance(
        couronne,
        Couronne
    )

    assert abs(
        couronne.largeur - 0.4
    ) < 1e-9


print()
print("Largeur des traits : 0.4 mm")

print()
print("OK")