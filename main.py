# --- Importation des modules pour chaque code de chiffrement ---
from atbash import *
from delastelle import *
from transRect import *
from cesar import *
from vigenere import *
from hill import *



fl = True
flHill = True
ret = "Retour"
stop = "Stop"
un = "Atbash"
de = "César"
tr = "Vigenère"
qu = "Hill"
ci = "Delastelle"
si = "Transposition Rectangulaire"
chi = "Chiffrer"
dech = "Déchiffrer"
oui = "Oui"
non = "Non"
while fl:
    print(" Méthodes de chiffrement disponibles: \n 1. 'Atbash' \n 2. 'César' \n 3. 'Vigenère' \n 4. 'Hill' \n 5. 'Delastelle' \n6. 'Transposition Rectangulaire' \n 7. 'Stop' \n")
    choix = input("Quelle méthode de chiffrement voulez-vous utiliser (Inscrivez le nom de la méthode) ?   ")
    print("\n    Vous avez choisi : "+choix)
    if choix == un:
        #Atbash
        message = input("Inscrivez le message à chiffrer/déchiffrer ou inscrivez 'Retour' pour choisir une méthode de chiffrement :   ")
        while message != ret:
            print(" \n Résultat du chiffrement/déchiffrement d'Atbash avec le message : "+ message)
            print("\n")
            chiffreAtbash(message)
            message = ret
    elif choix == de:
    #César
        message = input("Inscrivez le message à chiffrer/déchiffrer ou 'Retour' pour choisir la méthode de chiffrement :   ")
        if message != ret:
            cle = int(input("Inscrivez l'entier qui consituera la clé de chiffrement ou '0' pour choisir une méthode de chiffrement :   "))
            if cle != 0 :
                type_chiffre = input("Inscrivez 'Chiffrer' pour chiffrer le message, 'Déchiffrer' pour le déchiffrer ou 'Retour' pour choisir une méthode de chiffrement ?   ")
                if type_chiffre == chi:
                    print(" \n Résultat du chiffrement de César avec le message : "+ message + " \n et la clé : "+str(cle))
                    print("\n")
                    print(chiffreCesar(cle, message))
                elif type_chiffre == dech:
                    print(" \n Résultat du déchiffrement d'abash avec le message : "+ message)
                    print("\n")
                    print(dechiffreCesar(cle, message))
                else:
                    print("Retour \n")
    elif choix == tr:
    #Vigenère
        message = input("Inscrivez le message à chiffrer/déchiffrer ou 'Retour' pour choisir la méthode de chiffrement :   ")
        if message != ret:
            cle = input("Inscrivez les caractères qui consitueront la clé de chiffrement ou 'Retour' pour choisir la méthode de chiffrement :   ")
            if cle != ret :
                type_chiffre = input("Inscrivez 'Chiffrer' pour chiffrer le message, 'Déchiffrer' pour le déchiffrer ou 'Retour' pour choisir une méthode de chiffrement ?   ")
                if type_chiffre == chi:
                    print(" \n Résultat du chiffrement de Vigenère avec le message : "+ message + " \n et la clé : "+cle)
                    print("\n")
                    print(chiffreVigenere(cle, message))
                elif type_chiffre == dech:
                    print(" \n Résultat du déchiffrement de Vigenère avec le message : "+ message + " \n et la clé : "+cle)
                    print("\n")
                    print(dechiffreVigenere(cle, message))
                else:
                    print("Retour \n")
    elif choix == qu:
        flHill = True
        while flHill :
            
            #Hill
            message = input("Inscrivez le message à chiffrer/déchiffrer ou 'Retour' pour choisir la méthode de chiffrement :   ")
            if message != ret:
                a = int(input("\n Inscrivez l'entier a de la matrice :   "))
                b = int(input(" Inscrivez l'entier b de la matrice :   "))
                c = int(input(" Inscrivez l'entier c de la matrice :   "))
                d = int(input(" Inscrivez l'entier d de la matrice :   "))
                print("\n")
                det = a*d-b*c
                detP = pgcd(det,95)
                if detP == 1:
                    type_chiffre = input(" Inscrivez 'Chiffrer' pour chiffrer le message, 'Déchiffrer' pour le déchiffrer ou 'Retour' pour choisir une méthode de chiffrement ?   ")
                    if type_chiffre != ret:
                        if type_chiffre == chi:
                            print(" \n Résultat du chiffrement de Hill avec le message : "+ message + " \n et les entiers : \n ")
                            print("a : "+str(a))
                            print("\n")
                            print("b : "+str(b))
                            print("\n")
                            print("c : "+str(c))
                            print("\n")
                            print("d : "+str(d))
                            print("\n \n")
                            print(chiffreHill(a,b,c,d,message))
                        elif type_chiffre == dech:
                            print(" \n Résultat du déchiffrement de Hill avec le message : "+ message + " \n et les entiers : \n ")
                            print("a : "+str(a))
                            print("\n")
                            print("b : "+str(b))
                            print("\n")
                            print("c : "+str(c))
                            print("\n")
                            print("d : "+str(d))
                            print("\n \n")
                            print(dechiffreHill(a,b,c,d,message))
                        else:
                            print("Retour \n")
                else:
                    print("\n Attention, la clé posera problème pour le déchiffrement car le déterminant de la matrice n'est pas inversible dans Z/95Z !!! \n")
                    hillAg = input("Voulez-vous tenter une autre matrice ('Oui'/'Non') ? ")
                    print("")
                    if hillAg == non:
                        flHill = False
                        
    elif choix == ci:
        #Delastelle
        message = input("Inscrivez le message à chiffrer/déchiffrer ou 'Retour' pour choisir la méthode de chiffrement :   ")
        if message != ret:
            cle = input("Inscrivez les caractères qui consitueront la clé de chiffrement ou 'Retour' pour choisir la méthode de chiffrement :   ")
            if cle != ret:
                fragments = int(input("Choisissez un entier qui constituera la longueur des fragments :   "))
                if fragments%2==0:
                    print(" \n il faut que la longueur des fragments soit impair !! \n")
                    fragments = 0
                
                if fragments != 0:
                    type_chiffre = input("Inscrivez 'Chiffrer' pour chiffrer le message, 'Déchiffrer' pour le déchiffrer ou 'Retour' pour choisir une méthode de chiffrement ?   ")
                    if type_chiffre == chi:
                        print(" \n Résultat du chiffrement de Delastelle avec le message : "+ message + " \n la clé : "+cle+"\n et la longueur des fragments à : "+str(fragments))
                        print("\n")
                        print(chiffreDelastelle(cle,fragments,message))
                    elif type_chiffre == dech:
                        print(" \n Résultat du déchiffrement de Delastelle avec le message : "+ message + " \n la clé : "+cle+"\n et la longueur des fragments à : "+str(fragments))
                        print("\n")
                        print(dechiffreDelastelle(cle,fragments,message))
                    else:
                        print("Retour \n")
    elif choix == si:
        #Transp. Rect.
        message = input("Inscrivez le message à chiffrer/déchiffrer ou 'Retour' pour choisir la méthode de chiffrement :   ")
        if message != ret:
            cle = input("Inscrivez les caractères qui consitueront la clé de chiffrement ou 'Retour' pour choisir la méthode de chiffrement :   ")
            if cle != ret:
                type_chiffre = input("Inscrivez 'Chiffrer' pour chiffrer le message, 'Déchiffrer' pour le déchiffrer ou 'Retour' pour choisir une méthode de chiffrement ?   ")
                if type_chiffre == chi:
                    print(" \n Résultat du chiffrement de la Transposition Rectangulaire avec le message : "+ message + " \n et la clé : "+cle+"\n")
                    print("\n")
                    print(chiffreTranspRect(cle,message))
                elif type_chiffre == dech:
                    print(" \n Résultat du déchiffrement de Delastelle avec le message : "+ message + " \n et la clé : "+cle+"\n")
                    print("\n")
                    print(dechiffreTranspRect(cle,message))
                else:
                    print("Retour \n")
    elif choix == stop:
        fl=False
        print("\n    Aurevoir !!!")
    else :
        print("Inscrivez une méthode de chiffrement correcte !!! \n")
        
    print("\n ------------------------------------------------------- ")
    
        
