import numpy as np
import tkinter as tk
from tkinter import ttk
import math

class BalleState:
    def __init__(self, postion, temps, velocite):
        self.postion = postion.copy()
        self.temps = temps
        self.velocite = velocite.copy()

class SimulateurPool:
    def __init__(self, width=800, height=400, ball_radius=10, dt=0.01):
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.dt = dt

        self.balls = []
        self.root = tk.Tk()
        self.root.title("Simulateur de Billard")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="green")
        self.canvas.pack()

    def trajectoire(self, position, angle_degres, vitesse):
        p = position.copy()
        angle_rad = math.radians(angle_degres)
        p[0] += vitesse * math.cos(angle_rad) * self.dt
        p[1] += vitesse * math.sin(angle_rad) * self.dt
        return p

        