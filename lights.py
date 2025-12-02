#Différents type de lumières
class AmbientLight:
    def __init__(self, intensity):
        self.type = 'ambient'
        self.intensity = intensity


class PointLight:
    def __init__(self, intensity, position):
        self.type = 'point'
        self.intensity = intensity
        self.position = position


class DirectionalLight:
    def __init__(self, intensity, direction):
        self.type = 'directional'
        self.intensity = intensity
        self.direction = direction
