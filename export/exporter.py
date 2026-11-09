from __future__ import annotations

from abc import ABC, abstractmethod

from figures.figure import Figure

from geometrie.point import Point
from geometrie.segment import Segment
from geometrie.cercle import Cercle
from geometrie.polygone import Polygone
from geometrie.couronne import Couronne


class Exporter(ABC):
    """
    Classe abstraite de base de tous les exporteurs.

    Elle ne fait qu'une chose :
    parcourir une Figure et dispatcher
    les objets vers les méthodes spécialisées.
    """

    # ==========================================================
    # API PUBLIQUE
    # ==========================================================

    def export(
        self,
        figure: Figure
    ) -> None:

        self.debut_export(figure)

        for objet in figure:
            self.exporter_objet(objet)

        self.fin_export(figure)

    # ==========================================================
    # DISPATCH
    # ==========================================================

    def exporter_objet(self, objet) -> None:

        if isinstance(objet, Point):
            self.export_point(objet)

        elif isinstance(objet, Segment):
            self.export_segment(objet)

        elif isinstance(objet, Cercle):
            self.export_cercle(objet)
        
        elif isinstance(objet, Couronne):
            self.export_couronne(objet)

        elif isinstance(objet, Polygone):
            self.export_polygone(objet)

        else:
            raise TypeError(
                f"Type non supporté : {type(objet).__name__}"
            )

    # ==========================================================
    # HOOKS
    # ==========================================================

    def debut_export(
        self,
        figure: Figure
    ) -> None:
        pass

    def fin_export(
        self,
        figure: Figure
    ) -> None:
        pass

    # ==========================================================
    # OBJETS
    # ==========================================================

    @abstractmethod
    def export_point(
        self,
        point: Point
    ) -> None:
        ...

    @abstractmethod
    def export_segment(
        self,
        segment: Segment
    ) -> None:
        ...

    @abstractmethod
    def export_cercle(
        self,
        cercle: Cercle
    ) -> None:
        ...

    @abstractmethod
    def export_couronne(
        self,
        couronne: Couronne
    ) -> None:
        ...

    @abstractmethod
    def export_polygone(
        self,
        polygone: Polygone
    ) -> None:
        ...