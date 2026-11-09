import FreeCAD as App
import Part

doc = App.ActiveDocument

# ==========================================================
# PARAMETRES
# ==========================================================

RAYON = 3.14
COURONNES = 2

EPAISSEUR_TRAIT = 0.4
PROFONDEUR_GRAVURE = 0.4

# Fleur centrée sur l'origine
CENTRE = App.Vector(0, 0, 0)


# ==========================================================
# CENTRES DE LA FLEUR DE VIE
# ==========================================================

centres = []

# centre
centres.append(CENTRE)

# couronnes
for couronne in range(1, COURONNES + 1):

    rayon_centres = RAYON * couronne

    for i in range(6):

        import math

        angle = math.radians(60 * i)

        x = rayon_centres * math.cos(angle)
        y = rayon_centres * math.sin(angle)

        centres.append(
            App.Vector(x, y, 0)
        )


# ==========================================================
# CREATION DES COURONNES
# ==========================================================

formes = []

rayon_interieur = (
    RAYON - EPAISSEUR_TRAIT / 2
)

rayon_exterieur = (
    RAYON + EPAISSEUR_TRAIT / 2
)

for centre in centres:

    cercle_ext = Part.Wire([
        Part.makeCircle(
            rayon_exterieur,
            centre
        )
    ])

    cercle_int = Part.Wire([
        Part.makeCircle(
            rayon_interieur,
            centre
        )
    ])

    face_ext = Part.Face(
        cercle_ext
    )

    face_int = Part.Face(
        cercle_int
    )

    anneau = face_ext.cut(
        face_int
    )

    formes.append(
        anneau
    )


# ==========================================================
# UNION DES TRAITS
# ==========================================================

gravure = formes[0]

for forme in formes[1:]:

    gravure = gravure.fuse(
        forme
    )


# Nettoyage géométrique
gravure = gravure.removeSplitter()


# ==========================================================
# EXTRUSION DE LA GRAVURE
# ==========================================================

outil = gravure.extrude(
    App.Vector(
        0,
        0,
        -PROFONDEUR_GRAVURE
    )
)


# ==========================================================
# AFFICHAGE
# ==========================================================

objet = doc.addObject(
    "PartDesign::Feature",
    "OutilGravure"
)

objet.Label = "Outil gravure Fleur de Vie"

objet.Shape = outil


doc.recompute()

Gui.activeDocument().activeView().fitAll()