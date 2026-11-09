from figures.figure import Figure
from geometrie.point import Point
from geometrie.couronne import Couronne

from export.exporter import Exporter


class TestExporter(Exporter):

    def __init__(self):
        self.couronnes_exportees = []

    def export_point(self, point):
        pass

    def export_segment(self, segment):
        pass

    def export_cercle(self, cercle):
        pass

    def export_polygone(self, polygone):
        pass

    def export_couronne(self, couronne):
        self.couronnes_exportees.append(couronne)


figure = Figure()

figure.ajouter(
    Couronne(
        centre=Point(0, 0),
        rayon_interieur=4,
        rayon_exterieur=5
    )
)

exporteur = TestExporter()

exporteur.exporter_objet(
    figure.objets[0]
)

assert len(
    exporteur.couronnes_exportees
) == 1

couronne = exporteur.couronnes_exportees[0]

assert couronne.rayon_interieur == 4
assert couronne.rayon_exterieur == 5

print("=" * 60)
print("TEST EXPORTER COURONNE")
print("=" * 60)
print()
print("Couronnes exportées :", len(
    exporteur.couronnes_exportees
))
print("Rayon intérieur     :", couronne.rayon_interieur)
print("Rayon extérieur     :", couronne.rayon_exterieur)
print()
print("OK")


couronne2 = Couronne(
    centre=Point(0, 0),
    rayon_interieur=4,
    rayon_exterieur=5
)

print(couronne2.cercle_interieur)
print(couronne2.cercle_exterieur)

assert couronne2.cercle_interieur.rayon == 4
assert couronne2.cercle_exterieur.rayon == 5