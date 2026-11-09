from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Vecteur:
    """
    Représente un vecteur du plan.
    Toutes les coordonnées sont exprimées en millimètres.
    """

    x: float
    y: float

    # ------------------------------------------------------------------
    # Propriétés
    # ------------------------------------------------------------------

    @property
    def norme(self) -> float:
        """Longueur du vecteur."""
        return math.hypot(self.x, self.y)

    @property
    def norme2(self) -> float:
        """Carré de la norme."""
        return self.x**2 + self.y**2

    @property
    def unitaire(self) -> "Vecteur":
        """Retourne le vecteur unitaire."""
        n = self.norme

        if n == 0:
            raise ValueError("Impossible de normaliser un vecteur nul.")

        return Vecteur(
            self.x / n,
            self.y / n
        )

    @property
    def angle(self) -> float:
        """Angle du vecteur en degrés."""
        return math.degrees(
            math.atan2(self.y, self.x)
        )

    # ------------------------------------------------------------------
    # Opérations
    # ------------------------------------------------------------------

    def __add__(self, autre: "Vecteur") -> "Vecteur":
        return Vecteur(
            self.x + autre.x,
            self.y + autre.y
        )

    def __sub__(self, autre: "Vecteur") -> "Vecteur":
        return Vecteur(
            self.x - autre.x,
            self.y - autre.y
        )

    def __mul__(self, scalaire: float) -> "Vecteur":
        return Vecteur(
            self.x * scalaire,
            self.y * scalaire
        )

    def __rmul__(self, scalaire: float) -> "Vecteur":
        return self * scalaire

    def __truediv__(self, scalaire: float) -> "Vecteur":

        if scalaire == 0:
            raise ZeroDivisionError

        return Vecteur(
            self.x / scalaire,
            self.y / scalaire
        )

    # ------------------------------------------------------------------
    # Géométrie
    # ------------------------------------------------------------------

    def produit_scalaire(self, autre: "Vecteur") -> float:
        return (
            self.x * autre.x +
            self.y * autre.y
        )

    def produit_vectoriel(self, autre: "Vecteur") -> float:
        return (
            self.x * autre.y -
            self.y * autre.x
        )

    def rotation(self, angle: float) -> "Vecteur":
        """Rotation en degrés."""
        a = math.radians(angle)

        c = math.cos(a)
        s = math.sin(a)

        return Vecteur(
            self.x * c - self.y * s,
            self.x * s + self.y * c
        )

    @classmethod
    def depuis_points(cls, A, B):
        """Construit le vecteur AB."""
        return cls(
            B.x - A.x,
            B.y - A.y
        )

    @property
    def oppose(self):
        return Vecteur(
            -self.x,
            -self.y
        )

    @property
    def normale_gauche(self):
        return Vecteur(
            -self.y,
            self.x
        )

    @property
    def normale_droite(self):
        return Vecteur(
            self.y,
            -self.x
        )

    def angle_avec(self, autre):

        return math.degrees(
            math.atan2(
                self.produit_vectoriel(autre),
                self.produit_scalaire(autre)
            )
        )