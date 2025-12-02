#Intersection rayon et la spphère
IntersectRaySphere(O, D, sphère) {
    r = sphère.rayon
    CO = O - sphère.centre

    a = dot(D, D)
    b = 2 * dot(CO, D)
    c = dot(CO, CO) - r*r

    discriminant = b*b - 4*a*c

    si discriminant < 0 {
        retourner inf, inf
    }

    t1 = (-b + sqrt(discriminant)) / (2*a)
    t2 = (-b - sqrt(discriminant)) / (2*a)

    retourner t1, t2
}


#Calul de la couleur du pixel en fonction des intersections + lumières
TraceRay(O, D, t_min, t_max, profondeur_récursion) {
    sphère_la_plus_proche, t_le_plus_proche = Intersection_la_plus_proche(O, D, t_min, t_max)

    si closest_sphere == NULL {
        renvoyer COULEUR_D'ARRIÈRE-PLAN
    }

    P = O + plus proche_t * D
    N = P - centre de la sphère la plus proche
    N = N / longueur(N)

    couleur_locale = sphère_la_plus_proche.couleur *
        CalculÉclairage(P, N, -D, sphère_la_plus_proche.spéculaire)

    r = closest_sphere.reflective

    si la profondeur de récursion est inférieure ou égale à 0 ou si r est inférieur ou égal à 0 {
        renvoyer la couleur locale
    }

    R = ReflectRay(-D, N)

    couleur_réfléchie = TraceRay(P, R, 0.001, inf, profondeur_récursion - 1)

    renvoie la couleur locale * (1 - r) + la couleur réfléchie * r
}

#Calcul des ombres et des reflets
Calcul de l'éclairage(P, N, V, s) {
    i = 0,0
    pour la lumière dans la scène.Lumières {
        si light.type == ambient {
            i += intensité lumineuse
        } autre {
            si light.type == point {
                L = position de la lumière - P
                t_max = 1
            } autre {
                L = direction de la lumière
                t_max = inf
            }

            shadow_sphere, shadow_t = ClosestIntersection(P, L, 0.001, t_max)

            si shadow_sphere != NULL {
                continuer
            }

            n_dot_l = dot(N, L)
            si n_dot_l > 0 {
                i += intensité_lumière * n_dot_l / (longueur(N) * longueur(L))
            }

            si s != -1 {
                R = 2 * N * dot(N, L) - L
                r_dot_v = dot(R, V)
                si r_dot_v > 0 {
                    i += intensité_lumière * pow(r_dot_v / (longueur(R) * longueur(V)), s)
                }
            }
        }
    }

    retour i
}