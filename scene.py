
class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []
        self.camera = None

    def add_object(self, obj):
        self.objects.append(obj)

    def add_light(self, light):
        self.lights.append(light)

    def set_camera(self, camera):
        self.camera = camera

    def closest_intersection(self, O, D, t_min, t_max):
        closest_t = float('inf')
        closest_obj = None

        for obj in self.objects:
            t1, t2 = obj.intersect(O, D)
            for t in (t1, t2):
                if t is None:
                    continue
                if t_min <= t <= t_max and t < closest_t:
                    closest_t = t  # Distance de l'objet le plus proche
                    closest_obj = obj

        if closest_obj is None:
            return None, float('inf')
        return closest_obj, closest_t

    # Intercepte l'objet le plus proche
    def intersect(self, O, D):
        return self.closest_intersection(O, D, 0.0, float('inf'))
