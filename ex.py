import tkinter as tk
#Canevas pour dessiner la trajectoire
class TrajectoireCanvas(tk.Canvas):
    def __init__(self, master=None, width=800, height=400, bg="white"):
        super().__init__(master, width=width, height=height, bg=bg)
        self.pack()

    def dessiner_trajectoire(self, points):
        for i in range(len(points) - 1):
            self.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], fill="blue", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trajectoire de la Balle")
    canvas = TrajectoireCanvas(root)

    # Exemple de points pour la trajectoire
    points = [(50, 350), (150, 300), (250, 250), (350, 200), (450, 150)]
    canvas.dessiner_trajectoire(points)

    root.mainloop() 

            