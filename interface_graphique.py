import tkinter as tk
import numpy as np
import Main

pool = tk.Tk()
pool.title("Jeu de billard")

conteneur = tk.Frame(pool)
conteneur.pack(fill="both", expand=True)

# Mise en page avec grid
cadre_textes = tk.Frame(conteneur, width=300)
cadre_textes.pack(side="left", fill="y", padx=10, pady=10)
cadre_textes.grid_propagate(False)
cadre_textes.columnconfigure(0, weight=1)

cadre_terrain = tk.Frame(conteneur)
cadre_terrain.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Champs angle et vitesse
tk.Label(cadre_textes, text="Entrez un angle de lancement").grid(row=0, column=0, sticky="w", padx=5, pady=(6,2))
champ_angle = tk.Entry(cadre_textes, width=30)
champ_angle.grid(row=1, column=0, sticky="we", padx=5, pady=(0,8))

tk.Label(cadre_textes, text="Entrez une vitesse de lancement").grid(row=2, column=0, sticky="w", padx=5, pady=(2,2))
champ_vitesse = tk.Entry(cadre_textes, width=30)
champ_vitesse.grid(row=3, column=0, sticky="we", padx=5, pady=(0,8))

# Champ friction
tk.Label(cadre_textes, text="Coefficient de friction").grid(row=4, column=0, sticky="w", padx=5, pady=(2,2))
champ_friction = tk.Entry(cadre_textes, width=30)
champ_friction.insert(0, "1.0")
champ_friction.grid(row=5, column=0, sticky="we", padx=5, pady=(0,8))

# Labels de résultat
result_frame = tk.Frame(cadre_textes)
result_frame.grid(row=6, column=0, sticky="we", padx=5, pady=(0,8))
result_frame.columnconfigure(0, weight=1)
label_resultat_angle = tk.Label(result_frame, text="Résultat : ")
label_resultat_angle.pack(anchor="w")
label_resultat_vitesse = tk.Label(result_frame, text="Résultat : ")
label_resultat_vitesse.pack(anchor="w")


def lancement():
    angle = champ_angle.get()
    vitesse = champ_vitesse.get()
    friction = champ_friction.get()
    bouton_lancer.config(state="disabled")
    bouton_pas_prec.config(state="disabled")
    bouton_pas_suiv.config(state="disabled")
    bouton_pos_finale.config(state="disabled")
    bouton_renitialiser.config(state="disabled")
    try:
        angle = float(angle)
        vitesse = float(vitesse)
        friction = float(friction)
        label_resultat_angle.config(text="Simulation en cours...")
        Main.lancer(np.radians(angle), vitesse, friction)
    except ValueError as e:
        label_resultat_angle.config(text=f"Erreur : {e}")


def reset_buttons():
    bouton_lancer.config(state="normal")
    bouton_pas_prec.config(state="normal")
    bouton_pas_suiv.config(state="normal")
    bouton_pos_finale.config(state="normal")
    bouton_renitialiser.config(state="normal")


def pas_precedent():
    for i in range(int(champ_multi.get()) if champ_multi.get().isdigit() else 1):
        Main.pas_precedent()


def pas_suivant():
    for i in range(int(champ_multi.get()) if champ_multi.get().isdigit() else 1):
        Main.pas_suivant()


# Boutons regroupés
btn_frame = tk.Frame(cadre_textes)
btn_frame.grid(row=7, column=0, sticky="we", padx=5, pady=(0,8))
btn_frame.columnconfigure(0, weight=1)

bouton_lancer = tk.Button(btn_frame, text="Lancer", command=lancement)
bouton_lancer.grid(row=0, column=0, sticky="we", pady=2)

bouton_pas_prec = tk.Button(btn_frame, text="Pas précédent", command=pas_precedent)
bouton_pas_prec.grid(row=1, column=0, sticky="we", pady=2)

bouton_pas_suiv = tk.Button(btn_frame, text="Pas suivant", command=pas_suivant)
bouton_pas_suiv.grid(row=2, column=0, sticky="we", pady=2)

bouton_pos_finale = tk.Button(btn_frame, text="Position finale", command=Main.position_finale)
bouton_pos_finale.grid(row=3, column=0, sticky="we", pady=2)

bouton_renitialiser = tk.Button(btn_frame, text="Réinitialiser", command=Main.reinitialiser)
bouton_renitialiser.grid(row=4, column=0, sticky="we", pady=2)

# Champ multiplicateur d'étapes
tk.Label(cadre_textes, text="Multiplicateur d'étapes").grid(row=8, column=0, sticky="w", padx=5, pady=(2,2))
champ_multi = tk.Entry(cadre_textes, width=30)
champ_multi.insert(0, "1")
champ_multi.grid(row=9, column=0, sticky="we", padx=5, pady=(0,8))

# Canvas
canvas = tk.Canvas(cadre_terrain, width=1000, height=500, bg="green")
canvas.pack(fill="both", expand=True)


def dessiner_balle(x1, y1, r):
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 10, 500, fill="brown", outline="black")  # gauche
    canvas.create_rectangle(990, 0, 1000, 500, fill="brown", outline="black")  # droit
    canvas.create_rectangle(0, 0, 1000, 10, fill="brown", outline="black")  # haut
    canvas.create_rectangle(0, 490, 1000, 500, fill="brown", outline="black")  # bas
    balle = canvas.create_oval(x1 - r/2, y1 - r/2, x1 + r/2, y1 + r/2, fill="white", outline="black", width=2)
    pool.update()


def afficher_position_finale(x, y):
    """Afficher la position où la balle s'est arrêtée"""
    label_resultat_vitesse.config(text=f"Position finale: ({x:.1f}, {y:.1f})")


if __name__ == "__main__":
    pool.mainloop()
