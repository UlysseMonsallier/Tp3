from logging import config

import numpy as np
import tkinter as tk
import interface_graphique as ig
import listeChainée
from listeChainée import ListeChainee
import json
dt = 0.001
r = 15
cofrot = 1.0
L = 1000
H = 500
vitesseMin = 0.5
with open("FichierConfiguration.json", "r") as f:
    configfile = json.load(f)

def OpenConfig(file):
    with open(file, "r") as f:
        
        configfile = json.load(f)
    try:
        configfile["dimensions de la surface de jeu"]
        configfile["rayon des balles"]
        configfile["coefficient de frottement"]
        configfile["position initiale des balles"]
        configfile["vitesse minimum des balles"]
        configfile["variation de temps"]
        
    except KeyError as e:
        print(f"Error: Missing configuration key - {e}")
        exit(1)
    try:
        global dt, r, cofrot, L, H, vitesseMin
        dt = float(configfile["variation de temps"])
        r = int(configfile["rayon des balles"])
        cofrot = float(configfile["coefficient de frottement"])
        L = int(configfile["dimensions de la surface de jeu"][0])
        H = int(configfile["dimensions de la surface de jeu"][1])
        vitesseMin = float(configfile["vitesse minimum des balles"])
        
    except ValueError as e:
        print(f"Error: Invalid configuration value - {e}")
        exit(1)
    finally:
        ig.draw_canva(L,H)
        ig.dessiner_balle(configfile["position initiale des balles"][0][0], configfile["position initiale des balles"][0][1], r)
        ig.pool.mainloop()
        print("Configuration loaded successfully.")

p_min = np.array([r, r])
p_max = np.array([L - r, H - r])

liste = ListeChainee()
pasActuel = None


def detecter_et_rebondir(p, v):
    global r, L, H
    if p[0] <= r:
        p[0] = r
        n = np.array([1.0, 0.0])
        v = v - 2 * np.dot(v, n) * n

    if p[0] >= L - r:
        p[0] = L - r
        n = np.array([-1.0, 0.0])
        v = v - 2 * np.dot(v, n) * n

    if p[1] <= r:
        p[1] = r
        n = np.array([0.0, 1.0])
        v = v - 2 * np.dot(v, n) * n

    if p[1] >= H - r:
        p[1] = H - r
        n = np.array([0.0, -1.0])
        v = v - 2 * np.dot(v, n) * n

    return p, v


def calculer_position(p, v, frottement=None):
    if frottement is None:
        frottement = cofrot
    v = v * (1 - frottement * dt)
    p, v = detecter_et_rebondir(p, v)
    p = p + (v * dt)
    return p, v


def lancer(angle, vitesse):
    global pasActuel, liste
    frottement = cofrot
    stop = False
    pasActuel = None
    liste.__init__()

    p = np.array(configfile["position initiale des balles"][0])
    v = np.array([0, 0])
    v[0] = vitesse * np.cos(angle)
    v[1] = vitesse * np.sin(angle)

    while stop == False:
        p, v = calculer_position(p, v, frottement)

        liste.append(p.copy())
        ig.dessiner_balle(p[0], p[1], r)

        vitesse_norm = np.linalg.norm(v)
        if vitesse_norm <= vitesseMin:
            stop = True
            ig.afficher_position_finale(p[0], p[1])
            ig.reset_buttons()

        ig.pool.update()


def pas_suivant():
    global pasActuel
    if pasActuel is None:
        pasActuel = liste.tete
    elif pasActuel.suivant is not None:
        pasActuel = pasActuel.suivant
    if pasActuel is not None:
        p = pasActuel.valeur
        ig.dessiner_balle(p[0], p[1], r)


def pas_precedent():
    global pasActuel
    if pasActuel is None:
        pasActuel = liste.queue
    else:
        courant = liste.tete
        while courant and courant.suivant != pasActuel:
            courant = courant.suivant
        if courant:
            pasActuel = courant
    if pasActuel is not None:
        p = pasActuel.valeur
        ig.dessiner_balle(p[0], p[1], r)


def position_finale():
    global pasActuel
    pasActuel = liste.queue
    if pasActuel is not None:
        p = pasActuel.valeur
        ig.dessiner_balle(p[0], p[1], r)


def reinitialiser():
    global pasActuel
    pasActuel = liste.tete
    if pasActuel is not None:
        p = pasActuel.valeur
        ig.dessiner_balle(p[0], p[1], r)


if __name__ == "__main__":
    ig.pool.mainloop()
