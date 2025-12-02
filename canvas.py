# canvas.py

class Canvas:
    def __init__(self, width, height):
        self.width = width    # Cw
        self.height = height  # Ch
        self.pixels = [[(0.0, 0.0, 0.0) for _ in range(width)] for _ in range(height)]

    def put_pixel(self, x, y, color):
        # Base du projet = La toile blanche sur laquelle on dessine.
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def save(self, filename):
        """✅ AJOUTÉ : Sauvegarde l'image en PPM"""
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
        print(f"✅ Image sauvée : {filename}")

def canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d):
    # Conversion de 2D vers 3D
    return (x * Vw / Cw, y * Vh / Ch, d)
