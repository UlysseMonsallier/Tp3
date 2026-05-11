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

current_pas = 0
def calculer_position(p, v):
    v[0] = v[0] * (1 - (cofrot * dt))
    v[1] = v[1] * (1 - (cofrot * dt))
    p = p + (v * dt )
    return p, v

liste = ListeChainee()
def lancer(angle, vitesse):
    collision = False
    global pasActuel
    pasActuel = None 
    liste.__init__()  
    p = np.array([225, 225])
    v = np.array([0, 0])
    v[0] = vitesse * np.cos(angle)
    v[1] = vitesse * np.sin(angle)
    while collision == False:
        
        p, v = calculer_position(p, v)
        liste.append(p.copy())
        ig.dessiner_balle(p[0], p[1], r)
        if np.any(p <= p_min) or np.any(p >= p_max) or np.all(v == 0):
            collision = True
            print("Collision détectée !")
            
            ig.reset_buttons()
            

pasActuel = None
def pas_suivant():
    global pasActuel
    if pasActuel is None:
        pasActuel = liste.tete
    p = pasActuel.valeur
    pasActuel = pasActuel.suivant
    ig.dessiner_balle(p[0], p[1], r)
def pas_precedent():
    global pasActuel
    if pasActuel is None:
        pasActuel = liste.tete
    
    p = pasActuel.valeur
    pasActuel = pasActuel.precedent
    ig.dessiner_balle(p[0], p[1], r)
def position_finale():
    global pasActuel
    pasActuel = liste.queue
    p = pasActuel.valeur
    ig.dessiner_balle(p[0], p[1], r)

def reinitialiser():
    global pasActuel
    pasActuel = liste.tete
    p = pasActuel.valeur
    ig.dessiner_balle(p[0], p[1], r)
    
    

if __name__ == "__main__":
    ig.dessiner_balle(225, 225, r)
    ig.pool.mainloop()
