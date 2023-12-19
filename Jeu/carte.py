import random
from Jeu.pile_file import Pile,File
import colorama
colorama.init()


class Carte :
    """
    Classe qui gère une carte.
    """
    def __init__(self,nombre, symbole):
        """
        param nombre : int
        param symbole : str
        Constructeur de la classe Carte.
        """
        self.__nombre = nombre #compris entre 2 et 14 (14 c'est l'as)
        self.__symbole = symbole
    
    def get_nombre(self):
        """
        Fonction qui renvoie le nombre de la carte.
        return : int
        """
        return self.__nombre
    
    def __eq__(self,autre_carte):
        """
        param autre_carte : Carte()
        Fonction qui renvoie True si les cartes sont égales, False sinon.
        return : bool
        """
        return self.__nombre == autre_carte.get_nombre()


    def __lt__(self,autre_carte):
        """
        param autre_carte : Carte()
        Fonction qui renvoie True si la carte est inférieure à l'autre, False sinon.
        return : bool
        """
        return self.__nombre < autre_carte.get_nombre()
    
    def __gt__(self,autre_carte):
        """
        param autre_carte : Carte()
        Fonction qui renvoie True si la carte est supérieure à l'autre, False sinon.
        return : bool
        """
        return self.__nombre > autre_carte.get_nombre()
    
    def get_true_nombre(self):
        """
        Fonction qui renvoie le vrai nom de la carte.
        return : str
        """
        if self.__nombre == 11 :
            return "Valet"
        elif self.__nombre == 12 :
            return "Dame"
        elif self.__nombre == 13 :
            return "Roi"
        elif self.__nombre == 14 :
            return "As"
        return self.__nombre
    
    def __str__(self):
        """
        Fonction qui renvoie une représentation de la carte.
        return : str
        """
        return f"{self.get_true_nombre()} de {self.__symbole}"


class Paquet :
    """
    Classe qui gère un paquet de carte.
    """
    def __init__(self):
        """
        Constructeur de la classe Paquet.
        """
        self.__paquet = self.generer_paquet()

    def generer_paquet(self):
        """
        Fonction qui génère un paquet de carte.
        return : List[Carte()]
        """
        symbole_dispo = [colorama.Fore.RED + "♦" + colorama.Style.RESET_ALL,colorama.Fore.RED + "♥" + colorama.Style.RESET_ALL,"♠","♣"]
        paquet = []
        for nombre in range(2,15):
            for symbole in symbole_dispo:
                paquet.append(Carte(nombre,symbole))
        random.shuffle(paquet)
        return paquet

    def diviser_paquet(self):
        """
        Fonction qui divise le paquet en deux.
        return : File(), File()
        """
        paquet1 = File()
        paquet2 = File()
        
        for i in range(len(self.__paquet)//2) :
            paquet1.enfile(self.__paquet[i])
            paquet2.enfile(self.__paquet[-(i + 1)])
         
        return paquet1, paquet2
    
    def __str__(self):
        """
        Fonction qui renvoie une représentation du paquet.
        return : str
        """
        res = "Paquet: "
        for elt in self.__paquet :
            res += f"{elt}, "
        return res
    
            