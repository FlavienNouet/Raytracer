# raytracer.py
from utils import dot, longueur, normalize
from math import sqrt

def trace_ray(scene, O, D, t_min, t_max, recursion_depth):
    closest_sphere, closest_t = scene.intersect(O, D)

    if closest_sphere is None:
        return (0.0, 0.0, 0.0)

    P = (O[0] + closest_t * D[0], O[1] + closest_t * D[1], O[2] + closest_t * D[2])
    N = (P[0] - closest_sphere.center[0], P[1] - closest_sphere.center[1], P[2] - closest_sphere.center[2])
    N = normalize(N)

    # CORRECTION 1: calcul_eclairage retourne UN FLOAT (intensité scalaire)
    intensity = calcul_eclairage(scene, P, N, (-D[0], -D[1], -D[2]), closest_sphere.specular)
    
    local_color = (
        closest_sphere.color[0] * intensity,
        closest_sphere.color[1] * intensity, 
        closest_sphere.color[2] * intensity
    )

    r = closest_sphere.reflective

    if recursion_depth <= 0 or r <= 0:
        return local_color

    R = reflect_ray((-D[0], -D[1], -D[2]), N)
    reflected_color = trace_ray(scene, P, R, 0.001, float('inf'), recursion_depth - 1)

    return (
        local_color[0] * (1 - r) + reflected_color[0] * r,
        local_color[1] * (1 - r) + reflected_color[1] * r,
        local_color[2] * (1 - r) + reflected_color[2] * r
    )

def calcul_eclairage(scene, P, N, V, s):
    # CORRECTION 2: i = 0.0 (float scalaire) au lieu de tuple
    i = 0.0
    for light in scene.lights:
        if light.type == 'ambient':
            i += light.intensity  # float unique
        else:
            if light.type == 'point':
                L = (light.position[0] - P[0], light.position[1] - P[1], light.position[2] - P[2])
                t_max = 1.0
            else:  # directional
                L = light.direction
                t_max = float('inf')

            shadow_sphere, shadow_t = scene.intersect(P, normalize(L))

            if shadow_sphere is not None:
                continue

            L = normalize(L)
            n_dot_l = dot(N, L)
            if n_dot_l > 0:
                # CORRECTION 3: light.intensity est float
                i += light.intensity * n_dot_l

            if s != -1:
                R = (2 * N[0] * dot(N, L) - L[0], 2 * N[1] * dot(N, L) - L[1], 2 * N[2] * dot(N, L) - L[2])
                r_dot_v = dot(R, V)
                if r_dot_v > 0:
                    specular_factor = (r_dot_v / (longueur(R) * longueur(V))) ** s
                    i += light.intensity * specular_factor

    return i  # Retourne float

def reflect_ray(I, N):
    return (
        I[0] - 2 * N[0] * dot(I, N),
        I[1] - 2 * N[1] * dot(I, N),
        I[2] - 2 * N[2] * dot(I, N)
    )
