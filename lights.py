# Mise en place des lumières 

class AmbientLight:
    def __init__(self, intensity):  # Lumière ambiante => eclaire tous les objets de manière uniforme
        self.type = 'ambient'
        self.intensity = intensity

class PointLight:
    def __init__(self, intensity, position):  # Lumèe localisée = comme une ampoule
        self.type = 'point'
        self.intensity = intensity
        self.position = position

class DirectionalLight:
    def __init__(self, intensity, direction): # Lumière directionnelle = comme le soleil
        self.type = 'directional'
        self.intensity = intensity
        self.direction = direction
