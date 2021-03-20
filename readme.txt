----------------------------------- PRESENTATION DU PROJET DE SECURITE INFORMATIQUE -----------------------------------


------------------------- INTRODUCTION -------------------------

Ce readme contient toutes les informations importantes pour comprendre le code et les fonctions utiles du projet.
Le projet à été réalisé par Brandon CHIEN-KAN-FOON et Stanislas CORRE.
Le langage python à été choisi car c'est un langage simple et il est facile d'implémenter dans ce langage.
Nous avons choisi les chiffrements/déchiffrements suivants : 

	- Atbash
	- César
	- Vigenère
	- Hill
	- Transposition rectangulaire
	- Delastelle

Nous avons ajouté Atbash et César car nous avions déjà travaillé sur ces méthodes de chiffrements.
Le dépôt Git contient :
	- un module pour chaque méthode de chiffrement/déchiffrement,
	- Un fichier main permet de tester les méthodes de chiffrements/déchiffrements,
	- Le fichier readme.

PLAN :

	- EXPLICATIONS ET EXEMPLES
	- FONCTIONNEMENT DU FICHIER MAIN
	- CONCLUSION

----------------------------------- EXPLICATIONS ET EXEMPLES -----------------------------------

 ------------------- Chiffrement et Déchiffrement du code Atbash ------------------- 

Fonctionnement de la fonction de chiffrement de chiffrement/déchiffrement Atbash : 

	chiffreAtbash(message)

La fonction prend en paramètre :
	
	
	- message : un message en chaine de caractère.


 --- Exemples de fonctionnement du code de chiffrement/déchiffrement Atbash --- 

Chiffrement du message : 'Enseignement de master en Securite informatique' 

Résultat du chiffrement : 

Y0+95709190*~:9~1=+*9,~90~K9;),5*9~508/,1=*5-)9




Déchiffrement du message : 'Y*59009~N=%9*~9+*~)0~.,/89++9),~:w508/,1=*5-)9~*=290*)9)&' 

Résultat du déchiffrement : 

Etienne Payet est un professeur d'informatique talentueux

------------------------------------------------------------- 




 ------------------- Chiffrement et Déchiffrement du code de César ------------------- 

Fonctionnement des fonctions de chiffrement et déchiffrement de César : 

La fonction prend en paramètre : 

    chiffreCesar(cle,message) 

    dechiffreCesar(cle,message) 

     cle : une clé en entier. 

     message : un message en chaine de caractères. 



 --- Exemples de fonctionnement du code de chiffrement/déchiffrement de César --- 

Chiffrement du message : '---Stanislas & Brandon---' 

Avec la clé : '3' 

Résultat du chiffrement : 

#000Vwdqlvodv#)#Eudqgrq000#

Déchiffrement du message : 'Qjx%x~rgtqjx%+%$%(%,%!%`%2%d%E%xj%xzn{jsy%xzw%qj%hqf{njw%&' 

Avec la clé : '5' 

Résultat du déchiffrement : 

Les symboles & ~ # ' { [ - _ @ se suivent sur le clavier !

------------------------------------------------------------- 




 ------------------- Chiffrement et Déchiffrement du code de Vigenère ------------------- 

Fonctionnement des fonctions de chiffrement et déchiffrement de Vigenère : 

    chiffreVigenere(cle,message) 
 

    dechiffreVigenere(cle,message) 
 

La fonction prend en paramètre : 

     cle : une clé en chaine de caractères. 

     message : un message en chaine de caractères. 



 --- Exemples de fonctionnement du code de chiffrement/déchiffrement de Vigenère --- 

Chiffrement du message : '!!!' 

Avec la clé : '???' 

Résultat du chiffrement : 

@@@

Déchiffrement du message : ` %&0) %~ !$/D@AB? 

Avec la clé : '20/20' 

Résultat du déchiffrement : 

Nous voulons 20/20

------------------------------------------------------------- 




 ------------------- Chiffrement et Déchiffrement de Hill ------------------- 

Fonctionnement des fonctions de chiffrement et déchiffrement de Hill : 

   chiffreHill(a,b,c,d,message) 

   dechiffreHill(a,b,c,d,message) 
 

La fonction prend en paramètre : 

     a : un entier. 

     b : un entier. 

     c : un entier. 

     d : un entier. 

     message : un message en chaine de caractères. 



 --- Exemples de fonctionnement du code de chiffrement/déchiffrement des transpositions rectangulaires --- 

Chiffrement du message : Voici certains caractères de la table ASCII : 0123 , +-*,&~@() 

Avec les entiers :  

   a = 3,   b=5,   c=2,   d=7  

Résultat du chiffrement : 

r{oM=SgO!wugohRyCGW=1P5m[gjQ Y%C'U(~1KeK9h<rnTFXVj\tWmy!bb^@eo
 
 Déchiffrement du message : k OO@?R0cU %~(|T`;80 

Avec les entiers :  

   a = 3,   b=5,   c=2,   d=7  

Résultat du déchiffrement : 

azertyuiop/*-+)@_-( 

 ------------------------------------------------------------- 




 ------------------- Chiffrement et Déchiffrement du code de Delastelle ------------------- 

Fonctionnement des fonctions de chiffrement et déchiffrement de Delastelle : 

    chiffreDelastelle(clé, longueur des fragments, message) 

    dechiffreDelastelle(clé, longueur des fragments, message) 
 

La fonction prend en paramètre : 

     cle : une clé en chaine de caractères. 

     longueur des fragments : longueur des fragments qui correspond à l'autre partie de la clé . 

     message : un message en chaine de caractères. 



 --- Exemples de fonctionnement du code de chiffrement/déchiffrement de Delastelle --- 

Chiffrement du message : 'leloupestentredanslabergerie' 

Avec la clé : 'vbkua0clxrd1mysfn2zogpi3hqewt456789j' 

Et une longueur des fragments à  : '11' 

Résultat du chiffrement : 

druetyyrgnnqqkyvtgtedxrqillrsisss

Déchiffrement du message : druetyyrgnnqqkyvtgtedxrqillrsisss 

Avec la clé : vbkua0clxrd1mysfn2zogpi3hqewt456789j 

Résultat du déchiffrement : 

leloupestentredanslabergeriexxxxx

------------------------------------------------------------- 




 ------------------- Chiffrement et Déchiffrement des Transpositions Rectangulaires ------------------- 

Fonctionnement des fonctions de chiffrement et déchiffrement des transpositions rectangulaires : 

   chiffreTranspRect(clé, message) 

   dechiffreTranspRect(clé, message) 
 

La fonction prend en paramètre : 

     cle : une clé en chaine de caractères. 

     message : un message en chaine de caractères. 



 --- Exemples de fonctionnement du code de chiffrement/déchiffrement des transpositions rectangulaires --- 

Chiffrement du message : jesuisenitalieavecmarie 

Avec la clé : bibmath 

Résultat du chiffrement : 

ilmjnaisteeereiveuacsia
 
 Déchiffrement du message : bunnaedrmerdeqenmiaeton 

Avec la clé : chat 

Résultat du déchiffrement : 

debarquementennormandie

 ------------------------------------------------------------- 





----------------------------------- FONCTIONNEMENT DU FICHIER MAIN -----------------------------------

Le fichier main permet de tester toutes les méthodes de chiffrement/déchiffrement. 

Il est intuitif et simple à comprendre.

Inscrivez le nom de la méthode de chiffrement que vous souhaitez utiliser entre ceux disponible : 
	
	1. Atbash
	2. César
	3. Vigenère
	4. Hill
	5. Delastelle
	6. Transposition Rectangulaire
	7. Stop

Si vous inscrivez le mot "Stop", vous arrêtez le programme.

Après avoir choisi la méthode de chiffrement, vous devrez inscrire les paramètres nécessaires pour que la méthode de chiffrement fonctionne. 
Après avoir inscrit ces informations, vous pouvez choisir de chiffrer ou de déchiffrer. 
Enfin, vous pouvez revenir au choix de la méthode de chiffrement à tout moment en inscrivant 'Retour'. 

 ------------------------------------------------------------- 
