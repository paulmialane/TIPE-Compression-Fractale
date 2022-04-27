from Block import Block
import Cut
from Searcher import Searcher
import numpy as np


class Ifs :
    """
    Represente un IFS

    Interet : Si on veut compresser une image coloré, on separe l'image est 3 IFS (R, G, B), et on travaille sur chacun
    
    """
    def __init__(self, smallSize : int) -> None:
        """
        Creer un IFS

        Parametres : 

        [smallSize] : int -> taille des blocks de destination (range)
        
        """

        self.smallSize = smallSize
        self.ranges = []
    
    def apply(self, image : np.array) -> np.array:
        """
        Applique l'IFS a une image donnée

        Parametres : 

        [image] : np.array -> Image a laquelle on applique l'IFS
        
        """
        sources = [Block(data=b, dimensions=(self.smallSize*2, self.smallSize*2)) for b in Cut.cut(size=self.smallSize * 2, image=image)]
        destinations = []
        for indice, s, o in self.ranges :
            i, transformation = indice // 8, indice % 8
            destinations.append(sources[i].transform(transformation, s, o).data)
        
        return Cut.rebuild(size=self.smallSize, blockList=destinations, dimensions=image.shape)

    def search(self, image : np.array) -> object:
        """
        Creer l'IFS associé à une image

        Parametres :

        [size] : int -> Taille des blocs de destinations
        [image] : np.array -> Image que l'on souhaite représenter
        """

        sources = [Block(data=b, dimensions=(self.smallSize*2, self.smallSize*2)) for b in Cut.cut(size=self.smallSize*2, image=image)]
        destinations = [Block(data=b, dimensions=(self.smallSize, self.smallSize)) for b in Cut.cut(size=self.smallSize, image=image)]
        allPossibility = []
        for block in sources:
            for transformation in range(8):
                allPossibility.append(block.transform(transformation).reduce(factor=2))
        G = Searcher(allPossibility)
        
        for i in range(len(destinations)) :
            print("{}% effectué".format(int(i/len(destinations) * 100)))
            indice, s , o = G.search(destinations[i])
            self.ranges.append( (indice, s, o) )
        



