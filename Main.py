import numpy as np
import tkinter as tk
import interface_graphique as ig
import listeChainée
from listeChainée import ListeChainee


dt = 0.001
r = 15
cofrot = 0.001
L = 1000
H = 500
epsilon = 0.5

p_min = np.array([r, r])
p_max = np.array([1000 - r, 500 - r])
simulation = False

liste = ListeChainee()
pasActuel = None


def detecter_et_rebondir(p, v):
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


def calculer_position(p, v, mu=None):
    if mu is None:
        mu = cofrot
    v = v * (1 - mu * dt)
    p, v = detecter_et_rebondir(p, v)
    p = p + (v * dt)
    return p, v


def lancer(angle, vitesse, mu=None):
    global simulation, pasActuel, liste
    if mu is None:
        mu = cofrot
    collision = False
    pasActuel = None
    liste.__init__()

    p = np.array([225, 225])
    v = np.array([0, 0])
    v[0] = vitesse * np.cos(angle)
    v[1] = vitesse * np.sin(angle)

    while collision == False:
        simulation = True
        p, v = calculer_position(p, v, mu)

        liste.append(p.copy())
        ig.dessiner_balle(p[0], p[1], r)

        vitesse_norm = np.linalg.norm(v)
        if vitesse_norm <= epsilon:
            collision = True
            print(f"Balle immobile! Position finale: ({p[0]:.1f}, {p[1]:.1f})")
            simulation = False
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
        # Parcourir la liste pour trouver le noeud précédent
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
    ig.dessiner_balle(225, 225, r)
    ig.pool.mainloop()
