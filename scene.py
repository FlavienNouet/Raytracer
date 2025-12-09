# scene.py

class Scene:
    def __init__(self):
        self.objects = []    # Liste des objets 3D (ex : sphères)
        self.lights = []     # Liste des sources lumineuses
        self.camera = None   # Objet caméra (position, rotation, etc.)

    def add_object(self, obj):
        self.objects.append(obj)

    def add_light(self, light):
        self.lights.append(light)

    def set_camera(self, camera):
        self.camera = camera

    def closest_intersection(self, O, D, t_min, t_max):
        """
        Trouve l'intersection la plus proche entre t_min et t_max.
        Retourne (objet, distance) ou (None, inf) s'il n'y a pas d'intersection.
        """
        closest_t = float('inf')
        closest_obj = None

        for obj in self.objects:
            t1, t2 = obj.intersect(O, D)
            for t in (t1, t2):
                if t is None:
                    continue
                if t_min <= t <= t_max and t < closest_t:
                    closest_t = t
                    closest_obj = obj

        if closest_obj is None:
            return None, float('inf')
        return closest_obj, closest_t

    def intersect(self, O, D):
        """
        Compatibilité arrière : intersection la plus proche sur [0, +inf).
        """
        return self.closest_intersection(O, D, 0.0, float('inf'))
