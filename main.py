import os
from canvas import Canvas, canvas_to_viewport
from utils import dot, normalize, longueur
from raytracer import trace_ray
from scene import Scene
from object import Sphere
from lights import AmbientLight, PointLight, DirectionalLight
from PIL import Image # Pour la création du GIF
import math
import numpy as np

Cw = 800 
Ch = 600 
Vw = 1.0
Vh = 0.75
d = 1     # Distance entre la caméra et le viewport

# Params pour les animations de lumière
num_frames = 5
radius_light = 3
height_light = 1

O = (0, 0, 0)

os.makedirs("output", exist_ok=True)

for frame in range(num_frames):
    print(f"Rendu en cours {frame + 1}/{num_frames}...")
    
    canvas = Canvas(Cw, Ch)
    
    scene = Scene()
    
    # SCÈNE PAR DÉFAUT : Drapeau français

    scene.add_object(Sphere((-2, 0, 5), 1, (0, 85, 164), 100, 0.3))             # Sphère bleue
    scene.add_object(Sphere((0, 0, 5), 1, (255, 255, 255), 100, 0.3))           # Sphère blanche
    scene.add_object(Sphere((2, 0, 5), 1, (239, 65, 53), 100, 0.3))             # Sphère rouge
    scene.add_object(Sphere((0, -5001, 0), 5000, (200, 200, 200), 1000, 0.5))   # Sol gris

    # SCÈNE ALTERNATIVE
    """
    scene.add_object(Sphere((0, 1, 5), 1, (255, 255, 0), 100, 0.2))             # Sphère jaune
    scene.add_object(Sphere((0, -0.5, 4), 0.5, (0, 150, 255), 100, 0.2))        # Sphère bleue
    scene.add_object(Sphere((0, -5001, 0), 5000, (200, 200, 200), 1000, 0.5))   # Sol gris
    """

    # Position de la lumière point sur un cercle
    angle = (frame / num_frames) * 2 * math.pi  # Angle de 0 à 2π
    light_x = radius_light * math.cos(angle)
    light_z = radius_light * math.sin(angle)
    
    scene.add_light(AmbientLight(0.2))           
    scene.add_light(PointLight(1.0, (light_x, height_light, light_z)))   # Lumière qui tourne
    scene.add_light(DirectionalLight(0.2, (1, 4, 4)))
    
    # Rendu avec la scène
    for x in range(-Cw // 2, Cw // 2):
        for y in range(-Ch // 2, Ch // 2):
            D = canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d)
            D = normalize(D)
            couleur = trace_ray(scene, O, D, 1, float('inf'), 3)
            canvas_x = x + Cw // 2
            canvas_y = (Ch // 2 - y)
            canvas.put_pixel(canvas_x, canvas_y, couleur)
    
    filename = f'raytracer_{frame:02d}.ppm'
    canvas.save(filename)

# Génération du GIF
frames = []
for i in range(num_frames):
    filename = os.path.join("output", f'raytracer_{i:02d}.ppm')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier attendu est absent : {filename}")
    img = Image.open(filename)
    frames.append(img)

if frames:
    gif_path = os.path.join("output", 'raytracer_animation.gif')
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=500,
        loop=0
    )
    print(f"GIF créé : {gif_path}")
else:
    print("Aucun frame trouvé pour créer le GIF.")