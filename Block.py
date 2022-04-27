import numpy as np
from Transformation import *

class Block :
    """
    Représente un bloc d'une image.

    Infos:
    Dans notre modèle, les blocs sont seulement carrés donc ils sont représentés par des tableaux numpy
    de dimensions (n*n)

    """
    def __init__(self, data=None, dimensions=(8, 8)) -> None:
        """
        Creer un nouveau bloc.

        Parametres:
        [dimensions] : (int * int) -> Les dimensions de notre bloc (par défaut 8x8)
        [data] : None / np.array -> Les données que doit contenir notre bloc (Si None, on initialise un bloc aléatoire)
        """

        self.dimensions=dimensions

        if not (data is None) : self.data = data
        else : self.data = np.array(np.random.random(self.dimensions)*256, dtype=int)
    
    def __add__(self, other : object) -> object:
        """
        Additionne les valeurs de deux blocs (2 à 2) lorsque les dimensions sont compatibles

        Parametres :
        [other] : Block -> Le bloc avec lequel on veut additionner
        """
        if other.dimensions == self.dimensions:
            return Block(dimensions=self.dimensions, data=(self.data + other.data))
        else:
            raise Exception("Dimensions incompatibles")
    
    def transform(self, i : int, s=1, o=0) -> object:
        """
        Renvoie le bloc obtenu en appliquant a ce bloc la i-ème transformation

        Parametres :
        [i] : int -> Le numero de la transformation
        """
        if 0 <= i <= 7:
            transformation = ensembleTransformation[i]
            nouveau = Block(dimensions=self.dimensions, data=self.data)
            for sousTransformation in transformation:
                nouveau = Block(dimensions=nouveau.dimensions, data=sousTransformation(nouveau.data))
            nouveau=Block(dimensions=nouveau.dimensions, data=contrast(nouveau.data, s))
            nouveau=Block(dimensions=nouveau.dimensions, data=brightness(nouveau.data, o))
            return nouveau
        else:
            raise Exception("Transformation inconnue")

    def distance(self, other : object) -> float:
        """
        Renvoie la distance entre deux blocs (ici c'est la somme des carrées des differences)

        Parametres :
        [other] : Block -> Le bloc avec lequel on veut se comparer

        Idee : Implementer d'autre mesure de distance peut être plus fiable... (Metrique de Haussdorf en temps raisonnable?)
        """

        if self.dimensions == other.dimensions:
            return np.sum((self.data - other.data)**2)
        else: return float('inf')

    def reduce(self, factor : int) -> object:
        """
        Réduire la taille d'un bloc en moyennant les pixels

        Parametres : 

        [factor] : int -> Facteur par lequel réduire les dimensions du bloc
        """
        l, h = self.dimensions[0]//factor, self.dimensions[1]//factor
        result = np.zeros((l, h))
        for i in range(l):
            for j in range(h):
                result[i,j] = np.mean(self.data[i*factor:(i+1)*factor,j*factor:(j+1)*factor])
                
        return Block(data=result, dimensions=(l, h))