class Pile:
    """
    Classe qui gère une pile.
    """
    def __init__(self):
        """
        Constructeur de la classe Pile.
        """
        self.__pile = []
        
    def est_vide(self):
        """
        Fonction qui renvoie True si la pile est vide, False sinon.
        return : bool
        """
        return self.__pile == []
    
    def taille(self):
        """
        Fonction qui renvoie la taille de la pile.
        return : int
        """
        return len(self.__pile)
    
    def empile(self,val):
        """
        param val : int
        Fonction qui empile la valeur val à la pile.
        """
        self.__pile.append(val)
        
    def depile(self):
        """
        Fonction qui dépile la pile.
        return le dernier élément de la pile.
        """
        if self.est_vide() :
            return None
        return self.__pile.pop()
    
    def __str__(self):
        """
        Fonction qui renvoie une représentation de la pile.
        return : str
        """
        res = "Entrée - "
        if self.est_vide() :
            return "La pile est vide."
        for e in self.__pile :
            res += f">{e}"
        res += " - Sortie"
        return res
    
class File:
    """
    Classe qui gère une file.
    """
    def __init__(self):
        """
        Constructeur de la classe File.
        """
        self.__file = []
        
    def est_vide(self):
        """
        Fonction qui renvoie True si la file est vide, False sinon.
        return : bool
        """
        return self.__file == []
    
    def taille(self):
        """
        Fonction qui renvoie la taille de la file.
        return : int
        """
        return len(self.__file)
    
    def enfile(self,val):
        """
        param val : int
        Fonction qui enfile la valeur val à la file.
        """
        self.__file.append(val)
        
    def defile(self):
        """
        Fonction qui dépile la file.
        return le premier élément de la file.
        """
        if self.est_vide() :
            raise "ERROR"
        return self.__file.pop(0)
    
    def __str__(self):
        """
        Fonction qui renvoie une représentation de la file.
        return : str
        """
        res = "Entrée/Sortie - "
        if self.est_vide() :
            return "La file est vide."
        for e in self.__file :
            res += f">{e}"
        return res
    