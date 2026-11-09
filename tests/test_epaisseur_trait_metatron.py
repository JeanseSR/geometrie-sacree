from geometrie.point import Point

from figures.cube_metatron import CubeMetatron
from fabrication.epaisseur_trait import EpaisseurTrait


print("=" * 60)
print("TEST EPAISSEUR TRAIT — METATRON")
print("=" * 60)


# ==========================================================
# 1. METATRON ORIGINAL
# ==========================================================

figure = CubeMetatron(
    centre=Point(0, 0),
    rayon=3.14,
    couronnes=2
)


print()
print("Figure originale")

print(
    "Cercles :",
    len(figure.cercles)
)

print(
    "Segments :",
    len(figure.segments)
)


assert len(figure.cercles) == 13
assert len(figure.segments) == 78


# ==========================================================
# 2. EPAISSEUR DE TRAIT
# ==========================================================

fabrication = EpaisseurTrait(
    largeur=0.4
)

figure2 = fabrication.appliquer(
    figure
)


# ==========================================================
# 3. RESULTAT
# ==========================================================

print()
print("Figure fabrication")

print(
    "Couronnes :",
    len(figure2.couronnes_geometriques)
)

print(
    "Bandes :",
    len(figure2.bandes_segments)
)


# ==========================================================
# 4. VALIDATIONS
# ==========================================================

assert len(
    figure2.couronnes_geometriques
) == 13

assert len(
    figure2.bandes_segments
) == 78


for couronne in figure2.couronnes_geometriques:

    assert abs(
        couronne.largeur - 0.4
    ) < 1e-9


for bande in figure2.bandes_segments:

    assert abs(
        bande.largeur - 0.4
    ) < 1e-9


print()
print("Largeur du trait : 0.4 mm")


print()
print("=" * 60)
print("TEST EPAISSEUR TRAIT METATRON : OK")
print("=" * 60)