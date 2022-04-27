
# Fichier contenant l'ensemble des tranformations possibles


import numpy as np
from math import pi, ceil

def id(data : np.array) -> np.array :
    return data

def flip(data : np.array) -> np.array: 
    """
    Renvoie le symétrique d'un np.array selon l'axe des abscisses.
    
    Parametres : 

    [data] : np.array -> Données a transformer
    """
    return np.flip(data, 0)

def rot(data : np.array) -> np.array:
    """
    Renvoie un le np.array correspondant à une rotation de 90 degré de data.

    Parametres : 

    [data] : np.array -> Données a transformer
    """
    return np.rot90(data)

def contrast(data : np.array, s : float) -> np.array:
    """
    Modifie le contrast d'une image

    Parametres : 

    [data] : np.array -> Données a modifier
    [s] : -> Valeurs par laquelle on veut modifier le contrast
    """
    return int(s)*data

def brightness(data : np.array, o : float) -> np.array:
    """
    Modifie la luminosité d'une image

    Parametres

    [data] : np.array -> Données à modifier
    [o] : Luminosité a ajouter
    """

    return data + int(o)


# Ensemble des tranformations que l'on peut faire sur un carré

ensembleTransformation = [[id], [rot], [rot, rot], [rot, rot, rot], [flip], [flip, rot], [flip, rot, rot], [flip, rot, rot, rot]]