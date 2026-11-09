from fabrication.plaque import Plaque


print("=" * 60)
print("TEST PLAQUE")
print("=" * 60)


# ==========================================================
# PLAQUE
# ==========================================================

plaque = Plaque(
    largeur=70,
    hauteur=70,
    epaisseur=2,
)


# ==========================================================
# RESULTATS
# ==========================================================

print()
print("Plaque")

print(
    f"Largeur : {plaque.largeur:.6f} mm"
)

print(
    f"Hauteur : {plaque.hauteur:.6f} mm"
)

print(
    f"Épaisseur : {plaque.epaisseur:.6f} mm"
)

print(
    f"Volume : {plaque.volume:.6f} mm³"
)

print(
    "Centre :",
    plaque.centre
)

print(
    "X :",
    plaque.xmin,
    "→",
    plaque.xmax
)

print(
    "Y :",
    plaque.ymin,
    "→",
    plaque.ymax
)


# ==========================================================
# VALIDATIONS
# ==========================================================

assert plaque.largeur == 70
assert plaque.hauteur == 70
assert plaque.epaisseur == 2

assert plaque.volume == 9800

assert plaque.centre == (0.0, 0.0)

assert plaque.xmin == -35
assert plaque.xmax == 35

assert plaque.ymin == -35
assert plaque.ymax == 35


# ==========================================================
# VALIDATION ERREURS
# ==========================================================

for dimensions in (
    (0, 70, 2),
    (70, 0, 2),
    (70, 70, 0),
    (-70, 70, 2),
):

    try:

        Plaque(*dimensions)

    except ValueError:

        pass

    else:

        raise AssertionError(
            "Une dimension invalide aurait dû "
            "provoquer une ValueError."
        )


print()
print("=" * 60)
print("TEST PLAQUE : OK")
print("=" * 60)