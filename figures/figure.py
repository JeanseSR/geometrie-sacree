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

    # AJOUT étape 3 : marqueur "trait de construction" (trait d'aide).
    #
    # construction[i] correspond à objets[i] :
    #   False -> trait RÉEL : il sera fabriqué (imprimé, gravé,
    #            découpé, mis en relief, évidé en pochoir...)
    #   True  -> trait de CONSTRUCTION : il sert à bâtir la figure
    #            (ex. les 13 cercles du Métatron) mais n'est
    #            jamais fabriqué.
    #
    # Le nom reprend le vocabulaire FreeCAD :
    #   sketch.addGeometry(geometrie, construction)
    #
    # Pourquoi dans Figure et pas dans Segment / Cercle... ?
    # -> la géométrie reste pure (un segment ne sait pas comment
    #    il sera fabriqué) et le marqueur est géré à UN seul endroit.
    construction: list[bool] = field(
        default_factory=list
    )

    def __post_init__(self) -> None:
        # AJOUT étape 3 : si une Figure est créée avec
        # objets=[...] déjà remplis, on complète `construction`
        # avec la valeur par défaut de chaque objet, pour que
        # les deux listes aient toujours la même longueur.
        while len(self.construction) < len(self.objets):
            objet = self.objets[len(self.construction)]
            self.construction.append(
                self._construction_par_defaut(objet)
            )

    # ==========================================================
    # AJOUT
    # ==========================================================

    @staticmethod
    def _construction_par_defaut(
        objet: ObjetGeometrique
    ) -> bool:
        """
        AJOUT étape 3 : valeur utilisée quand on ne précise rien.

        Un Point n'a pas de matière (pas de longueur ni de surface) :
        il est toujours un repère de construction.
        Tout le reste est un trait réel par défaut.
        """
        return isinstance(objet, Point)

    def ajouter(
        self,
        objet: ObjetGeometrique,
        construction: bool | None = None
    ) -> None:
        """
        Ajoute un objet à la figure.

        construction :
            None  -> valeur par défaut (Point = construction,
                     le reste = trait réel)
            True  -> trait de construction (jamais fabriqué)
            False -> trait réel (fabriqué)
        """
        # MODIFICATION étape 3 : ajout du paramètre `construction`
        # (optionnel : tout le code existant reste valable).
        if construction is None:
            construction = self._construction_par_defaut(objet)

        self.objets.append(objet)
        self.construction.append(construction)

    def ajouter_plusieurs(
        self,
        *objets: ObjetGeometrique,
        construction: bool | None = None
    ) -> None:
        """Ajoute plusieurs objets (même marqueur pour tous)."""
        # MODIFICATION étape 3 : passe par ajouter() pour que
        # `construction` reste aligné sur `objets`.
        for objet in objets:
            self.ajouter(objet, construction)

    # AJOUT étape 3 : association de figures.
    def ajouter_figure(
        self,
        autre: "Figure"
    ) -> None:
        """
        Ajoute tous les objets d'une autre figure,
        en conservant leur marqueur de construction.

        Base des futures associations de figures
        (ex. Fleur de Vie + Métatron sur la même plaque).
        Les métadonnées (nom, paramètres...) de `autre`
        ne sont pas reprises : seule la géométrie l'est.
        """
        for objet, construction in autre.elements():
            self.ajouter(objet, construction)

    # ==========================================================
    # SUPPRESSION
    # ==========================================================

    def supprimer(
        self,
        objet: ObjetGeometrique
    ) -> None:

        # MODIFICATION étape 3 : on supprime aussi le marqueur
        # correspondant (même position) pour garder les listes alignées.
        index = self.objets.index(objet)

        del self.objets[index]
        del self.construction[index]

    def vider(self) -> None:

        self.objets.clear()
        # AJOUT étape 3
        self.construction.clear()

    # ==========================================================
    # PARCOURS AVEC MARQUEUR (AJOUT étape 3)
    # ==========================================================

    def elements(
        self
    ) -> Iterator[tuple[ObjetGeometrique, bool]]:
        """
        Parcourt les objets avec leur marqueur :

            for objet, construction in figure.elements():
                ...
        """
        return zip(self.objets, self.construction)

    @property
    def objets_reels(self) -> list[ObjetGeometrique]:
        """Objets à fabriquer (construction = False)."""
        return [
            o for o, c in self.elements()
            if not c
        ]

    @property
    def objets_construction(self) -> list[ObjetGeometrique]:
        """Objets de construction (jamais fabriqués)."""
        return [
            o for o, c in self.elements()
            if c
        ]

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

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():
            nouvelle.ajouter(
                objet.translation(dx, dy),
                construction  # MODIFICATION étape 3 : marqueur conservé
            )

        return nouvelle

    def rotation(
        self,
        angle: float
    ) -> "Figure":

        # CORRECTION étape 1 : Figure() -> self._copie_vide()
        nouvelle = self._copie_vide()

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():
            nouvelle.ajouter(
                objet.rotation(angle),
                construction  # MODIFICATION étape 3 : marqueur conservé
            )

        return nouvelle

    def rotation_autour(
        self,
        centre: Point,
        angle: float
    ) -> "Figure":

        # CORRECTION étape 1 : Figure() -> self._copie_vide()
        nouvelle = self._copie_vide()

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():
            nouvelle.ajouter(
                objet.rotation_autour(
                    centre,
                    angle
                ),
                construction  # MODIFICATION étape 3 : marqueur conservé
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

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():

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
                ),
                construction  # MODIFICATION étape 3 : marqueur conservé
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

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():
            nouvelle.ajouter(
                objet.echelle(facteur),
                construction  # MODIFICATION étape 3 : marqueur conservé
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

        # MODIFICATION étape 3 : on parcourt aussi le marqueur de construction
        for objet, construction in self.elements():
            nouvelle.ajouter(
                objet.echelle_autour(
                    centre,
                    facteur
                ),
                construction  # MODIFICATION étape 3 : marqueur conservé
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
            f"{len(self.bandes_segments)} bande(s), "
            # AJOUT étape 3 : nombre d'objets de construction
            f"dont {len(self.objets_construction)} de construction"
            ")"
        )

    # ==========================================================
    # MÉTHODES D'AJOUT SPÉCIFIQUES
    # ==========================================================

    def ajouter_point(
        self,
        point: Point,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter(point, construction)

    def ajouter_segment(
        self,
        segment: Segment,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter(segment, construction)

    def ajouter_cercle(
        self,
        cercle: Cercle,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter(cercle, construction)

    def ajouter_polygone(
        self,
        polygone: Polygone,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter(polygone, construction)

    def ajouter_couronne(
        self,
        couronne: Couronne,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter(couronne, construction)

    # ==========================================================
    # AJOUTS MULTIPLES
    # ==========================================================

    def ajouter_points(
        self,
        *points: Point,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter_plusieurs(*points, construction=construction)

    def ajouter_segments(
        self,
        *segments: Segment,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter_plusieurs(*segments, construction=construction)

    def ajouter_cercles(
        self,
        *cercles: Cercle,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter_plusieurs(*cercles, construction=construction)

    def ajouter_polygones(
        self,
        *polygones: Polygone,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter_plusieurs(*polygones, construction=construction)

    def ajouter_couronnes(
        self,
        *couronnes: Couronne,
        construction: bool | None = None  # AJOUT étape 3
    ) -> None:

        self.ajouter_plusieurs(*couronnes, construction=construction)

    # ==========================================================
    # COPIE
    # ==========================================================

    def copier(self) -> "Figure":

        # CORRECTION étape 1 : bloc de 7 lignes -> self._copie_vide()
        nouvelle = self._copie_vide()

        # MODIFICATION étape 3 : ajouter_figure recopie les objets
        # AVEC leur marqueur de construction (ajouter_plusieurs
        # les aurait tous remis à la valeur par défaut).
        nouvelle.ajouter_figure(self)

        return nouvelle