import os
import numpy as np

# Mise en place de le Toile ( Canvas ) = image finale que l'on remplit pixel par pixel.
class Canvas:
    def __init__(self, width, height):
        self.width = width    # Cw => largeur
        self.height = height  # Ch => hauteur
        self.pixels = [[(0.0, 0.0, 0.0) for _ in range(width)] for _ in range(height)]

    # Mise en place de la coloration des pixels => RGB
    def put_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    # Sauvegarde du résultat en PPM dans le dossier ./output/
    def save(self, filename):
        dirpath = os.path.dirname(filename)
        if not os.path.isabs(filename) and dirpath == "":
            dirpath = "output"
            filename = os.path.join(dirpath, filename)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

        with open(filename, 'w') as f:
            f.write(f"P3\n{self.width} {self.height}\n255\n")
            for y in range(self.height):
                for x in range(self.width):
                    r, g, b = self.pixels[y][x]
                    r = int(min(max(r, 0), 255))
                    g = int(min(max(g, 0), 255))
                    b = int(min(max(b, 0), 255))
                    f.write(f"{r} {g} {b} ")
                f.write("\n")
        print(f"Raytracer Sauvegardé : {filename}")

# Fonction qui convertie les coordonnées 2D en pixel vers la 3D du viewport
def canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d): # Cw, Ch => Canvas width, height / Vw, Vh => Viewport width, height
    return (x * Vw / Cw, y * Vh / Ch, d)
