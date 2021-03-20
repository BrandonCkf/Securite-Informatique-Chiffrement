# --- Programme de chiffrement César ---
# Programme qui va réaliser un chiffrement César sur un message à partir de la clé donnée.
# Entrées :
#   - (cle) : Une clé de type entier
#   - (string) : Un message en chaine de caractère.
# Sortie : Un message chiffré ou déchiffré.

# Constantes qui détermine l'indice du premier et du dernier caractère à considérer dans la table ASCII
MINASCII = 32
MAXASCII = 126

def chiffreCesar(cle, string):
    str = ""
    #Pour chaque caractère du message à considérer traduit en code ASCII,
        #on déplace son code de cle indice de la table ASCII entre les caractères lisibles de la table
    for i in string:
        count = cle
        asc = ord(i)
        #Tant que le compteur ne vaut pas 0, on déplace l'indice du caractère de la table ASCII
        while count > 0:
            #Si le code ASCII du caractère considéré vaut 126, soit le code du dernier caractère lisible dans la table ASCII,
                #alors le caractère considéré vaut 32, soit le code du premier caractère lisible de la table ASCII
            if asc == MAXASCII:
                asc = 32
            #Sinon, on incrémente de 1 en 1 l'indice du caractère de la table ASCII
            else:
                asc = asc + 1
            count = count - 1
        str = str + chr(asc)
    return(str)


# --- Programme de déchiffrement César ---
# Programme qui va réaliser un déchiffrement César sur un message à partir de la clé donnée.
# Entrées :
#   - (cle) : Une clé de type entier
#   - (string) : Un message en chaine de caractère.
# Sortie : Un message déchiffré.
def dechiffreCesar(cle,string):
    str = ""
    #Pour chaque caractère du message à considérer traduit en code ASCII,
        #on déplace son code de cle indice de la table ASCII entre les caractères lisibles de la table
    for i in string:
        count = cle
        asc = ord(i)
        #Tant que le compteur ne vaut pas 0, on déplace l'indice du caractère de la table ASCII
        while count > 0:
            #Si le code ASCII du caractère considéré vaut 32, soit le code du premier caractère lisible dans la table ASCII,
                #alors le caractère considéré vaut 126, soit le code du dernier caractère lisible de la table ASCII
            if asc == MINASCII:
                asc = 126
            #Sinon, on incrémente de 1 en 1 l'indice du caractère de la table ASCII
            else:
                asc = asc - 1
            count = count - 1
        str = str + chr(asc)
    return(str)
