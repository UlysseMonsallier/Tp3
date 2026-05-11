import numpy as np
import tkinter as tk
import interface_graphique as ig
import listeChainée
from listeChainée import ListeChainee


dt = 0.001
r = 15
cofrot = 0.001

p_min = np.array([r, r])
p_max = np.array([1000 - r, 500 - r])
simulation = False
current_pas = 0
def calculer_position(p, v):
    v[0] = v[0] * (1 - (cofrot * dt))
    v[1] = v[1] * (1 - (cofrot * dt))
    p = p + (v * dt )
    return p, v

liste = ListeChainee()
def lancer(angle, vitesse):
    global simulation
    if simulation == False:
        collision = False
    p = np.array([225, 225])
    v = np.array([0, 0])
    liste = listeChainée.ListeChainee()
    v[0] = vitesse * np.cos(angle)
    v[1] = vitesse * np.sin(angle)
    while collision == False:
        simulation = True
        p, v = calculer_position(p, v)
        current_pas += 1
        liste.append(p.copy())
        ig.dessiner_balle(p[0], p[1], r)
        if np.any(p <= p_min) or np.any(p >= p_max) or np.all(v == 0):
            collision = True
            print("Collision détectée !")
            simulation = False

def pas_suivant():
    global current_pas
    if current_pas >= 0 and current_pas < len(liste) - 1:
        current_pas += 1
    p, v = liste[current_pas]
    ig.dessiner_balle(p[0], p[1], r)
def pas_precedent():
    global current_pas
    if current_pas > 0:
        current_pas -= 1
    p, v = liste[current_pas]
    ig.dessiner_balle(p[0], p[1], r)
    
    
    

if __name__ == "__main__":
    ig.dessiner_balle(225, 225, r)
    ig.pool.mainloop()
