from __future__ import annotations

from geometrie.point import Point


class SVGWriter:
    """
    Écriture d'un fichier SVG.
    """

    def __init__(self, boite):

        self.boite = boite
        self.lignes: list[str] = []

    # ==========================================================
    # DOCUMENT
    # ==========================================================

    def begin(self):

        self.lignes.append('<?xml version="1.0" encoding="UTF-8"?>')

        self.lignes.append(

            f'<svg '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'width="{self.boite.largeur}" '
            f'height="{self.boite.hauteur}" '
            f'viewBox="'
            f'{self.boite.xmin} '
            f'{self.boite.ymin} '
            f'{self.boite.largeur} '
            f'{self.boite.hauteur}'
            f'">'

        )

    def end(self):

        self.lignes.append("</svg>")

    # ==========================================================
    # OBJETS
    # ==========================================================

    def point(
        self,
        point: Point,
        rayon: float = 1.5,
        couleur: str = "black"
    ):

        self.lignes.append(

            f'<circle '
            f'cx="{point.x}" '
            f'cy="{point.y}" '
            f'r="{rayon}" '
            f'fill="{couleur}" />'

        )

    def segment(
        self,
        segment,
        couleur="black",
        epaisseur=1
    ):

        self.lignes.append(

            f'<line '
            f'x1="{segment.debut.x}" '
            f'y1="{segment.debut.y}" '
            f'x2="{segment.fin.x}" '
            f'y2="{segment.fin.y}" '
            f'stroke="{couleur}" '
            f'stroke-width="{epaisseur}" />'

        )

    def cercle(
        self,
        cercle,
        couleur="black",
        epaisseur=1,
        remplissage="none"
    ):

        self.lignes.append(

            f'<circle '
            f'cx="{cercle.centre.x}" '
            f'cy="{cercle.centre.y}" '
            f'r="{cercle.rayon}" '
            f'fill="{remplissage}" '
            f'stroke="{couleur}" '
            f'stroke-width="{epaisseur}" />'

        )

    def polygone(
        self,
        polygone,
        couleur="black",
        epaisseur=1,
        remplissage="none"
    ):

        points = " ".join(

            f"{p.x},{p.y}"

            # CORRECTION étape 1 : `points` -> `sommets`
            for p in polygone.sommets

        )

        self.lignes.append(

            f'<polygon '
            f'points="{points}" '
            f'fill="{remplissage}" '
            f'stroke="{couleur}" '
            f'stroke-width="{epaisseur}" />'

        )

    # ==========================================================
    # SAUVEGARDE
    # ==========================================================

    def save(
        self,
        fichier: str
    ):

        with open(
            fichier,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("\n".join(self.lignes))