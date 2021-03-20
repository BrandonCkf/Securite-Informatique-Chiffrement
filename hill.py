# --- Programme subsidiaire ---
# Programme qui va permettre de transformer une chaine de caractère en une liste contenant chaque caracère de cette chaine.
# Et qui vérifie si le nombre de caractère de la chaine est pair ou non.
# Entrée : (string) : une chaine de caractère
# Sortie : une liste contenant tous les caractères de la chaine donnée en entrée.
def stringToPairChars(string):
    lChar = list(string)
    if len(lChar)%2!=0:
        lChar.append(" ")
    return(lChar)

# --- Programme de chiffrement de Hill ---
# Programme qui va réaliser un chiffrement de Hill sur un message à partir des entiers donnés.
# Entrées :
#   - (a) : un entier
#   - (b) : un entier
#   - (c) : un entier
#   - (d) : un entier
#   - (string) : Un message en chaine de caractère chiffré.
# Sortie : Un message chiffré.
def chiffreHill(a,b,c,d,string):
    lChar = stringToPairChars(string)
    stri = ""
    #Pour chaque bloc de deux caractères du message considéré
    for i in range(0,len(lChar),2):
        #On récupère l'indice de la table ASCII des caractères qu'on ramène dans l'intervalle [0,94]
        eun = ord(lChar[i])-32
        ede = ord(lChar[i+1])-32
        #Calcul de Y1 et Y2 qui correspond aux deux caractères chiffré. 
        yun = (a*eun+b*ede)
        yde = (c*eun+d*ede)
        #On applique le modulo 95 pour avoir le caractère chiffré dans l'alphabet considéré ([0,94])
        yunmod = (yun%95)
        ydemod = (yde%95)
        #On ramène Y1 et Y2 à l'indice correspondant dans la table ASCII
        yunmod = yunmod+32
        ydemod= ydemod+32
        #On ajoute le résultat chiffré dans la chaine de caractères finale.
        stri = stri + str(chr(yunmod)) + str(chr(ydemod))
    
    return(stri)

# --- Programme de calcul du PGCD ---
# Programme qui va réaliser le calcul du PGCD entre deux nombres.
# Entrées :
#   - (a) : un entier 
#   - (b) : un entier
# Sortie : un entier qui représente le plus grand diviseur commum entre les deux entiers
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

# --- Programme de déchiffrement de Hill ---
# Programme qui va réaliser un déchiffrement de Hill sur un message à partir des entiers donnés.
# Entrées :
#   - (a) : un entier
#   - (b) : un entier
#   - (c) : un entier
#   - (d) : un entier
#   - (string) : Un message en chaine de caractère déchiffré.
# Sortie : Un message chiffré.
def dechiffreHill(a,b,c,d,string):
    #Mise en place des variables(blocs de 2 caractères, message final, déterminant.
    lChar = stringToPairChars(string)
    stri = ""
    det = a*d-c*b
    pgcdd = pgcd(det,95)
    #On vérifie si la clé est utilisable et donc que a clé soit correcte
    if pgcdd != 1:
        return("Attention, la clé peut poser problème")
    #Si elle est corecte, on inverse la matrice
    else:
        b = -b
        c = -c
        i=1
        # Il existe un k entier tel que k*det=1+95n, et c'est ce k que nous calculons ici
        # tant que l'on ne trouve pas ce k, on incrémente de 1 notre compteur
        while (det*i)%95!=1:
            i=i+1
        #On adapte notre matrice
        ap = i*d
        b=i*b
        c=i*c
        d=i*a
        #Pour chaque bloc de deux caractères du message considéré, on calcul X1 et X2 qui seront les deux caractères déchiffrés
        for i in range(0,len(lChar),2):
            # On récupère les indices des caractères par bloc de 2 caractères
            eun = ord(lChar[i])-32
            ede = ord(lChar[i+1])-32
            #On déchiffre les caractères
            xun = ap*eun+b*ede
            xde = c*eun+d*ede
            xunm = (xun%95)+32
            xdem = (xde%95)+32
            # On ajoute les caractères déchiffrés dans le message final.
            stri = stri + str(chr(xunm)) + str(chr(xdem))
    return(stri)





    

