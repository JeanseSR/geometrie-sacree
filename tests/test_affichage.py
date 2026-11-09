from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.polygone import Polygone

from figures.figure import Figure
from affichage.affichage import Afficheur

fig = Figure()

fig.ajouter_point(Point(0, 0))

fig.ajouter_cercle(
    Cercle(
        Point(0, 0),
        10
    )
)

fig.ajouter_segment(
    Segment(
        Point(-10, 0),
        Point(10, 0)
    )
)

fig.ajouter_polygone(
    Polygone.regulier(
        Point(0, 0),
        8,
        6
    )
)

a = Afficheur()

a.figure(fig)

a.afficher("Premier test")