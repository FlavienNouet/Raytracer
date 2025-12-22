from canvas import Canvas, canvas_to_viewport
from utils import dot, normalize, longueur
from raytracer import trace_ray
from scene import Scene
from object import Sphere  
from lights import AmbientLight, PointLight, DirectionalLight

# Miee en lace de la boucle principale de notre projet => rendu d'une scène simple

#Paramètre de notre scène
Cw = 800  
Ch = 600  
Vw = 1.0  
Vh = 0.75 
d = 1     

canvas = Canvas(Cw, Ch)

# Création de la scène = objets + lumières
scene = Scene()

# Ajout des objets
scene.add_object(Sphere((-2,0,5), 1, (0,85,164), 100, 0.3))   # Sphère Bleue
scene.add_object(Sphere((0,0,5), 1, (255,255,255), 100, 0.3))   # Sphère Blanche
scene.add_object(Sphere((2,0,5), 1, (239,65,53), 100, 0.3))   # Sphère Rouge
scene.add_object(Sphere((0,-5001,0), 5000, (200,200,200), 1000, 0.5))  # Sol gris

# Ajouter des lumières
scene.add_light(AmbientLight(0.2))           
scene.add_light(PointLight(1.0, (2,1,0)))   
scene.add_light(DirectionalLight(0.2, (1,4,4)))

# Caméra à l'origine
O = (0, 0, 0)

# Rendu avec la scène
for x in range(-Cw // 2, Cw // 2):
    for y in range(-Ch // 2, Ch // 2):
        D = canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d)
        D = normalize(D)
        couleur = trace_ray(scene, O, D, 1, float('inf'), 3)
        canvas_x = x + Cw // 2
        canvas_y = (Ch // 2 - y)  # inverse l'axe Y pour afficher à l'endroit
        canvas.put_pixel(canvas_x, canvas_y, couleur)

canvas.save('raytracer.ppm') #Enristrement de l'image finale

