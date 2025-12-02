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
        Intersection rayon-sphère:
        P = O + tD
        ||P - C||^2 = r^2
        Rend la distance t au point d'intersection le plus proche > 0, ou None si pas d'intersection.
        O: origine du rayon (tuple)
        D: direction du rayon (tuple normalisé)
        """
        OC = (O[0] - self.center[0], O[1] - self.center[1], O[2] - self.center[2])
        a = D[0]*D[0] + D[1]*D[1] + D[2]*D[2]
        b = 2 * (OC[0]*D[0] + OC[1]*D[1] + OC[2]*D[2])
        c = (OC[0]*OC[0] + OC[1]*OC[1] + OC[2]*OC[2]) - self.radius*self.radius

        delta = b*b - 4*a*c
        if delta < 0:
            return None

        t1 = (-b - delta**0.5) / (2*a)
        t2 = (-b + delta**0.5) / (2*a)

        if t1 > 0:
            return t1
        if t2 > 0:
            return t2
        return None
