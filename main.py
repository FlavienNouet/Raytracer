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

# Paramètre de notre scène = Configuration du Canvas et du Viewport
Cw = 800  # Largeur du canvas
Ch = 600  # Hauteur du canvas
Vw = 1.0  # Largeur du viewport
Vh = 0.75 # Hauteur du viewport
d = 1     # Distance entre la caméra et le viewport

# Paramètres pour les animations de lumière
num_frames = 5  # Nombre d'images à générer
radius_light = 3
height_light = 1  # Hauteur de la lumière

# Caméra à l'origine
O = (0, 0, 0)

# Mise en place du dossier output pour y mettre les résultats
os.makedirs("output", exist_ok=True)

# Boucle de génération d'images
for frame in range(num_frames):
    print(f"Rendu en cours {frame + 1}/{num_frames}...")
    
    canvas = Canvas(Cw, Ch)
    
    # Création de la scène = objets + lumières
    scene = Scene()
    
    # Ajout des objets (les mêmes pour chaque frame)
    scene.add_object(Sphere((-2, 0, 5), 1, (0, 85, 164), 100, 0.3))             # Sphère Bleue
    scene.add_object(Sphere((0, 0, 5), 1, (255, 255, 255), 100, 0.3))           # Sphère Blanche
    scene.add_object(Sphere((2, 0, 5), 1, (239, 65, 53), 100, 0.3))             # Sphère Rouge
    scene.add_object(Sphere((0, -5001, 0), 5000, (200, 200, 200), 1000, 0.5))   # Sol gris
    
    # Position de la lumière point sur un cercle
    angle = (frame / num_frames) * 2 * math.pi  # Angle de 0 à 2π
    light_x = radius_light * math.cos(angle)
    light_z = radius_light * math.sin(angle)
    
    # Ajout des lumières avec position changeante
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
            canvas_y = (Ch // 2 - y)  # inverse l'axe Y pour afficher à l'endroit
            canvas.put_pixel(canvas_x, canvas_y, couleur)
    
    # Sauvegarde de l'image PPM
    filename = f'raytracer_{frame:02d}.ppm'
    canvas.save(filename)

# Après avoir rendu toutes les images, créer un GIF à partir des images PPM dans `output/`
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
    print("⚠️ Aucun frame trouvé pour créer le GIF.")