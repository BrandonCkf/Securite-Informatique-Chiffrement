# --- Programme de chiffrement Vigenere ---
# Programme qui va réaliser un chiffrement Vigenère sur un message à partir de la clé donnée.
# Entrées :
#   - (cle) : Une clé de type chaine de caractère
#   - (string) : Un message en chaine de caractère.
# Sortie : Un message chiffré.
def chiffreVigenere(cle,string):
    str = ""
    li = list()
    #Pour chaque caractère de la clé, on récupère le code ASCII du caractère  
    for i in cle:
        ascCle = ord(i) - 32
        li.append(ascCle)
    indiceTab = 0
    #Pour chaque caractère du message, on récupère le code ASCII du caractère et on va déplacer l'indice de la table ASCII
        # jusqu'à ce que le nombre de déplacement correspond au caractère de la clé considéréé
    for c in string:
        ascStr = ord(c)
        compteur = li[indiceTab]
        #Tant que le compteur correspondant à un caractère de la clée considérée ne vaut pas 0, on déplace l'indice du caractère considérée dans le message
        while compteur > 0 :
            #Si l'indice du caractère vaut 126, soit le dernier caractère lisible de la table ASCII,
                #On se déplace au 32e caractère de la table ASCII, soit le premier caractère lisible
            if ascStr == 126 :
                ascStr = 32
            #Sinon, l'indice du caractère est déplacé par pas de 1 par rapport aux indices de la table ASCII
            else:
                ascStr = ascStr + 1
            compteur = compteur-1
        #Si on arrive au dernier caractère de la clé, on revient au premier caractère de celle-ci
        if indiceTab == len(li)-1:
            indiceTab = 0
        #Sinon, on déplace le caractère de la clé de 1
        else:
            indiceTab = indiceTab + 1
        str = str + chr(ascStr)
    return(str)

# --- Programme de déchiffrement Vigenere ---
# Programme qui va réaliser un déchiffrement Vigeznère sur un message à partir de la clé donnée.
# Entrées :
#   - (clé) : Une clé de type chaine de caractère
#   - (string) : Un message en chaine de caractère.
# Sortie : Un message déchiffré.
def dechiffreVigenere(cle,string):
    str = ""    
    li = list()
    #Pour chaque caractère de la clé, on récupère le code ASCII du caractère  
    for i in cle:
        ascCle = ord(i) - 32
        li.append(ascCle)
    indiceTab = 0
    #Pour chaque caractère du message, on récupère le code ASCII du caractère et on va déplacer l'indice de la table ASCII
        # jusqu'à ce que le nombre de déplacement correspond au caractère de la clé considéréé
    for c in string:
        ascStr = ord(c)
        compteur = li[indiceTab]
        #Tant que le compteur correspondant à un caractère de la clée considérée ne vaut pas 0, on déplace l'indice du caractère considérée dans le message
        while compteur > 0 :
            #Si l'indice du caractère vaut 32, soit le premier caractère lisible de la table ASCII,
                #On se déplace au 126e caractère de la table ASCII, soit le dernier caractère lisible
            if ascStr == 32 :
                ascStr = 126
            # Sinon, on décrémente l'indice du caractère du message de 1
            else:
                ascStr = ascStr - 1
            compteur = compteur-1
        #Si on arrive au dernier caractère de la clé, on revient au premier caractère de celle-ci
        if indiceTab == len(li)-1:
            indiceTab = 0
        #Sinon, on déplace le caractère de la clé de 1
        else:
            indiceTab = indiceTab + 1
        str = str + chr(ascStr)
    return(str)
