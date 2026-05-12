import tkinter as tk
import numpy as np
import Main

pool = tk.Tk()
pool.title("Jeu de billard")

conteneur = tk.Frame(pool)
conteneur.pack(fill="both", expand=True)

cadre_textes = tk.Frame(conteneur)
cadre_textes.pack(side="left", fill="y", padx=10, pady=10)

cadre_terrain = tk.Frame(conteneur)
cadre_terrain.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(cadre_textes, text="entrez un angle de lancement").pack(anchor="w")

champ_angle = tk.Entry(cadre_textes, width=40)
champ_angle.pack(anchor="w")

tk.Label(cadre_textes, text="entrez une vitesse de lancement").pack(anchor="w")

champ_vitesse = tk.Entry(cadre_textes, width=40)
champ_vitesse.pack(anchor="w")

tk.Label(cadre_textes, text="Coefficient de friction (μ)").pack(anchor="w", pady=(10, 0))
champ_friction = tk.Entry(cadre_textes, width=40)
champ_friction.insert(0, "1.0")
champ_friction.pack(anchor="w")


    
def lancement():
    angle = champ_angle.get()
    vitesse = champ_vitesse.get()
    friction = champ_friction.get()
    try:
        angle = float(angle)
        vitesse = float(vitesse)
        friction = float(friction)
        label_resultat_angle.config(text="Simulation en cours...")
        Main.lancer(np.radians(angle), vitesse, friction)
    except ValueError as e:
        label_resultat_angle.config(text=f"Erreur : {e}")

bouton_lancer = tk.Button(pool, text="Lancer", command=lancement)
bouton_lancer.pack(in_=cadre_textes, anchor="w", pady=(10, 0))
label_resultat_angle = tk.Label(pool, text="Résultat : ")
label_resultat_angle.pack(in_=cadre_textes, anchor="w")
label_resultat_vitesse = tk.Label(pool, text="Résultat : ")
label_resultat_vitesse.pack(in_=cadre_textes, anchor="w")

canvas = tk.Canvas(cadre_terrain, width=1000, height=500, bg="green")
canvas.pack(fill="both", expand=True)

def dessiner_balle(x1,y1,r):
    canvas.delete("all")
    # Dessiner les bandes sur les 4 bords
    canvas.create_rectangle(0, 0, 10, 500, fill="brown", outline="black")  # gauche
    canvas.create_rectangle(990, 0, 1000, 500, fill="brown", outline="black")  # droit
    canvas.create_rectangle(0, 0, 1000, 10, fill="brown", outline="black")  # haut
    canvas.create_rectangle(0, 490, 1000, 500, fill="brown", outline="black")  # bas
    # Dessiner la balle
    balle = canvas.create_oval(x1-(r/2), y1-(r/2), x1+r, y1+r, fill="white", outline="black", width=2)
    pool.update()

def afficher_position_finale(x, y):
    """Afficher la position où la balle s'est arrêtée"""
    label_resultat_vitesse.config(text=f"Position finale: ({x:.1f}, {y:.1f})")

if __name__ == "__main__":
    pool.mainloop()