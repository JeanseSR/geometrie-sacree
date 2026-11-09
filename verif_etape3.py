"""Vérification étape 3 : Point figé + marqueur de construction (+ non-régression étapes 1 et 2).
Usage : python verif_etape3.py [dossier_bibliotheque]   (défaut : dossier courant)"""
import sys, os, tempfile, traceback
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else ".")
import matplotlib; matplotlib.use("Agg")   # pas de fenêtre

from geometrie.point import Point
from geometrie.polygone import Polygone
from figures.figure import Figure
from figures.fleur_de_vie import FleurDeVie
from figures.fruit_de_vie import FruitDeVie
from figures.cube_metatron import CubeMetatron
from figures.graine_de_vie import GraineDeVie
from figures.vesica_piscis import VesicaPiscis

tmp = tempfile.mkdtemp()
hexa = Polygone.regulier(Point(0, 0), 10, 6)
f_poly = Figure(nom="Poly"); f_poly.ajouter_polygone(hexa)
fleur = FleurDeVie(Point(0, 0), 10, 2)
ok = ko = 0

def essai(nom, fn):
    global ok, ko
    try:
        r = fn(); print(f"OK  {nom}" + (f"  -> {r}" if r is not None else "")); ok += 1
    except Exception as e:
        print(f"KO  {nom}  -> {type(e).__name__}: {e}"); ko += 1

# 1. Polygone.boite_englobante
essai("Polygone.boite_englobante", lambda: hexa.boite_englobante)
# 3. __repr__ de toutes les figures
for f in (Figure(), fleur, FruitDeVie(Point(0,0),10), CubeMetatron(Point(0,0),10), GraineDeVie(Point(0,0),10), VesicaPiscis(Point(0,0),10)):
    essai(f"repr {type(f).__name__}", lambda f=f: Figure.__repr__(f))
# 4. mise_a_echelle
essai("Figure.mise_a_echelle (cercles)", lambda: len(fleur.mise_a_echelle(2).cercles))
# 5. métadonnées conservées
essai("translation garde le nom", lambda: fleur.translation(1, 1).nom == "Fleur de Vie" or (_ for _ in ()).throw(AssertionError("nom perdu")))
essai("rotation garde les paramètres", lambda: fleur.rotation(30).parametres == fleur.parametres or (_ for _ in ()).throw(AssertionError("paramètres perdus")))
essai("rotation_autour garde l'unité", lambda: fleur.rotation_autour(Point(1,1), 30).unite == "mm" or (_ for _ in ()).throw(AssertionError("unité perdue")))
# 2. exports de polygones
from export.svg_exporter import SVGExporter
essai("SVG polygone", lambda: SVGExporter().export(f_poly, os.path.join(tmp, "p.svg")))
from export.freecad_code_exporter import FreeCADCodeExporter
essai("FreeCAD sketch polygone", lambda: FreeCADCodeExporter().export(f_poly, os.path.join(tmp, "p.py")))
# 6. MatplotlibExporter
from export.matplotlib_exporter import MatplotlibExporter
essai("MatplotlibExporter fleur", lambda: MatplotlibExporter().export(fleur, os.path.join(tmp, "f.png")))
essai("MatplotlibExporter polygone", lambda: MatplotlibExporter().export(f_poly, os.path.join(tmp, "p.png")))
# Non-régression : comptes exacts
essai("Fleur 19 cercles", lambda: len(fleur.cercles) == 19 or (_ for _ in ()).throw(AssertionError))
essai("Métatron 78 segments", lambda: len(CubeMetatron(Point(0,0),10).segments_metatron) == 78 or (_ for _ in ()).throw(AssertionError))

# --- Étape 2 : les méthodes conservées marchent toujours ---
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.bande_segment import BandeSegment
from geometrie.vecteur import Vecteur
from geometrie.reseau_hexagonal_axial import ReseauHexagonalAxial
seg = Segment(Point(0, 0), Point(10, 0))
def verifie(cond, msg):
    if not cond: raise AssertionError(msg)
    return True
essai("Segment.translation", lambda: verifie(seg.translation(1, 2).debut.y == 2, "translation"))
essai("Segment.echelle", lambda: verifie(seg.echelle(2).longueur == 20, "echelle"))
essai("Segment.echelle_autour", lambda: verifie(seg.echelle_autour(Point(10, 0), 2).debut.x == -10, "echelle_autour"))
essai("Cercle.contient", lambda: verifie(Cercle(Point(0, 0), 5).contient(Point(3, 4)), "contient"))
essai("BandeSegment.echelle_autour", lambda: verifie(BandeSegment(Point(0,0), Point(10,0), 1).echelle_autour(Point(0,0), 2).largeur == 2, "bande"))
essai("Point - Point -> Vecteur", lambda: verifie(isinstance(Point(3, 4) - Point(0, 0), Vecteur), "sub"))
essai("Réseau axial 19 points / 3 couronnes", lambda: verifie(len(ReseauHexagonalAxial(Point(0,0), 1, 2)) == 19 and len(ReseauHexagonalAxial(Point(0,0), 1, 2).couronnes_points) == 3, "reseau"))
essai("Segment sans alias mise_a_echelle", lambda: verifie(not hasattr(seg, "mise_a_echelle"), "alias encore présent"))
# --- Étape 2 : les fichiers supprimés ont bien disparu ---
racine = sys.path[0]
for f in ("geometrie/reseau_hexagonal.py", "geometrie/tranformation.py", "export/writers/freecad_writer.py",
          "export/dxf_exporter.py", "export/pdf_exporter.py", "export/png_exporter.py", "export/styles.py",
          "tests/test_reseau_hexagonal.py"):
    essai(f"supprimé : {f}", lambda f=f: verifie(not os.path.exists(os.path.join(racine, f)), "encore présent"))

# =====================================================================
# ÉTAPE 3
# =====================================================================
import dataclasses
from geometrie.segment import Segment
from fabrication.epaisseur_trait import EpaisseurTrait

# --- Point figé ---
def modifier_point():
    p = Point(1, 2)
    try:
        p.x = 5
    except dataclasses.FrozenInstanceError:
        return True
    raise AssertionError("Point encore modifiable")
essai("Point non modifiable", modifier_point)
essai("Point hachable (set dédoublonne)", lambda: verifie(len({Point(1, 2), Point(1, 2), Point(3, 4)}) == 2, "set"))
essai("Cercle hachable", lambda: verifie(len({Cercle(Point(0, 0), 5), Cercle(Point(0, 0), 5)}) == 1, "set cercle"))

# --- Valeurs par défaut ---
def defauts():
    f = Figure()
    f.ajouter(Point(0, 0)); f.ajouter(seg); f.ajouter(Cercle(Point(0, 0), 3))
    verifie(list(f.construction) == [True, False, False], f"obtenu {f.construction}")
    return f.construction
essai("Défaut : Point=construction, reste=réel", defauts)

# --- Métatron ---
m = CubeMetatron(Point(0, 0), 10)
essai("Métatron : 78 traits réels (segments)", lambda: verifie(len(m.objets_reels) == 78 and all(isinstance(o, Segment) for o in m.objets_reels), f"{len(m.objets_reels)}"))
essai("Métatron : 26 de construction (13 cercles + 13 points)", lambda: verifie(len(m.objets_construction) == 26, f"{len(m.objets_construction)}"))
essai("Fleur : 19 cercles réels", lambda: verifie(len(fleur.objets_reels) == 19, "fleur"))

# --- Transformations : marqueur conservé ---
for nom, fn in [("translation", lambda: m.translation(5, 5)), ("rotation", lambda: m.rotation(30)),
                ("rotation_autour", lambda: m.rotation_autour(Point(1, 1), 30)), ("echelle", lambda: m.echelle(2)),
                ("echelle_autour", lambda: m.echelle_autour(Point(1, 1), 2)), ("mise_a_echelle", lambda: m.mise_a_echelle(2)),
                ("copier", lambda: m.copier())]:
    essai(f"{nom} garde le marqueur", lambda fn=fn: verifie(fn().construction == m.construction, "marqueur perdu"))

# --- Association de figures ---
def association():
    f = Figure(nom="Association")
    f.ajouter_figure(fleur); f.ajouter_figure(m)
    verifie(len(f) == len(fleur) + len(m), "taille")
    verifie(len(f.objets_reels) == 19 + 78, f"réels {len(f.objets_reels)}")
    return f
essai("ajouter_figure (Fleur + Métatron)", association)

# --- supprimer garde les listes alignées ---
def suppression():
    f = Figure(); a = Point(0, 0)
    f.ajouter(a); f.ajouter(seg)
    f.supprimer(a)
    verifie(f.objets == [seg] and f.construction == [False], "désalignement")
    return True
essai("supprimer garde l'alignement", suppression)
essai("Figure(objets=[...]) complète le marqueur", lambda: verifie(Figure(objets=[Point(0, 0), seg]).construction == [True, False], "post_init"))

# --- Épaisseur de trait : construction non épaissie ---
def epaisseur():
    e = EpaisseurTrait(largeur=0.5).appliquer(m)
    verifie(len(e.bandes_segments) == 78, f"bandes {len(e.bandes_segments)}")
    verifie(len(e.couronnes_geometriques) == 0, f"couronnes {len(e.couronnes_geometriques)}")
    verifie(len(e.objets_construction) == 26, "construction")
    return "78 bandes, 0 couronne"
essai("EpaisseurTrait ignore la construction", epaisseur)

# --- Export Sketch FreeCAD ---
def sketch():
    chemin = os.path.join(tmp, "metatron.py")
    exp = FreeCADCodeExporter()
    exp.export(m, chemin); taille1 = len(open(chemin, encoding="utf-8").read())
    exp.export(m, chemin); txt = open(chemin, encoding="utf-8").read()
    verifie(len(txt) == taille1, "le 2e export a doublé le script")
    vrais = txt.count("\n    True\n"); faux = txt.count("\n    False\n")
    verifie(vrais == 13 and faux == 78, f"True={vrais} False={faux}")
    compile(txt, chemin, "exec")   # le script généré est du Python valide
    return "13 cercles construction, 78 segments réels"
essai("Sketch FreeCAD : marqueur + export répétable", sketch)
print(f"\n{ok} OK / {ko} KO")
