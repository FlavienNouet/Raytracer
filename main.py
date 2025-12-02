from canvas import Canvas, canvas_to_viewport
from utils import dot, normalize, longueur
from raytracer import trace_ray
from scene import Scene
from object import Sphere  
from lights import AmbientLight, PointLight

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
scene.add_object(Sphere((0,-1,3), 1, (255,0,0), 10, 0.2))   # Sphère Rouge
scene.add_object(Sphere((2,0,4), 1, (0,255,0), 10, 0.1))   # Sphère Vert  
scene.add_object(Sphere((-2,0,4), 1, (0,0,255), 10, 0.4))  # Shère Bleu

# Ajouter des lumières
scene.add_light(AmbientLight(0.2))           
scene.add_light(PointLight(1.0, (2,1,0)))   

# Caméra à l'origine
O = (0, 0, 0)

# Rendu avec la scène
for x in range(-Cw // 2, Cw // 2):
    for y in range(-Ch // 2, Ch // 2):
        D = canvas_to_viewport(x, y, Vw, Vh, Cw, Ch, d)
        D = normalize(D)
        couleur = trace_ray(scene, O, D, 1, float('inf'), 3)
        canvas.put_pixel(x + Cw//2, y + Ch//2, couleur)

canvas.save('raytracer.ppm') #Enristrement de l'image finale

