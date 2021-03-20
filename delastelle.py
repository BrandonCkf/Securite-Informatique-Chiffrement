# Chiffrement/Dechifrement par Delastelle

# Création de la classe carre polybe
class CarrePolybe:
    def __init__(self, key):
        self.key = key
        self.carre = [[-1 for i in range(6)] for j in range(6)]
        self.loading()
    
    # Charge les caractères dans le carre
    def loading(self):
        # Liste des chiffres et des lettres
        chiffres = [str(i) for i in range(10)]
        lettres = [chr(i) for i in range(ord("a"), ord("z")+1)]
        

        # Liste des symboles qui ne sont pas encore dans le carré
        symb = chiffres + lettres

        # Liste des symbole de la clé
        keySymb = list(self.key)

        # On commence par remplir avec les symboles de la clé
        for i in range(6):
            for j in range(6):
                if len(keySymb) != 0:
                    # Supprime et retourne le première élément de la liste
                    s = keySymb.pop(0)
                    if s in symb:
                        self.carre[i][j] = s
                        symb.remove(s)
                else:
                    if len(symb) != 0:
                        self.carre[i][j]  = symb.pop(0)
        
        return

    # Affiche la clé et le carré de polybe
    def display(self):
        print("Carré de polybe avec la clé {}:\n".format(self.key))

        for line in self.carre:
            print(line)
        return

    # Renvoie le carré sous forme de dictionnaire qui à chaque lettre associe sa position (ligne, colonne) dans le carré
    # ligne et colonne sous forme de string
    def toDict(self):
        res = dict()
        for i in range(6):
            for j in range(6):
                res[self.carre[i][j]] = (i, j)
        return res


# Fonction qui chiffre un msg avec Delastelle
# Input:
            # - key1: str, clé pour créer le carré de polybe
            # - key2: int, clé pour la longueur des fragments (non pair)
            # - msg: str, msg à chiffrer
# Output:
            # Le message chiffré par delastelle
def chiffreDelastelle(key1, key2, msg):
    # Ramménne les caractères du msg et de key1 en minuscule
    msg = msg.casefold()
    key1 = key1.casefold()

    # On ajoute des caractères x à la fin du msg afin que sa taille soit un multiple de key2
    msg = msg + ("x"*(key2-len(msg)%key2))

    # Créer le carré de polybe associé à key1
    carrePolybe = CarrePolybe(key1)
    # carrePolybe.display()

    # Récupères le carré de polybe associées à key1 sous forme de dictionnaire
    polybeDict = carrePolybe.toDict()

    # Liste des (ligne, colonne) associés à chaque lettre du msg par le carré de polybe
    lm = [polybeDict[c] for c in msg]
    
    # Gestion des fragments
    if key2%2 == 0:
        raise NameError("La clé 2 n'est pas impaire")

    # Liste des fragments
    lf = [[lm.pop(0) for i in range(key2)] for j in range(len(msg)//key2)]

    # Liste des fragment avec pour chaque fragment la liste des bigrammes éclatés
            # fragment[i%key2][i//key2] valeurs de la ligne du caractère i si i<key2 sinon valeurs de la colonne
    lfb = [[(fragment[i%key2][i//key2],fragment[(i+1)%key2][(i+1)//key2]) for i in range(0,key2*2,2)] for fragment in lf]

    # Retransformation des bigramme éclaté en texte
    res = ""

    for fragment in lfb:
        for bigramme in fragment:
            res += carrePolybe.carre[bigramme[0]][bigramme[1]]
    
    return res

# Fonction qui chiffre un msg avec Delastelle
# Input:
            # - key1: str, clé pour créer le carré de polybe
            # - key2: int, clé pour la longueur des fragments (non pair)
            # - msg: str, msg à déchiffrer
# Output:
            # Le message dechiffré par delastelle
def dechiffreDelastelle(key1, key2, msg):
    # Ramménne les caractères du msg et de key1 en minuscule
    msg = msg.casefold()
    key1 = key1.casefold()

    # Créer le carré de polybe associé à key1
    carrePolybe = CarrePolybe(key1)
    # carrePolybe.display()

    # Récupères le carré de polybe associées à key1 sous forme de dictionnaire
    polybeDict = carrePolybe.toDict()

    # Liste des (ligne, colonne) associés à chaque lettre du msg par le carré de polybe
    lm = [polybeDict[c] for c in msg]
    
    # Gestion des fragments
    if key2%2 == 0:
        raise NameError("La clé 2 n'est pas impaire")

    # Liste des fragments des bigrammes éclatés
    lfbe = [[lm.pop(0) for i in range(key2)] for j in range(len(msg)//key2)]

    # Liste des fragment avec pour chaque fragment la liste des bigrammes reconstitué
            # fragment[i//2][i%2] valeur de la ligne pour le ieme element
            # fragment[(i+key2)//2][(i+1)%2] valeur de la colonne pour le ieme element
    lfb = [[(fragment[i//2][i%2], fragment[(i+key2)//2][(i+1)%2] ) for i in range(key2)]for fragment in lfbe]

    # Retransformation des bigramme éclaté en texte
    res = ""

    for fragment in lfb:
        for bigramme in fragment:
            res += carrePolybe.carre[bigramme[0]][bigramme[1]]
    
    return res

if __name__ == "__main__":
    # Exemple de bibmath
    print(chiffreDelastelle("vbkua0clxrd1mysfn2zogpi3hqewt456789j", 11, "leloupestentredanslabergerie"))
    print(dechiffreDelastelle("vbkua0clxrd1mysfn2zogpi3hqewt456789j", 11, "druetyyrgnnqqkyvtgtedxrqillrsisss"))






