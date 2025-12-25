# utils.py

# Produit scalaire = calcul si deux vecteurs vont dans la même direction
def dot(v, w):
    """dot(v, w) - Produit scalaire entre deux vecteurs 3D"""
    return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]

# Normaisation d'un vecteur = vecteur en vecteur de longueur 1
def normalize(v):
    """normalize(v) - Normalise un vecteur (longueur = 1)"""
    length = longueur(v)
    if length == 0:
        return (0.0, 0.0, 0.0)
    return (v[0]/length, v[1]/length, v[2]/length)

# Calcul de la longueur d'un vecteur
def longueur(v):
    """longueur(v) - Norme euclidienne d'un vecteur"""
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

# Savoir si on touche une sphere
def intersect_sphere(O, D, C, r):
    """
    O : Origine, D : Direction, C : Centre de la sphere, r : Rayon
    """
    OC = (O[0]-C[0], O[1]-C[1], O[2]-C[2]) # Distance entre l'origine et le contre le la sphere
    a = dot(D, D) # Calcul de l'impact
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
