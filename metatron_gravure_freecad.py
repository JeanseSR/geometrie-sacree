# ======================================================
# MODELE FREECAD — GRAVURE
# Généré automatiquement
# ======================================================

import FreeCAD as App
import Part
import math

doc = App.newDocument("Gravure")

# Paramètres
PLAQUE_LARGEUR = 70
PLAQUE_HAUTEUR = 70
PLAQUE_EPAISSEUR = 2
PROFONDEUR_GRAVURE = 1

# Plaque
plaque = Part.makeBox(
    PLAQUE_LARGEUR,
    PLAQUE_HAUTEUR,
    PLAQUE_EPAISSEUR,
    App.Vector(
        -PLAQUE_LARGEUR / 2,
        -PLAQUE_HAUTEUR / 2,
        0
    )
)

# Outils de gravure
outils = []

# Couronne
centre = App.Vector(0.0, 0.0, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-5.007201646090535, -8.672727654771322, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(5.007201646090535, -8.672727654771322, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(10.01440329218107, 0.0, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(5.007201646090535, 8.672727654771322, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-5.007201646090535, 8.672727654771322, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-10.01440329218107, 0.0, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-10.01440329218107, -17.345455309542643, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(10.01440329218107, -17.345455309542643, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(20.02880658436214, 0.0, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(10.01440329218107, 17.345455309542643, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-10.01440329218107, 17.345455309542643, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Couronne
centre = App.Vector(-20.02880658436214, 0.0, PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE)
exterieur = Part.makeCylinder(10.97119341563786, PROFONDEUR_GRAVURE, centre)
interieur = Part.makeCylinder(9.05761316872428, PROFONDEUR_GRAVURE, centre)
outil = exterieur.cut(interieur)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -5.007201646090535
y2 = -8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 5.007201646090535
y2 = -8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 0.0
y1 = 0.0
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(0.0, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 5.007201646090535
y2 = -8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = -5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = -8.672727654771322
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = 5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = -5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = -8.672727654771322
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, -8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = 5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = -5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 0.0
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = -5.007201646090535
y2 = 8.672727654771322
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 5.007201646090535
y1 = 8.672727654771322
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -5.007201646090535
y1 = 8.672727654771322
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-5.007201646090535, 8.672727654771322, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = -10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 0.0
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = -17.345455309542643
x2 = 10.01440329218107
y2 = -17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = -17.345455309542643
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = -17.345455309542643
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = -17.345455309542643
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = -17.345455309542643
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = -17.345455309542643
x2 = 20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = -17.345455309542643
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = -17.345455309542643
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = -17.345455309542643
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, -17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 20.02880658436214
y1 = 0.0
x2 = 10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(20.02880658436214, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 20.02880658436214
y1 = 0.0
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(20.02880658436214, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 20.02880658436214
y1 = 0.0
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(20.02880658436214, 0.0, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 17.345455309542643
x2 = -10.01440329218107
y2 = 17.345455309542643
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = 10.01440329218107
y1 = 17.345455309542643
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(10.01440329218107, 17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Bande de segment
x1 = -10.01440329218107
y1 = 17.345455309542643
x2 = -20.02880658436214
y2 = 0.0
largeur = 1.91358024691358
dx = x2 - x1
dy = y2 - y1
longueur = math.hypot(dx, dy)
angle = math.degrees(math.atan2(dy, dx))
rectangle = Part.makeBox(
    longueur,
    largeur,
    PROFONDEUR_GRAVURE,
    App.Vector(
        0,
        -largeur / 2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
rectangle.rotate(
    App.Vector(0, 0, 0),
    App.Vector(0, 0, 1),
    angle
)
rectangle.translate(
    App.Vector(-10.01440329218107, 17.345455309542643, 0)
)
r = largeur / 2
bout1 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x1,
        y1,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
bout2 = Part.makeCylinder(
    r,
    PROFONDEUR_GRAVURE,
    App.Vector(
        x2,
        y2,
        PLAQUE_EPAISSEUR - PROFONDEUR_GRAVURE
    )
)
outil = rectangle.fuse(bout1).fuse(bout2)
outils.append(outil)

# Union des outils de gravure
outil_total = None

for outil in outils:
    if outil_total is None:
        outil_total = outil
    else:
        outil_total = outil_total.fuse(outil)

# Gravure dans la plaque
resultat = plaque.cut(outil_total)

objet = doc.addObject("PartDesign::Feature", "MetatronGrave")
objet.Label = "Cube de Métatron — gravure"
objet.Shape = resultat

info = doc.addObject("App::FeaturePython", "Informations")
info.addProperty("App::PropertyString", "Type", "Fabrication")
info.Type = "Cube de Métatron gravé"
info.addProperty("App::PropertyLength", "ProfondeurGravure", "Fabrication")
info.ProfondeurGravure = PROFONDEUR_GRAVURE
info.addProperty("App::PropertyLength", "LargeurPlaque", "Fabrication")
info.LargeurPlaque = PLAQUE_LARGEUR
info.addProperty("App::PropertyLength", "HauteurPlaque", "Fabrication")
info.HauteurPlaque = PLAQUE_HAUTEUR

objet.ViewObject.ShapeColor = (0.82, 0.82, 0.82)
objet.ViewObject.LineColor = (0.15, 0.15, 0.15)

doc.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.activeDocument().activeView().fitAll()

# Pour enregistrer directement :
# doc.saveAs("metatron_gravure.FCStd")
