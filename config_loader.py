import json
from object import Sphere
from lights import AmbientLight, PointLight, DirectionalLight

class SceneLoader:
    def __init__(self, scene):
        self.scene = scene

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.load_objects(data.get('objects', []))
        self.load_lights(data.get('lights', []))

    def load_objects(self, objects_data):
        for obj in objects_data:
            if obj.get('type') == 'sphere':
                self.scene.add_object(Sphere(
                    tuple(obj['center']), 
                    obj['radius'], 
                    tuple(obj['color']), 
                    obj['specular'], 
                    obj['reflective']
                ))

    def load_lights(self, lights_data):
        for l in lights_data:
            l_type = l.get('type')
            if l_type == 'ambient':
                self.scene.add_light(AmbientLight(l['intensity']))
            elif l_type == 'point':
                self.scene.add_light(PointLight(l['intensity'], tuple(l['position'])))
            elif l_type == 'directional':
                self.scene.add_light(DirectionalLight(l['intensity'], tuple(l['direction'])))
