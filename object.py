# Création de nos sphères dans la scène

class Sphere:
    def __init__(self, center, radius, color, specular, reflective):
        self.center = center     
        self.radius = radius     
        self.color = color       
        self.specular = specular  
        self.reflective = reflective  

    def intersect(self, O, D):
        """
        Intersection rayon-sphère :
        P = O + tD
        ||P - C||^2 = r^2
        Retourne les deux solutions (t1, t2), ou (None, None) si pas d'intersection.
        """
        OC = (O[0] - self.center[0], O[1] - self.center[1], O[2] - self.center[2])
        a = D[0]*D[0] + D[1]*D[1] + D[2]*D[2]
        b = 2 * (OC[0]*D[0] + OC[1]*D[1] + OC[2]*D[2])
        c = (OC[0]*OC[0] + OC[1]*OC[1] + OC[2]*OC[2]) - self.radius*self.radius

        delta = b*b - 4*a*c
        if delta < 0:
            return None, None

        sqrt_delta = delta ** 0.5
        t1 = (-b - sqrt_delta) / (2*a)
        t2 = (-b + sqrt_delta) / (2*a)
        return t1, t2
