"""Vérification étape 1 : chaque appel corrigé doit s'exécuter sans erreur."""
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
from export.writers.freecad_writer import FreeCADWriter
essai("FreeCADWriter polygone", lambda: FreeCADWriter().polygone(hexa))
# 6. MatplotlibExporter
from export.matplotlib_exporter import MatplotlibExporter
essai("MatplotlibExporter fleur", lambda: MatplotlibExporter().export(fleur, os.path.join(tmp, "f.png")))
essai("MatplotlibExporter polygone", lambda: MatplotlibExporter().export(f_poly, os.path.join(tmp, "p.png")))
# Non-régression : comptes exacts
essai("Fleur 19 cercles", lambda: len(fleur.cercles) == 19 or (_ for _ in ()).throw(AssertionError))
essai("Métatron 78 segments", lambda: len(CubeMetatron(Point(0,0),10).segments_metatron) == 78 or (_ for _ in ()).throw(AssertionError))
print(f"\n{ok} OK / {ko} KO")
