#coding en utf8
import tkinter
from tkinter import Label, Button


# Création de la fenêtre + paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry('640x480')
app.title('Informascience')




#Création du menu principale
menuprincipal = tkinter.Menu(app) #Barre de menu, partie principale .app > fenetre parente

# définir l'étiquette (Label)
texteLabel = "bonjour tout le monde"
etiquette = Label(menuprincipal, text = texteLabel, fg = "red")
etiquette.pack(padx = 0, pady = 0)





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
menu2.add_command(label="Longueur")


#Création de la barre de menu
#Pour que les menus se voient sur l'écran
menuprincipal.add_cascade(label="Ficher", menu=menu1)
menuprincipal.add_cascade(label="Edition", menu=menu2)


# Boucle principale
app.config(menu=menuprincipal) # lien entre mainmenu et onglet ?
app.mainloop()
