from hashlib import sha256
import json
import os

minuscule = "abcdefghijklmnopqrstuvwxyz"
majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre = "0123456789"
caractère_spéciaux = "!#@$%^&*"
rep = os.path.dirname((__file__))
chemin = os.path.join(rep,"mdp_liste.json")

def mdp():
    min = 0
    maj = 0
    chi = 0
    car = 0
    
    password=input("Veuillez entrer votre mot de passe : ")
    if len(password) >= 8:
        for i in password :
            if i in minuscule :
                min += 1
            elif i in majuscule :
                maj += 1
            elif i in chiffre :
                chi += 1
            elif i in caractère_spéciaux :
                car += 1
    else :
        print("Le mot de passe doit contenir au moins 8 caractères")
    if min >= 1 and maj >= 1 and chi >= 1 and car >= 1 :
        # print("Mot de passe valide")
        password = password.encode()
        cryp_password = sha256(password).hexdigest()
        # print("Le mot de passe crypté est :", cryp_password)

        if not os.path.isfile(chemin):
            open(chemin, 'w+').close()

        passwordfile = {
        "crypted_password" : cryp_password
        }
    
        with open(chemin, "r") as file :
            read_file = file.read()
            if cryp_password in read_file :
                print("Mot de passe déjà utilisé")
            else:
                with open(chemin, "a") as file :
                    json.dump(passwordfile, file, indent = 2)
                    print("Mot de passe enregistré")
    else:
        print("Le mot de passe doit contenir au moins :"+"\n"+" - une minuscule"+"\n"+" - une majuscule"+"\n"+" - un chiffre"+"\n"+" - un caractère spécial parmi (!#@$%^&*)")

mdp()

# with open(chemin, "r") as file :
#     read_file = file.read()
# print(read_file)