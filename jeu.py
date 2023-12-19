from Jeu.carte import Paquet,Carte
from Jeu.pile_file import Pile,File

class Bataille:
    """
    Classe qui gère le jeu de la bataille.
    """
    def __init__(self):
        """
        Constructeur de la classe Bataille.
        """
        self.__tour = 0
        
    def tour(self,j1,j2):
        """
        param j1 : File
        param j2 : File
        Fonction qui gère un tour de jeu.
        """
        c1 = j1.defile()
        c2 = j2.defile()

        print(f"Joueur1 : {c1}\nJoueur2 : {c2}")
        
        if c1 > c2 :
            j1.enfile(c1)
            j1.enfile(c2)
            print('Le Joueur 1 gagne la manche')
            
        elif c1 < c2  :
            j2.enfile(c1)
            j2.enfile(c2)
            print('Le Joueur 2 gagne la manche')
            
        else :
            autre_carte = [c1,c2]
            self.bataille(j1,j2,autre_carte)
            
    
    def bataille(self,j1,j2,autre_carte = []):
        """
        param j1 : File
        param j2 : File
        param autre_carte : List[Carte()]
        Fonction qui gère une bataille.
        """
        print('\nBataille :')
        c3 = j1.defile()
        c4 = j2.defile()
        c5 = j1.defile()
        c6 = j2.defile()
        autre_carte += [c3,c4,c5,c6]
        print(f"Joueur1 : Cachée\nJoueur2 : Cachée\n")
        print(f"Joueur1 : {c5}\nJoueur2 : {c6}")
        
        if c5 > c6 :
            for carte in autre_carte:
                j1.enfile(carte)
            print('Le Joueur 1 Gagne')
                  
        elif c5 < c6  :
            for carte in autre_carte:
                j2.enfile(carte)
            print('Le Joueur 2 Gagne')
            
        else :
            self.bataille(j1,j2,autre_carte)
    
    def jeu(self):
        """
        Fonction qui gère le jeu.
        """
        paquets = Paquet().diviser_paquet()
        j1 = paquets[0]
        j2 = paquets[1]
        while not j1.est_vide() and not j2.est_vide():
            self.__tour += 1
            print(f"\n---- TOUR : {self.__tour} ----")
            
            try:
                self.tour(j1,j2)
            except:
                break
            print(f"\nLe joueur 1 a {j1.taille()} cartes,\nLe joueur 2 a {j2.taille()} cartes")
            
        if j1.est_vide() :
            print(f"\nLe Joueur 2 est le Gagnant au tour : {self.__tour}")
        elif j2.est_vide() :
            print(f"\nLe Joueur 1 est le Gagnant au tour : {self.__tour}")
            
            
    
        
        

    