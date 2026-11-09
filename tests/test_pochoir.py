from fabrication.pochoir import Pochoir


print("=" * 60)
print("TEST POCHOIR")
print("=" * 60)


# ==========================================================
# CREATION
# ==========================================================

pochoir = Pochoir(
    largeur=70,
    hauteur=70,
    epaisseur=2,
)


# ==========================================================
# RESULTATS
# ==========================================================

print()
print("Pochoir")

print(
    f"Largeur : {pochoir.largeur:.6f} mm"
)

print(
    f"Hauteur : {pochoir.hauteur:.6f} mm"
)

print(
    f"Épaisseur : {pochoir.epaisseur:.6f} mm"
)

print(
    f"Volume : {pochoir.volume:.6f} mm³"
)

print(
    f"Centre : {pochoir.centre}"
)

boite = pochoir.boite_englobante

print(
    f"X : {boite.xmin} → {boite.xmax}"
)

print(
    f"Y : {boite.ymin} → {boite.ymax}"
)


# ==========================================================
# VALIDATIONS
# ==========================================================

assert pochoir.largeur == 70
assert pochoir.hauteur == 70
assert pochoir.epaisseur == 2

assert pochoir.volume == 9800

assert pochoir.centre == (0.0, 0.0)

assert boite.largeur == 70
assert boite.hauteur == 70

assert boite.xmin == -35
assert boite.xmax == 35

assert boite.ymin == -35
assert boite.ymax == 35


print()
print("=" * 60)
print("TEST POCHOIR : OK")
print("=" * 60)