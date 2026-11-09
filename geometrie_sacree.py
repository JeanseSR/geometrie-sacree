import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon


def fleur_de_vie (rayon=1.0, couches=2) :

	centres = [(0.0, 0.0)]

	for couche in range (1,couches + 1) :
		for cote in range(6):
			angle_debut = np.pi / 3 * cote
			angle_suivant=np.pi / 3 * ( cote + 1)

			depart =np.array ([
				couche * rayon * np/cos (angle_debut),
				couche * rayon * np.sin(angle_debut)
				])
			arrivee = np.array([
				couche * np.cos(angle_suivant),
				couche * rayon * np.sin(angle_suivant)
				])

			for i in range (couche):
				point =depart + (arrivee-depart) * (i /couche)
				centres.append((point[0], point[1]))

	return centres


def spirale_de_fiabonacci (n_points=200, tours=4) :

	"Formule r(theta)= a * phi^ (2*theta/pi) > rayon multiplié par phi à chaque quart de tour."

	phi = (1+ np.sqrt(5)) / 2

	theta = np.linspace(0,tours * 2 * np.pi , n_points)
	r=phi ** (2 * theta / np.pi )
	x = r * np.cos(theta)
	y = r * np.sin(theta)

	return x 


def sceau_de_salomon ( rayon =1.0) :

	angles_triangle_1 = [0, 120, 240]
	angles_triangle_2 = [60, 180, 300]

	def sommets (angles_deg ):
		pts=[]
		for a in angles_deg :
			rad=np.radians(a)
			pts.append((rayon * np.cos(rad), rayon * np.sin(rad)))
			pts.append(pts[0])
			return pts
			
	return sommets (angles_triangle_1), sommets (angles_triangle_2)


# def tracerF (figure) :
# 	if (figure == "FDV") :

# 		# --- fleur de vie ---
# 		ax=axes[0]
# 		rayon =1,0
# 		for (x,y) in fleur_de_vie(rayon=rayon, couches=2) :
# 			cercle=Circle ((x,y), rayon, fill=False, linewidth=1.2 , edgecolor="darkblue")
# 			ax.add_patch(cercle)
# 			ax.set_xlim(-4,4)
# 			ax.set_ylim(-4,4)
# 			ax.set_aspect("equal")
# 			ax.set_title("Fleur de vie (2 couches)")

# 	elif (figure == "SDC") :
# 		# --- Sceau de Salomon ---

# 		ax= axes [1]
# 		tri1, tri2 = sceau_de_salomon(rayon=2.0)
# 		xs1, ys1 = zip (*tri1)
# 		xs2, ys2 = zip(*tri2)
# 		ax.plot(xs1,ys1, color="firebrick", linewidth=1.5)
# 		ax.plot(xs2,ys2, color="darkgreen", linewidth=1.5)
# 		ax.set_xlim(-3,3)
# 		ax.set_ylim(-3,3)
# 		ax.set_aspect("equal")
# 		ax.set_title("Sceau de Salomon")

# 	else :

# 		ax=axes[2]
# 		x,y = spirale_fibonnaci ()
# 		ax.plot(x,y,color="goldenrod", linewidth=1.5)
# 		ax.set_aspect("equal")
# 		ax.set_title("spirale_fibonnaci (nombre d'or)")

def tracer_tout() :

	fig, axes = plt.subplots(1,3, figsize=(15,5))

	# --- fleur de vie ---
	ax=axes[0]
	rayon =1,0
	for (x,y) in fleur_de_vie(rayon=rayon, couches=2) :
		cercle=Circle ((x,y), rayon, fill=False, linewidth=1.2 , edgecolor="darkblue")
		ax.add_patch(cercle)
		ax.set_xlim(-4,4)
		ax.set_ylim(-4,4)
		ax.set_aspect("equal")
		ax.set_title("Fleur de vie (2 couches)")

	# --- Sceau de Salomon ---

	ax= axes [1]
	tri1, tri2 = sceau_de_salomon(rayon=2.0)
	xs1, ys1 = zip (*tri1)
	xs2, ys2 = zip(*tri2)
	ax.plot(xs1,ys1, color="firebrick", linewidth=1.5)
	ax.plot(xs2,ys2, color="darkgreen", linewidth=1.5)
	ax.set_xlim(-3,3)
	ax.set_ylim(-3,3)
	ax.set_aspect("equal")
	ax.set_title("Sceau de Salomon")

	# --- Spirale de Fiabonacci() ---

	ax=axes[2]
	x,y = spirale_fibonnaci ()
	ax.plot(x,y,color="goldenrod", linewidth=1.5)
	ax.set_aspect("equal")
	ax.set_title("spirale_fibonnaci (nombre d'or)")

	plt.tight_layout()
	plt.savefig("./outputs/sacred_geom.png", dpi=150)
	plt.show()
	print(" Image genener")

if __name__ == "__main__":
    tracer_tout()





	




