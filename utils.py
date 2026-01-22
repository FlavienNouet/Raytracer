# Produit scalaire = calcul si deux vecteurs vont dans la même direction
def dot(v, w):
    return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]

# Normalisation d'un vecteur = vecteur de longueur 1
def normalize(v):
    length = longueur(v)
    if length == 0:
        return (0.0, 0.0, 0.0)
    return (v[0]/length, v[1]/length, v[2]/length)

# Longueur d'un vecteur
def longueur(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

# Intersection avec une sphère
def intersect_sphere(O, D, C, r):
    OC = (O[0]-C[0], O[1]-C[1], O[2]-C[2])
    a = dot(D, D)
    b = 2 * dot(OC, D)
    c = dot(OC, OC) - r*r
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
