#______________Imports_________________
import fltk
#______________Fonctions_______________
def revenir_en_arriere(x):
    """
    permet d'effacer le dernier caractère du nom
    """
    return x[:-1]
def affiche_clavier(nb):
    """
    Permet d'afficher le clavier
    :param  nb: (int) l'ordre des joueurs.

    """
    fltk.texte(640,40,"Entrez votre nom joueur "+str(nb)+" :",'black','center',24)
    fltk.rectangle(320,120,960,175,'black','white',2)
    fltk.rectangle(150,250,1150,550,'black','white',8)
    x_1 = 150
    x_2 = 250
    y_1 = 250
    y_2 = 350
    for i in range(3):
        for j in range(10):
            fltk.rectangle(x_1,y_1,x_2,y_2, 'black')
            x_1 += 100
            x_2 += 100
        x_1 = 150
        x_2 = 250
        y_1 += 100
        y_2 += 100
    elem_clavier=["A", "Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","Espace","-","Retour","Entrer"]
    s=0
    for i in range(0,10):
        fltk.texte(200+s,300,elem_clavier[i],'black','center',taille=21)
        s+=100
    s=0
    for i in range(10,20):
        fltk.texte(200+s,400,elem_clavier[i],'black','center',taille=21)
        s+=100
    s=0
    for i in range(20,30):
        fltk.texte(200+s,500,elem_clavier[i],'black','center',taille=21)
        s+=100

def lettre(x,y):
    """
    Permet de déterminer le caractère saisi par le joueur.
    :param  x: (int) abscisse du clic gauche.
    :param  y: (int) ordonnée du clic gauche.
    :return: (str) Le caractère saisi.
    """
    l=0
    if 250<=y<=350:
        if 150<=x<=250 :
            l="a"
            return l
        elif 250<x<=350 :
            l="z"
            return l
        elif 350<x<=450 :
            l="e"
            return l
        elif 450<x<=550 :
            l="r"
            return l
        elif 550<x<=650 :
            l="t"
            return l
        elif 650<x<=750 :
            l="y"
            return l
        elif 750<x<=850 : 
            l="u"
            return l
        elif 850<x<=950 :
            l="i"
            return l
        elif 950<x<=1050 :
            l="o"
            return l
        elif 1050<x<=1150 :
            l="p"
            return l
    elif 350<y<=450:
          if 150<x<=250 :
            l="q"
            return l
          elif 250<x<=350 :
            l="s"
            return l
          elif 350<x<=450 :
            l="d"
            return l
          elif 450<x<=550 :
            l="f"
            return l
          elif 550<x<=650 :
            l="g"
            return l
          elif 650<x<=750 :
            l="h"
            return l
          elif 750<x<=850 : 
            l="j"
            return l
          elif 850<x<=950 :
            l="k"
            return l
          elif 950<x<=1050 :
            l="l"
            return l
          elif 1050<x<=1150 :
            l="m"
            return l
       
    elif 450<y<=550:
          if 150<=x<=250 :
            l="w"
            return l
          elif 250<x<=350 :
            l="x"
            return l
          elif 350<x<=450 :
            l="c"
            return l
          elif 450<x<=550 :
            l="v"
            return l
          elif 550<x<=650 :
            l="b"
            return l
          elif 650<x<=750 :
            l="n"
            return l
          elif 750<x<=850 : 
            l=" "
            return l
          elif 850<x<=950 :
            l="-"
            return l
          elif 950<x<=1050 :
            l="'"
            return l
          elif 1050<x<=1150 :
            l="Entrer"
            return l
   
def saisie_nom(nb):
    """
    Permet de saisir un nom
    :param  nb: (int) l'ordre des joueurs.

    """
    name=""
    affiche_clavier(nb)
    fltk.texte(330,128,'Nom : ','black','nw',tag='name')
    Erreur=fltk.texte(530,128,'','red','nw')
    var=True
    while var:
        touche=fltk.attend_ev()
        fltk.efface(Erreur)
        if fltk.type_ev(touche)=="Quitte":
            fltk.ferme_fenetre()
        if (fltk.type_ev(touche)=="ClicGauche"):
            x,y=fltk.abscisse(touche), fltk.ordonnee(touche)
            if 950<x<1050 and 450<y<550:
                name=revenir_en_arriere(name)
                fltk.efface("name")
                fltk.texte(330,128,f'Nom : {name}','black','nw',tag='name')
            elif 150<x<1150 and 250<y<550:
                l=lettre(x,y)
                if lettre(x,y)=="Entrer":
                    if len(name)>10:
                       fltk.efface("name")
                       Erreur=fltk.texte(350,128,'Nombre de caractères supérieur à 10 ','red','nw',tag='name')
                    else:
                        fltk.efface_tout()
                        return name
                elif lettre(x,y) != "Entrer":
                    name+=lettre(x,y)
                    fltk.efface("name")
                    fltk.texte(330,128,f'Nom : {name}','black','nw',tag='name')
    
def affiche_clavier_numérique():
    """
    Permet d'afficher le clavier numérique.
    """
    fltk.texte(640,40,"Entrez le nombre de manches: ",'black','center',24)
    fltk.rectangle(320,120,960,175,'black','white',2)
    fltk.rectangle(500,200,800,600,'black','white',8)
    x_1 = 500
    x_2 = 600
    y_1 = 200
    y_2 = 300
    for i in range(4):
        for j in range(3):
            fltk.rectangle(x_1,y_1,x_2,y_2, 'black')
            x_1 += 100
            x_2 += 100
        x_1 = 500
        x_2 = 600
        y_1 +=100
        y_2 +=100
    lst_element=["1","2","3","4","5","6","7","8","9","0","Entrer","Retour"]
    j=0
    for i in range(0,3):
        fltk.texte(550+j,250,lst_element[i],'black','center',taille=21)
        j+=100
    j=0
    for i in range(3,6):
        fltk.texte(550+j,350,lst_element[i],'black','center',taille=21)
        j+=100
    j=0
    for i in range(6,9):
        fltk.texte(550+j,450,lst_element[i],'black','center',taille=21)
        j+=100
    j=0
    for i in range(9,12):
        fltk.texte(550+j,550,lst_element[i],'black','center',taille=21)
        j+=100

def chiffre(x,y):
    """
    Permet de déterminer le caractère saisi par le joueur.
    :param  x: (int) abscisse du clic gauche.
    :param  y: (int) ordonnée du clic gauche.
    :return: (str) Le caractère saisi.
    """
    l=0
    if 200<=y<=300:
        if 500<=x<=600 :
            l="1"
            return l
        elif 600<x<=700 :
            l="2"
            return l
        elif 700<x<=800 :
            l="3"
            return l
    if 300<y<=400:
          if 500<=x<=600 :
            l="4"
            return l
          elif 600<x<=700 :
            l="5"
            return l
          elif 700<x<=800 :
            l="6"
            return l
    if 400<y<=500:
          if 500<=x<=600 :
            l="7"
            return l
          elif 600<x<=700 :
            l="8"
            return l
          elif 700<x<=800 :
            l="9"
            return l
    if 500<y<=600:
          if 500<=x<=600 :
            l="0"
            return l
          elif 600<x<=700 :
            l="Entrer"
            return l        
          elif 700<x<=800 :
            l="10"
            return l
def saisie_nombre():
    """
    Permet de saisir un nombre
    """
    nombre=""
    affiche_clavier_numérique()
    fltk.texte(330,128,'Nombre : ','black','nw',tag='nombre')
    Erreur=fltk.texte(370,128,'','red','nw',tag='nombre')
    var=True
    while var:
        touche=fltk.attend_ev()
        fltk.efface(Erreur)
        if fltk.type_ev(touche)=="Quitte":
            fltk.ferme_fenetre()
        if (fltk.type_ev(touche)=="ClicGauche"):
            x,y=fltk.abscisse(touche), fltk.ordonnee(touche)
            if 700<x<800 and 500<y<600:
                nombre=revenir_en_arriere(nombre)
                fltk.efface("nombre")
                fltk.texte(330,128,f'Nombre : {nombre}','black','nw',tag='nombre')
            elif 500<x<800 and 200<y<600:
                l=chiffre(x,y)
                if chiffre(x,y)=="Entrer":
                    if nombre== "0" or nombre== "":
                        Erreur=fltk.texte(570,128,'Erreur','red','nw',tag='nombre')
                    else:
                        fltk.efface_tout()
                        return int(nombre)
                elif chiffre(x,y) != "Entrer":
                    nombre+=chiffre(x,y)
                    fltk.efface("nombre")
                    fltk.texte(330,128,f'Nombre : {nombre}','black','nw',tag='nombre')
  
