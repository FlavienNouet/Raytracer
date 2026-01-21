from math import inf
from utils import dot, longueur, normalize

# Lance les rayons
def trace_ray(scene, O, D, t_min, t_max, recursion_depth):
    closest_sphere, closest_t = scene.closest_intersection(O, D, t_min, t_max)
    if closest_sphere is None:
        return (0.0, 0.0, 0.0)

    P = (O[0] + closest_t * D[0], O[1] + closest_t * D[1], O[2] + closest_t * D[2]) # Point d'intersection
    N = normalize((P[0] - closest_sphere.center[0], P[1] - closest_sphere.center[1], P[2] - closest_sphere.center[2])) # Normale au point d'intersection

    # Intensité de l'éclairage
    intensity = calcul_eclairage(scene, P, N, (-D[0], -D[1], -D[2]), closest_sphere.specular)
    local_color = (
        closest_sphere.color[0] * intensity,
        closest_sphere.color[1] * intensity,
        closest_sphere.color[2] * intensity,
    )

    # Gestion des réflexions
    r = closest_sphere.reflective
    if recursion_depth <= 0 or r <= 0:
        return local_color

    R = reflect_ray((-D[0], -D[1], -D[2]), N)
    reflected_color = trace_ray(scene, P, R, 0.001, inf, recursion_depth - 1)

    # Couleur reflétée
    return (
        local_color[0] * (1 - r) + reflected_color[0] * r,
        local_color[1] * (1 - r) + reflected_color[1] * r,
        local_color[2] * (1 - r) + reflected_color[2] * r,
    )


# Calcul de l'éclairage sur un point précis 
def calcul_eclairage(scene, P, N, V, s):
    i = 0.0
    for light in scene.lights:
        if light.type == 'ambient':
            i += light.intensity
            continue

        if light.type == 'point':
            L = (light.position[0] - P[0], light.position[1] - P[1], light.position[2] - P[2])
            t_max = longueur(L)
        else:  
            L = light.direction 
            t_max = inf

        if longueur(L) == 0:
            continue

        L_dir = normalize(L)
        shadow_sphere, _ = scene.closest_intersection(P, L_dir, 0.001, t_max)
        if shadow_sphere is not None:
            continue
        
        n_dot_l = dot(N, L_dir)
        if n_dot_l > 0:
            i += light.intensity * n_dot_l

        if s != -1:
            R = reflect_ray(L_dir, N) 
            r_dot_v = dot(R, V)
            denom = longueur(R) * longueur(V)
            if r_dot_v > 0 and denom > 0:
                i += light.intensity * (r_dot_v / denom) ** s

    return i

def reflect_ray(I, N):
    factor = 2 * dot(N, I)
    return (
        factor * N[0] - I[0],
        factor * N[1] - I[1],
        factor * N[2] - I[2],
    )
