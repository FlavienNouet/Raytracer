import os
import numpy as np

# Grille de pixels
class Canvas:
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
        self.pixels = [[(0.0, 0.0, 0.0) for _ in range(width)] for _ in range(height)]

    # Coloration des pixels
    def put_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    # Rendus PPM
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

def canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d):
    return (x * Vw / Cw, y * Vh / Ch, d)
