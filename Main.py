import numpy as np
import tkinter as tk
import interface_graphique as ig


# variables mouvement de la balle

dt = 0.001
r = 30

p_min = np.array([r, r])
p_max = np.array([1000 - r, 500 - r])
simulation = False
def lancer(angle, vitesse):
    global simulation
    if simulation == False:
        collision = False
    p = np.array([225, 225])
    v = np.array([0, 0])
    
    while collision == False:
        simulation = True
        v[0] = vitesse * np.cos(angle)
        v[1] = vitesse * np.sin(angle)
        p = p + v * dt
        print(p)
        ig.dessiner_balle(p[0], p[1], r)
        if np.any(p <= p_min) or np.any(p >= p_max):
            collision = True
            print("Collision détectée !")
            simulation = False
        
    

if __name__ == "__main__":
    ig.dessiner_balle(225, 225, r)
    ig.pool.mainloop()
