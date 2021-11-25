# afficher la liste des films
print("Bienvenue au cinéma")


# Creer une liste de films
#films = ["FF - FlingingFilm", "Conjuring", "Arcane"]

# Creer un dictionnaire 
# différence entre liste=[] et dictionnaire={}
#Liste cest un stockage d'une valeur et on connait son rang
# Dictionnaire on associe plusieurs valeurs
films = [
    {# Film 1
    "Titre": "FF - FlingingFilm", # Dès qu'on appelle Titre, il va nous envoyer FF - FlingingFilm
    "Horaire": "18h05",
    "Places": 130
    },
    
     { # Film 2
      "Titre": "Arcane",
      "Horaire": "13h05",
      "Places": 230
      },
    
     {
    "Titre": "Oui Le Film",
    "Horaire": "21h05",
    "Places": 0
    }
    
]

# Pour afficher "FF - FlingingFilm" on doit appeler Titre dans film donc:
# afficher chaque film
for numero, Liste in enumerate(films, start=1): #la boucle va parcourir toute la liste, pour pas faire print(film1), print(film2)
    #print("Film n°", numero, "nom:",  Liste['Titre'], " Horaire de la séance:", Liste['Horaire'])
# Pour chaque "x" , "y" dans [(compte de 1 à n les :) FILM], affiche (les numéros de la List:films, les caractères de la liste films)
   
 # Une autre manière de faire le  print IL FAUT LE METTRE SOUS LA BOUCLE FOR
    Titre = Liste['Titre']  
    Horaire = Liste['Horaire']
    Places = Liste['Places']
    
    # Il faut ajouter le "f" pour que ça marche
    print(f"Film n°{numero}: {Titre} - Horaire: {Horaire} - Places {Places} ")
    
 
 
print("Quel film voulez-vous voir aujourd'hui ? Indiquez le numéro du film svp")   
# Demander à l'utilisateur d'entrer un film à voir  
# Permet à l'utilisateur de rentrer un valeur  et après il faut la récuprer
#Par défaut input() c'est un text donc il faut le tranformer pourt que ca soit un nombre entier
choix = int(input())
print("Vous avez choisi le film numéro", choix, films[choix - 1]['Titre'])
    # Choix - 1 psk enumerate commence à 0
    
    
#nb_places = numéro du choix du film par l'utilisateur DANS la liste "films" et on veut l'argument "Places"
nb_places = films[choix - 1]['Places']
print(nb_places)


# Vérifier si c'est pas complet
if nb_places > 0:
    print("Achat effectué")
    films[choix - 1]['Places'] -= 1
else:
    print("Séance complète :(")




 
 
#coding en utf8
import tkinter
from tkinter import Label, Button


# Création de la fenêtre + paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry('640x480')
app.title('Informascience')




#Création du menu principale
menuprincipal = tkinter.Menu(app) #Barre de menu, partie principale .app > fenetre parente





#Création du menu 1 sous le menu principale
menu1 = tkinter.Menu(menuprincipal, tearoff=0) #Premier menu
#Ajout des commande dans le menu 1
menu1.add_command(label="Nouveau")
menu1.add_command(label="Nouvelle fenêtre")
menu1.add_command(label="Quitter", command=app.quit)

#Création du menu 2 sous le menu principale 
menu2 = tkinter.Menu(menuprincipal, tearoff=0) #deuxieme menu
#Ajout des commandes danas le menu 2
menu2.add_command(label="Editer")
menu2.add_command(label="Raccourcir")
menu2.add_command(label="Longugfcghfceur")


#Création de la barre de menu
#Pour que les menus se voient sur l'écran
menuprincipal.add_cascade(label="Ficher", menu=menu1)
menuprincipal.add_cascade(label="Edition", menu=menu2)

###########################################################################
# Boucle principale
#app.config(menu=menuprincipal) # lien entre mainmenu et onglet ?
#app.mainloop()
##########################################################################