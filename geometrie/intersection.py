from __future__ import annotations

import math

from .point import Point
from .segment import Segment
from .cercle import Cercle

# Tolérance utilisée pour les comparaisons de nombres flottants
EPSILON = 1e-9


# ==========================================================
# CERCLE / CERCLE
# ==========================================================

def cercle_cercle(
    c1: Cercle,
    c2: Cercle
) -> tuple[Point, Point] | None:
    """
    Retourne les points d'intersection de deux cercles.

    Retour
    ------
    tuple(Point, Point)
        Deux points d'intersection.

    None
        Si les cercles ne se coupent pas ou sont confondus.
    """

    x0, y0 = c1.centre.x, c1.centre.y
    x1, y1 = c2.centre.x, c2.centre.y

    r0 = c1.rayon
    r1 = c2.rayon

    dx = x1 - x0
    dy = y1 - y0

    d = math.hypot(dx, dy)

    # Cercles confondus
    if abs(d) < EPSILON and abs(r0 - r1) < EPSILON:
        return None

    # Trop éloignés
    if d > r0 + r1 + EPSILON:
        return None

    # Un cercle contenu dans l'autre
    if d < abs(r0 - r1) - EPSILON:
        return None

    a = (r0**2 - r1**2 + d**2) / (2 * d)

    h2 = r0**2 - a**2

    # Corrige les très petites erreurs numériques
    if abs(h2) < EPSILON:
        h2 = 0.0

    if h2 < 0:
        return None

    h = math.sqrt(h2)

    xm = x0 + a * dx / d
    ym = y0 + a * dy / d

    rx = -dy * h / d
    ry = dx * h / d

    p1 = Point(xm + rx, ym + ry)
    p2 = Point(xm - rx, ym - ry)

    return p1, p2


# ==========================================================
# SEGMENT / SEGMENT
# ==========================================================

def segment_segment(
    s1: Segment,
    s2: Segment
) -> Point | None:
    """
    Retourne le point d'intersection de deux segments.

    Retourne None si les segments ne se croisent pas.
    """

    x1, y1 = s1.debut.x, s1.debut.y
    x2, y2 = s1.fin.x, s1.fin.y

    x3, y3 = s2.debut.x, s2.debut.y
    x4, y4 = s2.fin.x, s2.fin.y

    denom = (
        (x1 - x2) * (y3 - y4)
        -
        (y1 - y2) * (x3 - x4)
    )

    if abs(denom) < EPSILON:
        return None

    px = (
        (x1 * y2 - y1 * x2) * (x3 - x4)
        -
        (x1 - x2) * (x3 * y4 - y3 * x4)
    ) / denom

    py = (
        (x1 * y2 - y1 * x2) * (y3 - y4)
        -
        (y1 - y2) * (x3 * y4 - y3 * x4)
    ) / denom

    # Vérifie que le point appartient bien aux deux segments

    def dans_segment(xa, ya, xb, yb, x, y):
        return (
            min(xa, xb) - EPSILON <= x <= max(xa, xb) + EPSILON
            and
            min(ya, yb) - EPSILON <= y <= max(ya, yb) + EPSILON
        )

    if (
        dans_segment(x1, y1, x2, y2, px, py)
        and
        dans_segment(x3, y3, x4, y4, px, py)
    ):
        return Point(px, py)

    return None