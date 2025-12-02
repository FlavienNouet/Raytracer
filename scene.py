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

    def intersect(self, O, D):
        """
        Trouve la première intersection du rayon (O, D) avec un objet de la scène.
        Retourne (objet, distance) ou (None, None) s'il n'y a pas d'intersection.
        """
        closest_t = float('inf')
        closest_obj = None
        
        for obj in self.objects:
            t = obj.intersect(O, D)
            if t is not None and t < closest_t:
                closest_t = t
                closest_obj = obj
        
        if closest_obj is None:
            return None, None
        return closest_obj, closest_t
