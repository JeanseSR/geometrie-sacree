from geometrie.point import Point

from figures.cube_metatron import CubeMetatron

from affichage.affichage import Afficheur


cube = CubeMetatron(

    centre=Point(0, 0),

    rayon=40,

    couronnes=2
)

print()

print("=" * 60)
print("CUBE DE MÉTATRON")
print("=" * 60)

print()

print("Cercles :", len(cube.cercles))
print("Centres :", len(cube.centres))
print("Segments :", len(cube.segments_metatron))

print()

# assert len(cube.cercles) == 13
# assert len(cube.centres) == 13
# assert len(cube.segments_metatron) == 78

print("Objets :", len(cube.objets))
print("Points :", len(cube.points))
print("Segments :", len(cube.segments))
print("Cercles :", len(cube.cercles))

print("Tests OK")

aff = Afficheur()

aff.figure(cube)

aff.afficher("Cube de Métatron")