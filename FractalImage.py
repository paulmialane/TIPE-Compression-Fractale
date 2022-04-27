from PIL import Image
import numpy as np
from Ifs import Ifs


class FractalImage :

    """
    Represente notre image en Python
    (On utilise pas Image comme nom car c'est déja emprunté par PIL)
    
    """


    def __init__(self) -> None:

        """
        Creer une nouvelle image

        """

        self.dimensions = None
        self.data = None
        self.ifs = None
        self.smallSize = None
    
    def open(self, filename : str, smallSize : int) -> None:
        """
        Charge une image depuis un fichier, sous format FractalImage

        Parametres : 

        [filemane] : string -> Chemin du fichier en absolu (comme ca ça marchera toujours) à ouvrir
        [smallSize] : int -> Taille des blocs de destinations lors du découpage
        
        """

        pilImage = Image.open(filename).convert('L')
        self.data = np.array(pilImage)
        self.dimensions = self.data.shape
        self.smallSize=smallSize
        self.ifs = Ifs(smallSize=smallSize)
        self.ifs.search(self.data)
        print("J'ai fini de compresser ! ")
    

    def export(self, iteration : int) -> Image:
        """
        Exporte une FractalImage au format Image (PIL)

        Parametres : 

        [iterations] : int -> Nombre d'iteration de l'IFS à appliquer.
        
        """

        newImage = np.zeros(self.dimensions, dtype=int)
        for i in range(iteration):
            print("J'en suis à la {}-ième itération".format(i))
            newImage = self.ifs.apply(newImage)
        return Image.fromarray(newImage)
    

#On va tester quelques trucs (Probablement beaucoup beaucoup de bugs....)

im = FractalImage()
im.open(filename="1.jpg", smallSize=4)
s = im.export(10)
s.show()