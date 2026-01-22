# Raytracer _  Moteur de rendu par lancer de rayons

Ce projet est un moteur de rendu par lancer de rayons autrement appelé ray-tracing développé en python. Il permet de générer des images de synthèses réalistes en simulant un parcours de lumière. Le programme renvoie un rendu de sphères colorés, une gestion de différentes sources de lumières et une animations au format GIF via des rendus PPM.

## User Guide

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de packages Python)

### Installation et déploiement

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/FlavienNouet/Raytracer.git
   cd Dashboard_python
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Sur Linux/macOS
   # ou
   .venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application**
   ```bash
   python main.py
   ```

5. **Accéder au rendu**
   Les rendus individuels sont générés au format PPM. Una animation finale regroupent les images au format PPM. 


### Structure des données

## Developer Guide

### Architecture du projet

```
- `output/`        : dossier contenant les rendus PPM et GIF.
- `main.py`        : point d'entrée qui configure la scène, les objets et le rendu.
- `raytracer.py`   : logique de ray-tracing et éclairage.
- `canvas.py`      : gère les grille de pixel(canvas), et l'exportation vers le format PPM.
- `object.py`      : contient les objets et la classe Sphere.
- `lights.py`      : définit les différents types de lumières.
- `scene.py`       : gestion scène en regroupant les objets et la lumière.
- `utils.py`       : fonctions mathméatiques utilitaires.
- `config_loader.py`       : charge les objets configurés dans le json.
- `scene.json`     : fichier de configuration de la scène.
```

## Fonctionnement technique 

Le raytracer repose sur le principe de la résolution mathématique de l'intersection entre un rayon et une sphère. 
Le moteur calcule ensuite l'intensité lumineuse au point d'impact avec les différentes sources de lumières. 

### Copyright

Je déclare sur l'honneur que le code fourni a été produit par moi-même, à l'exception des références théoriques citées ci-dessous :

    - L'algorithme de base et les concepts mathématiques sont inspirés de l'ouvrage "Computer Graphics from Scratch" de Gabriel Gambetta.
