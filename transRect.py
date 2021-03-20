# Transpositon rectangulaire
from math import ceil

# Fonction qui donne l'ordre des colonnes du rectangle
# Input:
            #  - key : la clé dont on doit donner l'ordre des caractères
# Output:
            # Une liste avec pour chaque caratères sa position (liste[0] == position du premier caractère de la clé)
def rangCleTransRect(key):
    # Liste des caractères de la clé
    l = list(key)

    # Liste des caractères de la clé triées dans l'ordre alphabétique
    lt = l.copy()
    lt.sort()

    # Rang du prochain caractères si il existe
    i = 1

    # On parcours la liste triée et pour chaque caractères, on le remplace par son rang à sa position dans la liste initiale
    for c in lt:
        l[l.index(c)] = i
        i += 1

    return l

# Fonction qui chiffre par transposition rectangulaire
# Input:
            # - key : str, la clé (un mot)
            # - msg, str, le message à chiffrer
# Output:
            # Le message chiffré par transposition réctangulaire
def chiffreTranspRect(key, msg):
    # Ordre des colonnes
    cOrder = rangCleTransRect(key)

    # Liste des caractères du message
    l = list(msg)

    # Initialisation du tableau rectangulaire avec de -1
    t = [[-1 for y in range(len(key))] for i in range(ceil(len(msg)/len(key)))]

    # Remplissage du tableau avec les caractères du msg
    for line in range(ceil(len(msg)/len(key))):
        for col in range(len(key)):
            if len(l) > 0: # Si il reste encore des caractères à mettre dans le rectangle
                t[line][col] = l.pop(0) # premier caractères de l renvoyé et supprimer de l
            else:
                break
    
    # # Affichage du rectangle
    # print(list(key))
    # print([str(i) for i in cOrder])
    # print()
    # [print(line) for line in t]

    # Liste des indices, dans le tableau de base, des colonnes dans l'ordre de transposition
    colId = [cOrder.index(i) for i in range(1, len(key)+1)]

    # Recomposition du message transposé
    res = ""

    # On parcours les colonnes dans l'ordre donné par le tableau de transposition
    for col in colId:
        for line in range(ceil(len(msg)/len(key))):
            if t[line][col] != -1:
                res += t[line][col]
    
    return res







# Fonction qui dechiffre une transposition rectangulaire
# Input:
            # - key : str, la clé (un mot)
            # - msg, str, le message à dechiffrer
# Output:
            # Le message dechiffré par transposition réctangulaire
def dechiffreTranspRect(key, msg):
    # Ordre des colonnes
    cOrder = rangCleTransRect(key)

    # Liste des caractères du message
    l = list(msg)

    # Initialisation du tableau rectangulaire avec de -1
    t = [[-1 for y in range(len(key))] for i in range(ceil(len(msg)/len(key)))]

    # Détermination de z le nb de colonnes utilisé sur la dernières ligne
    if len(msg)%len(key) != 0:
        z = len(msg)%len(key)
    else:
        z = len(key)

    # Liste des indices, dans le tableau de base, des colonnes dans l'ordre de transposition
    colId = [cOrder.index(i) for i in range(1, len(key)+1)]

    # Remplissage du rectangle par colonne en suivant l'odre de la transposition
    for col in colId:
        for line in range(ceil(len(msg)/len(key))):
            # Si on est sur une des case à remplir et qu'il reste encore des caractères à placer
            if (line != ceil(len(msg)/len(key))-1 or col <= z) and l != []:
                t[line][col] = l.pop(0)

    # # Affichage du rectangle
    # print(list(key))
    # print([str(i) for i in cOrder])
    # print()
    # [print(line) for line in t]

    
    # Recomposition du message
    res = ""
    # On parcours le tableau en suivant les lignes afin de reconstituer le msg
    for line in range(ceil(len(msg)/len(key))):
        for col in range(len(key)):
            if t[line][col] != -1:
                res += t[line][col]
    
    return res

if __name__ == "__main__":
    # Exemple de bibmath
    print(chiffreTranspRect("bibmath", "jesuisenitalieavecmarie"))

    print(dechiffreTranspRect("chat", "bunnaedrmerdeqenmiaeton"))