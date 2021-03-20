# --- Programme de chiffrement et déchiffrement Atbash ---
# Programme qui va réaliser un chiffrement Atbash sur un message.
# Entrée : (string) : Un message en chaine de caractère.
# Sortie : Un message chiffré.
def chiffreAtbash(string):
    str = ""
    # pour chaque caractère du message à chiffrer,
    #on récupère son code ASCII et on effectue une substitution.
    for i in string:
        asc = chr(128 - 1 - ord(i) + 32 - 1)
        str = str + (asc)
    print(str)

