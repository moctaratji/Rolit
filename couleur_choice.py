#_____________Imports_____________
import fltk
#_____________Fonctions____________
def affiche_choix(nom):
    """
    Permet d'afficher les différentes options de couleurs
    :param  nom: (str) nom du joueur.

    """
    fltk.rectangle(0,0,1400,800,"white","white")
    fltk.texte(600,30,f"Choisissez votre couleur :","black","center",police="Lucida Calligraphy",taille=30)
    fltk.texte(600,90,f"joueur : {nom}","black","center",police="Lucida Calligraphy",taille=30)
    
    fltk.image(1100,150,"deux_boules.ppm",largeur=150, hauteur=150,ancrage="center")
    
    fltk.texte(2,250,"Couleurs normales(Une boule initialement placée):",ancrage="nw",police="Lucida Calligraphy",taille=10)
    
    fltk.cercle(405,250,40,"white","red")
    fltk.texte(405,350,"ROUGE","red","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(355,200,455,300,"white")
        
    fltk.cercle(555,250,40,"white","yellow")
    fltk.texte(555,350,"JAUNE","yellow","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(505,200,605,300,"white")
        
    fltk.cercle(705,250,40,"white","blue")
    fltk.texte(705,350,"BLEU","blue","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(655,200,755,300,"white")
        
    fltk.cercle(855,250,40,"white","green")
    fltk.texte(855,350,"VERT","green","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(805,200,905,300,"white")

    fltk.texte(2,450,"Couleurs spéciales(Pas de boule initialement placée):",ancrage="nw",police="Lucida Calligraphy",taille=10)
    
    fltk.cercle(405,450,40,"white","purple")
    fltk.texte(405,550,"VIOLET","purple","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(355,400,455,500,"white")
        
    fltk.cercle(555,450,40,"white","black")
    fltk.texte(555,550,"NOIR","black","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(505,400,605,500,"white")
        
    fltk.cercle(705,450,40,"white","pink")
    fltk.texte(705,550,"ROSE","pink","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(655,400,755,500,"white")
        
    fltk.cercle(855,450,40,"white","orange")
    fltk.texte(855,550,"ORANGE","orange","center",police="Lucida Calligraphy",taille=20)
    fltk.rectangle(805,400,905,500,"white")    
def choix_clic():
    """
    Permet d'afficher les différentes options de couleurs
    :return: (str) La couleur sélectionnée par le joueur.
    """
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche":
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 200<y<300:
                if 355<x<455:
                    return "red"
                if 505<x<605:
                    return "yellow"
                if 655<x<755:
                    return "blue"
                if 805<x<905:
                    return "green"
            if 400<y<500:
                if 355<x<455:
                    return "purple"
                if 505<x<605:
                    return "black"
                if 655<x<755:
                    return "pink"
                if 805<x<905:
                    return "orange"
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
      
def choix_couleur(nb,nom1,nom2,nom3,nom4):
    """
    Permet aux joueurs de faire un choix unique de leur couleur.
    : param nb: (int) nombre de joueurs .
    : param nom1: (str) nom du premier joueur.
    : param nom2: (str) nom du deuxième joueur.
    : param nom3: (str) nom du troisième joueur.
    : param nom4: (str) nom du quatrième joueur.
    :return:  un couple(str,str),triplet(str,str,str) ou un Quadruplet (str,str,str,str) de chaînes de caractères correspondant aux couleurs choisies.
    """
    if nb==2:
        lst=[]
        erreur=fltk.texte(650,150,"","red","center",taille=20)
        affiche_choix(nom1)
        choix_1=choix_clic()
        lst.append(choix_1)
        affiche_choix(nom2)
        
        while True:
            choix_2=choix_clic()
            fltk.efface(erreur)
            if choix_2 not in lst:
                fltk.efface_tout()
                return choix_1,choix_2
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20)
        
    if nb==3:
        lst=[]
        erreur=fltk.texte(650,150,"","red","center",taille=20)
        affiche_choix(nom1)
        choix_1=choix_clic()
        lst.append(choix_1)
        affiche_choix(nom2)
        while True:
            choix_2=choix_clic()
            fltk.efface(erreur)
            if choix_2 not in lst:
                lst.append(choix_2)
                break
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20)       
        affiche_choix(nom3)
        while True:
            choix_3=choix_clic()
            fltk.efface(erreur)
            if choix_3 not in lst:
                fltk.efface_tout()
                return choix_1,choix_2,choix_3
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20)        
    if nb==4:
        lst=[]
        erreur=fltk.texte(650,150,"","red","center",taille=20)
        affiche_choix(nom1)
        choix_1=choix_clic()
        lst.append(choix_1)
        affiche_choix(nom2)
        while True:
            choix_2=choix_clic()
            fltk.efface(erreur)
            if choix_2 not in lst:
                lst.append(choix_2)
                break
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20)
        affiche_choix(nom3)
        while True:
            choix_3=choix_clic()
            fltk.efface(erreur)
            if choix_3 not in lst:
                lst.append(choix_3)
                break
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20)
        affiche_choix(nom4)
        while True:
            choix_4=choix_clic()
            fltk.efface(erreur)
            if choix_4 not in lst:
                fltk.efface_tout()
                return choix_1,choix_2,choix_3,choix_4
            else:
                erreur=fltk.texte(650,150,"Cette couleur a déjà été choisie !","red","center",police="Lucida Calligraphy",taille=20) 










