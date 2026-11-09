from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.polygone import Polygone
from geometrie.couronne import Couronne
from geometrie.boite_englobante import BoiteEnglobante
from geometrie.bande_segment import BandeSegment


ObjetGeometrique = (
    Point
    | Segment
    | Cercle
    | Polygone
    | Couronne
    | BandeSegment
)


@dataclass
class Figure:
    """
    Représente une figure géométrique composée
    de plusieurs objets géométriques.
    """

    # Métadonnées
    nom: str = "Figure"
    description: str = ""
    auteur: str = ""
    unite: str = "mm"  # mm cm in px
    tags: set[str] = field(default_factory=set)
    parametres: dict[str, float | int | str] = field(
        default_factory=dict
    )

    objets: list[ObjetGeometrique] = field(
        default_factory=list
    )

    # ==========================================================
    # AJOUT
    # ==========================================================

    def ajouter(
        self,
        objet: ObjetGeometrique
    ) -> None:
        """Ajoute un objet à la figure."""
        self.objets.append(objet)

    def ajouter_plusieurs(
        self,
        *objets: ObjetGeometrique
    ) -> None:
        """Ajoute plusieurs objets."""
        self.objets.extend(objets)

    # ==========================================================
    # SUPPRESSION
    # ==========================================================

    def supprimer(
        self,
        objet: ObjetGeometrique
    ) -> None:

        self.objets.remove(objet)

    def vider(self) -> None:

        self.objets.clear()

    # ==========================================================
    # FILTRES
    # ==========================================================

    @property
    def points(self) -> list[Point]:

        return [
            o for o in self.objets
            if isinstance(o, Point)
        ]

    @property
    def segments(self) -> list[Segment]:

        return [
            o for o in self.objets
            if isinstance(o, Segment)
        ]

    @property
    def cercles(self) -> list[Cercle]:

        return [
            o for o in self.objets
            if isinstance(o, Cercle)
        ]

    @property
    def polygones(self) -> list[Polygone]:

        return [
            o for o in self.objets
            if isinstance(o, Polygone)
        ]

    @property
    def couronnes_geometriques(self) -> list[Couronne]:

        return [
            o for o in self.objets
            if isinstance(o, Couronne)
        ]
    
    @property
    def bandes_segments(self) -> list[BandeSegment]:

        return [
            o
            for o in self.objets
            if isinstance(o, BandeSegment)
        ]

    @property
    def est_vide(self) -> bool:
        return len(self.objets) == 0

    # ==========================================================
    # STATISTIQUES
    # ==========================================================

    @property
    def nombre_objets(self) -> int:

        return len(self.objets)

    # ==========================================================
    # BOITE ENGLOBANTE
    # ==========================================================

    @property
    def boite_englobante(self) -> BoiteEnglobante:
        """
        Boîte englobante de toute la figure.
        """

        if not self.objets:
            raise ValueError(
                "La figure est vide."
            )

        boite = self.objets[0].boite_englobante

        for objet in self.objets[1:]:

            boite = boite.union(
                objet.boite_englobante
            )

        return boite

    # ==========================================================
    # INFORMATIONS
    # ==========================================================

    @property
    def informations(self) -> dict:

        return {
            "nom": self.nom,
            "description": self.description,
            "auteur": self.auteur,
            "unite": self.unite,
            "tags": sorted(self.tags),
        }

    # ==========================================================
    # COPIE VIDE (métadonnées seules)
    # ==========================================================

    # CORRECTION étape 1 : nouvelle méthode.
    # Avant, translation / rotation / rotation_autour créaient
    # `Figure()` -> nom, description, unité, tags et paramètres
    # étaient perdus. Les autres méthodes recopiaient chacune
    # le même bloc de 7 lignes. Ce bloc est désormais écrit
    # une seule fois ici.
    def _copie_vide(self) -> "Figure":
        """
        Retourne une nouvelle Figure portant les mêmes
        métadonnées, mais sans aucun objet géométrique.

        tags et parametres sont copiés (set / dict neufs)
        pour que modifier la copie ne modifie pas l'original.
        """

        return Figure(
            nom=self.nom,
            description=self.description,
            auteur=self.auteur,
            unite=self.unite,
            tags=set(self.tags),
            parametres=dict(self.parametres),
        )

    # ==========================================================
    # TRANSFORMATIONS
    # ==========================================================

    def translation(
        self,
        dx: float,
        dy: float
    ) -> "Figure":

        # CORRECTION étape 1 : Figure() -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:
            nouvelle.ajouter(
                objet.translation(dx, dy)
            )

        return nouvelle

    def rotation(
        self,
        angle: float
    ) -> "Figure":

        # CORRECTION étape 1 : Figure() -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:
            nouvelle.ajouter(
                objet.rotation(angle)
            )

        return nouvelle

    def rotation_autour(
        self,
        centre: Point,
        angle: float
    ) -> "Figure":

        # CORRECTION étape 1 : Figure() -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:
            nouvelle.ajouter(
                objet.rotation_autour(
                    centre,
                    angle
                )
            )

        return nouvelle

    def mise_a_echelle(
        self,
        facteur: float,
        centre: Point = Point(0, 0)
    ) -> "Figure":
        """
        Retourne une nouvelle figure mise à l'échelle
        autour d'un centre.

        Le facteur est identique sur X et Y afin de
        conserver les proportions.
        """

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        # CORRECTION étape 1 : bloc de 7 lignes -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:

            # CORRECTION étape 1 : `objet.mise_a_echelle(facteur, centre)`
            # n'existe que sur Segment et BandeSegment
            # (Point, Cercle, Polygone, Couronne -> AttributeError).
            # Tous les objets possèdent `echelle_autour(centre, facteur)`,
            # qui fait exactement la même chose (attention : ordre
            # des arguments inversé).
            nouvelle.ajouter(
                objet.echelle_autour(
                    centre,
                    facteur
                )
            )

        return nouvelle


    def echelle(
        self,
        facteur: float
    ) -> "Figure":
        """
        Retourne une nouvelle figure mise à l'échelle
        par rapport à l'origine.
        """

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        # CORRECTION étape 1 : bloc de 7 lignes -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:
            nouvelle.ajouter(
                objet.echelle(facteur)
            )

        return nouvelle

    def echelle_autour(
        self,
        centre: Point,
        facteur: float
    ) -> "Figure":
        """
        Retourne une nouvelle figure mise à l'échelle
        autour d'un point.
        """

        if facteur <= 0:
            raise ValueError(
                "Le facteur d'échelle doit être positif."
            )

        # CORRECTION étape 1 : bloc de 7 lignes -> self._copie_vide()
        nouvelle = self._copie_vide()

        for objet in self.objets:
            nouvelle.ajouter(
                objet.echelle_autour(
                    centre,
                    facteur
                )
            )

        return nouvelle

    # ==========================================================
    # ITERATION
    # ==========================================================

    def __iter__(
        self
    ) -> Iterator[ObjetGeometrique]:

        return iter(self.objets)

    def __len__(self) -> int:
        return len(self.objets)

    def __getitem__(self, index):
        return self.objets[index]

    # ==========================================================
    # AFFICHAGE
    # ==========================================================

    def __repr__(self):

        return (
            "Figure("
            f"{len(self.points)} point(s), "
            f"{len(self.segments)} segment(s), "
            f"{len(self.cercles)} cercle(s), "
            f"{len(self.polygones)} polygone(s), "
            # CORRECTION étape 1 : `self.couronnes` n'existe pas sur
            # Figure (AttributeError) et vaut un int dans FruitDeVie /
            # CubeMetatron (TypeError sur len). La liste des objets
            # Couronne s'appelle `couronnes_geometriques`.
            f"{len(self.couronnes_geometriques)} couronne(s), "
            # AJOUT étape 1 : les bandes de segments n'étaient pas comptées.
            f"{len(self.bandes_segments)} bande(s)"
            ")"
        )

    # ==========================================================
    # MÉTHODES D'AJOUT SPÉCIFIQUES
    # ==========================================================

    def ajouter_point(
        self,
        point: Point
    ) -> None:

        self.ajouter(point)

    def ajouter_segment(
        self,
        segment: Segment
    ) -> None:

        self.ajouter(segment)

    def ajouter_cercle(
        self,
        cercle: Cercle
    ) -> None:

        self.ajouter(cercle)

    def ajouter_polygone(
        self,
        polygone: Polygone
    ) -> None:

        self.ajouter(polygone)

    def ajouter_couronne(
        self,
        couronne: Couronne
    ) -> None:

        self.ajouter(couronne)

    # ==========================================================
    # AJOUTS MULTIPLES
    # ==========================================================

    def ajouter_points(
        self,
        *points: Point
    ) -> None:

        self.ajouter_plusieurs(*points)

    def ajouter_segments(
        self,
        *segments: Segment
    ) -> None:

        self.ajouter_plusieurs(*segments)

    def ajouter_cercles(
        self,
        *cercles: Cercle
    ) -> None:

        self.ajouter_plusieurs(*cercles)

    def ajouter_polygones(
        self,
        *polygones: Polygone
    ) -> None:

        self.ajouter_plusieurs(*polygones)

    def ajouter_couronnes(
        self,
        *couronnes: Couronne
    ) -> None:

        self.ajouter_plusieurs(*couronnes)

    # ==========================================================
    # COPIE
    # ==========================================================

    def copier(self) -> "Figure":

        # CORRECTION étape 1 : bloc de 7 lignes -> self._copie_vide()
        nouvelle = self._copie_vide()

        nouvelle.ajouter_plusieurs(
            *self.objets
        )

        return nouvelle