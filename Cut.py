
#Contient le nécessaire au découpage et rassemblage de l'image

from math import ceil
import numpy as np

def cut(size : int, image : np.array) -> list:
    """
    Decoupe une image en bloc de même taille.
    Attention, il faut que [size] divise les dimensions de l'image...

    Parametres :

    [size] : int -> Taille des blocs (identiques à tout les blocs)
    [image] : np.array -> Image à découper
    """

    if image.shape[0] % size != 0 or image.shape[1] % size != 0: 
        raise Exception("Image indécoupable : dimensions incompatible")
    else:
        numberOfLine, numberOfColumn = ceil(image.shape[0]//size), ceil(image.shape[1]//size)
        blockList = []
        for i in range(numberOfLine):
            for j in range(numberOfColumn):
                blockList.append(image[size*i:size*(i+1), size*j:size*(j+1)])
        return blockList
    
def rebuild(size : int, blockList : list, dimensions : tuple) -> np.array:
    """
    Reconstitue une image à partir d'un ensemble de blocs

    Parametres:

    [size] : int -> Taille des blocs (identique à tous les blocs)
    [blockList] : list -> Ensemble des blocs
    [dimensions] : tuple -> Dimensions de l'image a reconstituer
    
    """
    numberOfLine, numberOfColumn = ceil(dimensions[0]//size), ceil(dimensions[1]//size)
    lines = [np.concatenate(blockList[numberOfColumn*i:numberOfColumn*(i+1)], axis=1) for i in range(numberOfLine)]

    def reduce(image : np.array, factor : int) -> np.array:
        l, h = image.shape[0]//factor, image.shape[1]//factor
        result = np.zeros((l, h))
        for i in range(l):
            for j in range(h):
                result[i,j] = np.mean(image[i*factor:(i+1)*factor,j*factor:(j+1)*factor])

        return result
    return reduce(np.concatenate(lines), 2)