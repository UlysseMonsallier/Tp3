import tkinter as tk

pool = tk.Tk()
pool.title("Jeu de billard")

tk.Label(pool, text="entrez un angle de lancement" ).pack()

champ_angle = tk.Entry(pool, width=40)
champ_angle.pack()

tk.Label(pool, text="entrez une vitesse de lancement" ).pack()

champ_vitesse = tk.Entry(pool, width=40)
champ_vitesse.pack()

def lancement():
    angle = champ_angle.get()
    vitesse = champ_vitesse.get()
    try:
        angle = float(angle)
        vitesse = float(vitesse)
        label_resultat_angle.config(text=f"Angle de lancement : {angle} degrés,")
        label_resultat_vitesse.config(text=f"Vitesse de lancement : {vitesse} m/s")
    except ValueError as e:
        label_resultat_angle.config(text=f"Erreur : {e}")

bouton_lancer = tk.Button(pool, text="Lancer", command=lancement)
bouton_lancer.pack()
label_resultat_angle = tk.Label(pool, text="Résultat : ")
label_resultat_angle.pack()
label_resultat_vitesse = tk.Label(pool, text="Résultat : ")
label_resultat_vitesse.pack()

tk.canvas = tk.Canvas(pool, width=1000, height=500, bg="green")
tk.canvas.pack()

def dessiner_balle(x1,y1,r):
    tk.canvas.create_oval(x1-(r/2), y1-(r/2), x1+r, y1+r, fill="white", outline="black", width=2)
    pool.mainloop()

pool.mainloop()