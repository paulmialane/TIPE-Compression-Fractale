from cmath import isnan
from Block import Block
import numpy as np

def searchDistance(block : Block, sourceBlocks : list) -> tuple:
    """
    Revoie un couple avec la distance minimale au bloc [block], l'indice du bloc de la liste [sourceBlocks], ainsi
    que comment ajuster le contrast et la luminosité.

    Parametres :

    [block] : Block -> Le bloc que l'on veut comparer
    [sourceBlocks] : list -> La liste des blocs avec lesquels comparer
    """
    minimumDistance, minimumIndice, minS, minO = float('inf'), None, float('inf'), float('inf')
    for indice in range(len(sourceBlocks)):
        b=sourceBlocks[indice]
        s, o = solveRMS(b.data, block.data)
        b=sourceBlocks[indice].transform(i=0, s=s, o=o)
        distance = block.distance(b)
        if distance < minimumDistance:
            minimumIndice = indice
            minimumDistance = distance
            minS = s
            minO = o
    return (minimumDistance, minimumIndice, minS, minO)

def solveRMS(A : np.array, B : np.array) -> tuple:
    n, m = A.shape
    mefiance = (n*m*np.sum(A*A) - (np.sum(A)**2))
    if mefiance == 0:
        return 0, np.sum(B)/(n*m)
    else:
        s = (n*m*np.sum(A*B)-(np.sum(A)*np.sum(B)))/mefiance
        o = (np.sum(B)- s*(np.sum(A)))/(n*m)
        return s,o

class Searcher :
    """
    Represente l'algorithme de recherche
    
    """
    def __init__(self, blocks : list) -> None:
        """
        Creer la liste des blocs dans lesquels chercher

        Parametres :

        [blocks] : list -> Listes des blocs dans laquelle chercher
        """
        self.blocks = blocks
    
    def search(self, block : Block) -> int:
        """
        Renvoie le bloc de la liste le plus proche du bloc passé en paramètre

        Parametres :

        [block] : Block -> Un bloc avec lequel comparer
        """
        _, indice, s, o = searchDistance(block, self.blocks)
        return indice, s, o