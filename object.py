# Création de nos sphères dans la scène

class Sphere:
    def __init__(self, center, radius, color, specular, reflective):
        self.center = center     
        self.radius = radius     
        self.color = color       
        self.specular = specular  
        self.reflective = reflective  

    # Méthode pour savoir si le rayon tape dans la sphère
    def intersect(self, O, D):
        OC = (O[0] - self.center[0], O[1] - self.center[1], O[2] - self.center[2]) # Distance entre le centre de la sphère et l'origine du rayon
        a = D[0]*D[0] + D[1]*D[1] + D[2]*D[2]
        b = 2 * (OC[0]*D[0] + OC[1]*D[1] + OC[2]*D[2])
        c = (OC[0]*OC[0] + OC[1]*OC[1] + OC[2]*OC[2]) - self.radius*self.radius

        delta = b*b - 4*a*c # Permet de savoir si le rayon touche la sphère
        if delta < 0: # Pas touché 
            return None, None

        sqrt_delta = delta ** 0.5 # Touché 
        t1 = (-b - sqrt_delta) / (2*a)
        t2 = (-b + sqrt_delta) / (2*a)
        return t1, t2
