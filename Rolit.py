########################################################################
#                                                                      #
#  Développeurs: Moctar,Youssef et Romain             Janvier 2025     #
#                                                                      #
#                                                                      #
#                             jeu_Rolit                                #
#                                                                      #
#                                                                      #
########################################################################

#_______________Imports_______________
import random
import fltk
import couleur_choice
import clavier
import json
#_____________Constantes______________
LARG = 1200
HAUT = 640
#_____________Fonctions_______________
def initialiser_plateau():
    """
    la fonction initialiser_plateau permet d'initialiser le plateau de jeu avec les 4 boules initiales au centre.
    :return: le plateau initiale
    """
    global plateau
    plateau=[[" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "]]
    plateau[4][3]= "blue"
    plateau[3][4]= "yellow"
    plateau[3][3]= "red"       
    plateau[4][4]= "green"
    return plateau

def pix_vers_cel(x, y,taille_cel, x_offset, y_offset) :
    """
    La fonction calcule les références de la cellule dans laquelle le point (x, y) se situe.
    Les bords Ouest et Nord appartiennent à la cellule.
    : param x: (int) abscisse du clic gauche de la souris  .
    : param y: (int) une liste de bidules dont on décrit la composition.
    : param taille_cel: (int) taille d'une cellule en pixels
    : param x_offset: (int) décalage, en pixels, par rapport au bord gauche de la fenêtre
    : param y_offset: (int) décalage, en pixels, par rapport au bord supérieur de la fenêtre
    :return: (int,int)  un tuple d’entiers correspondant aux références de la cellule.
    """
    col = (x- x_offset)//taille_cel
    li = (y- y_offset)//taille_cel
    return li, col

def cel_vers_pix(li, col, taille_cel, x_offset, y_offset) :
    """
    la fonction Calcule les coordonnées en pixels du centre de la cellule référencée (li,col).
    : param li: (int) numéro de ligne de la cellule  .
    : param col: (int) numéro de colonne de la cellule.
    : param taille_cel: (int) taille d'une cellule en pixels
    : param x_offset: (int) décalage, en pixels, par rapport au bord gauche de la fenêtre
    : param y_offset: (int) décalage, en pixels, par rapport au bord supérieur de la fenêtre
    :return: (int,int) un tuple d’entiers correspondant aux coordonnées en pixels du centre de la cellule.
    """
    xc = (x_offset) + (col + 0.5)*(taille_cel)
    yc = (y_offset) + (li + 0.5)*(taille_cel)
    return xc,yc

def adjacente(x,y):
    """
    la fonction vérifie si la boule que le joueur souhaite placer est adjacente à une autre.
    : param x: (int) numéro de ligne de la boule placer.
    : param y: (int) numéro de colonne de la boule placer.
    :return: (bool) True si la boule est adjacente à une autre, False si c'est pas le cas .
    """
    directions = [
        (-1, 0), (1, 0),  
        (0, -1), (0, 1),  
        (-1, -1), (-1, 1),  
        (1, -1), (1, 1)]   
    for dx,dy in directions:
        sx, sy = x + dx, y + dy
        if 0<=sx<=7 and 0<=sy<=7 and plateau[sx][sy] != ' ':
            return True
    return False

def capture(x, y, couleur):
    """
    La fonction permet de capturer les boules pouvant l’être après que le joueur ai posé sa boule.
    : param x: (int) numéro de ligne de la boule placer.
    : param y: (int) numéro de colonne de la boule placer.
    : param couleur: (str) couleur du joueur.
    """
    directions_possibles = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for du, dv in directions_possibles:
        boules_capturer = []
        dx, dy = x + du, y + dv
        while (0 <= dx <=7 ) and (0 <= dy <= 7) and plateau[dx][dy] != " " and plateau[dx][dy] != couleur:
            boules_capturer.append((dx, dy))
            dx, dy = dx + du, dy + dv
        if  (0 <= dx <= 7) and (0 <= dy <= 7) and plateau[dx][dy] == couleur:
            for (bx, by) in boules_capturer:
                plateau[bx][by] = couleur
def transforme():
    """
    La fonction permet de placer les boules sur le plateau graphique en fonction du plateau de base.
    """
    for i in range(8):
        for b in range(8):
            xc,yc=cel_vers_pix(i,b,75,25,25)
            if plateau[i][b] == 'blue' :
                fltk.cercle(xc,yc,35,'blue',"blue")
            if plateau[i][b] == 'red' :
                fltk.cercle(xc,yc,35,'red',"red")
            if plateau[i][b] == 'yellow' :
                fltk.cercle(xc,yc,35,'yellow',"yellow")
            if plateau[i][b] == 'green' :
                fltk.cercle(xc,yc,35,'green',"green")
            if plateau[i][b] == 'pink' :
                fltk.cercle(xc,yc,35,'pink',"pink")
            if plateau[i][b] == 'black' :
                fltk.cercle(xc,yc,35,'black',"black")
            if plateau[i][b] == 'orange' :
                fltk.cercle(xc,yc,35,'orange',"orange")
            if plateau[i][b] == 'purple' :
                fltk.cercle(xc,yc,35,'purple',"purple")
def plateau_graphique():
    """
    La fonction permet d’afficher le plateau graphique ainsi que les différents menus liés à la partie.
    """
    fltk.rectangle(25,25,625,625,'black','white',6)
    x_1 = 25
    x_2 = 100
    y_1 = 25
    y_2 = 100
    for i in range(8):
        for j in range(8):
            fltk.rectangle(x_1,y_1,x_2,y_2, 'black',epaisseur=2)
            x_1 += 75
            x_2 += 75
        x_1 = 25
        x_2 = 100
        y_1 += 75
        y_2 += 75
    fltk.rectangle(945,280,1156,320,"black",epaisseur=2)
    fltk.texte(860,300,"Message:","black","center",police="Lucida Calligraphy",taille=15)
    fltk.rectangle(770,70,830,130,"white",epaisseur=4)
    fltk.image(800,100,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.rectangle(870,70,930,130,"white",epaisseur=4)
    fltk.image(900,100,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.rectangle(940,70,1165,130,"blue",epaisseur=2)
    fltk.texte(960,85,"Sauvegarder", police="Lucida Calligraphy",taille=20)
    transforme()

def placer(joueur):
    """
    La fonction permet de positionner la boule du joueur tout en respectant les règles du jeu et en prenant en compte les éventuels clics.
    : param joueur: (dict) dictionnaire du joueur contenant ses informations.
    :return: (str) "forfait" si le joueur décide de passer à la manche suivante.
    """
    plateau_graphique()
    var=True
    texte=fltk.texte(1100,300,"","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
    texte1=fltk.texte(1100,300,"","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
    texte2=fltk.texte(1100,300,"","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
    while var :
        evenement_placer= fltk.attend_ev()
        fltk.efface("erreur")
        if fltk.type_ev(evenement_placer)=="ClicGauche":
            a,b= fltk.abscisse(evenement_placer),fltk.ordonnee(evenement_placer)
            e,f= pix_vers_cel(a,b,75,25,25)
            if  870<a<930 and 70<b<130:
                fltk.rectangle(420,170,780,490,"white","white",tag="forfait")
                fltk.rectangle(420,170,780,490,"red","white",8,tag="forfait")
                fltk.texte(600,290,"Voulez-vous","black","center",police="Lucida Calligraphy",taille=15,tag="forfait")
                fltk.texte(600,320,"retourner au menu ?","black","center",police="Lucida Calligraphy",taille=15,tag="forfait")
                fltk.rectangle(650,380,710,440,"white",tag="forfait")
                fltk.rectangle(490,380,550,440,"white",tag="forfait")
                fltk.image(680,410,"oui.ppm",largeur=45, hauteur=45,ancrage="center",tag="forfait")
                fltk.image(520,410,"non.ppm",largeur=45, hauteur=50,ancrage="center",tag="forfait")
                variable=True
                while variable:
                    evenement_placer= fltk.attend_ev()
                    if fltk.type_ev(evenement_placer)=="ClicGauche":
                        a,b= fltk.abscisse(evenement_placer),fltk.ordonnee(evenement_placer)
                        if 650<a<710 and 380<b<440:
                            fltk.efface("forfait")
                            var = False
                            variable=False
                            menu()
                        if 490<a<550 and 380<b<440:
                            fltk.efface("forfait")
                            variable=False
            if not(0<=e<=7 and 0<=f<=7):
                texte= fltk.texte(1050,300,"boule en dehors","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
            if 0<=e<=7 and 0<=f<=7:
                if (plateau[e][f] != " ") :
                    texte1=fltk.texte(1050,300,"case occupée","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
                elif adjacente(e,f)==False :
                    texte2= fltk.texte(1050,300,"boule pas adjacente","red","center",police="Lucida Calligraphy",taille=15,tag="erreur")
                else:
                    plateau[e][f]=joueur["couleur"]
                    cx,cy=cel_vers_pix(e,f,75,25,25)
                    fltk.cercle(cx,cy,35,couleur=joueur["couleur"],remplissage=joueur["couleur"])
                    fltk.mise_a_jour()
                    capture(e,f,joueur["couleur"])
                    break
            if 940<a<1156 and 70<b<130:
                sauvegarder_etat_jeu(joueurs, plateau, manche_actuel, nb_manches, nom_fichier="sauvegarde.json")
                fltk.rectangle(420,170,780,490,"white","white",tag="indication")
                fltk.rectangle(420,170,780,490,"red","white",8,tag="indication")
                fltk.texte(600,290,"Partie sauvegardée avec","black","center",police="Lucida Calligraphy",taille=19,tag="indication")
                fltk.texte(600,340,"succès","black","center",police="Lucida Calligraphy",taille=19,tag="indication")
                fltk.attend_ev()
                fltk.efface("indication")
            if 770<a<830 and 70<b<130:
                fltk.rectangle(420,170,780,490,"white","white",tag="forfait")
                fltk.rectangle(420,170,780,490,"red","white",8,tag="forfait")
                fltk.texte(600,270,"Voulez-vous","black","center",police="Lucida Calligraphy",taille=15,tag="forfait")
                fltk.texte(600,300,"arrêter la manche","black","center",police="Lucida Calligraphy",taille=15,tag="forfait")            
                fltk.texte(600,330,"et passer à la suivante ?","black","center",police="Lucida Calligraphy",taille=15,tag="forfait")
                fltk.rectangle(650,380,710,440,"white",tag="forfait")
                fltk.rectangle(490,380,550,440,"white",tag="forfait")
                fltk.image(680,410,"oui.ppm",largeur=45, hauteur=45,ancrage="center",tag="forfait")
                fltk.image(520,410,"non.ppm",largeur=45, hauteur=50,ancrage="center",tag="forfait")
                variable=True
                while variable:
                    evenement_placer= fltk.attend_ev()
                    if fltk.type_ev(evenement_placer)=="ClicGauche":
                        a,b= fltk.abscisse(evenement_placer),fltk.ordonnee(evenement_placer)
                        if 650<a<710 and 380<b<440:
                            fltk.efface("forfait")
                            var = False
                            variable=False
                            return"forfait"
                        if 490<a<550 and 380<b<440:
                            fltk.efface("forfait")
                            variable=False                
        if fltk.type_ev(evenement_placer)=="Quitte":
            fltk.ferme_fenetre()

def case_disponible(lst):
    """
    La fonction permet de déterminer s'il reste des cases libres sur le plateau.
    : param lst: (list) plateaau de jeu .
    :return: (bool) True s'il reste des cases libres, et False dans le cas contraire.
    """
    for elem in lst:
        for case in elem:
            if case ==" ":
                return True
    return False

def score(couleur):
    """
    La fonction permet de connaître le nombre d'apparitions de la boule du joueur sur le plateau.
    :param couleur: (str) la couleur du joueur.
    :return:(int) le nombre de boules du joueur dans le plateau.
    """
    score=0
    for lst in plateau:
        for case in lst:
            if case==couleur:
                score=score+1
    return score

def determine_gagnant_manche(Nbre_joueurs,joueurs):
    """
    Permet de déterminer le gagnant d'une manche en fonction des points obtenus par les joueurs.
    :param   Nbre_joueurs: (int) Nombre de joueurs participant à la manche.
    :param   joueurs: (dico) dictionnaire contenant le dictionnaire de chaque joueur.
    :return: (str) Le nom du joueur gagnant la manche ou "egalite" en cas d'égalité.
    """
    v="egalite"
    if Nbre_joueurs==2:
        x=score(joueurs["joueur_A"]["couleur"])
        y=score(joueurs["joueur_B"]["couleur"])
        if x>y:
            return joueurs["joueur_A"]["nom"]
        elif x<y:
            return joueurs["joueur_B"]["nom"]
        else:
            return v
    elif Nbre_joueurs == 3:
        x = score(joueurs["joueur_A"]["couleur"])
        y = score(joueurs["joueur_B"]["couleur"])
        z = score(joueurs["joueur_C"]["couleur"])

        max_score = max(x, y, z)
        joueurs_max = []
        if x == max_score:
            joueurs_max.append(joueurs["joueur_A"]["nom"])
        if y == max_score:
            joueurs_max.append(joueurs["joueur_B"]["nom"])
        if z == max_score:
            joueurs_max.append(joueurs["joueur_C"]["nom"])

        if len(joueurs_max) == 1:
            return joueurs_max[0]
        else:
           return v
        
    elif Nbre_joueurs == 4:
        x = score(joueurs["joueur_A"]["couleur"])
        y = score(joueurs["joueur_B"]["couleur"])
        z = score(joueurs["joueur_C"]["couleur"])
        w = score(joueurs["joueur_D"]["couleur"])

        max_score = max(x, y, z, w)
        joueurs_max = []
        if x == max_score:
            joueurs_max.append(joueurs["joueur_A"]["nom"])
        if y == max_score:
            joueurs_max.append(joueurs["joueur_B"]["nom"])
        if z == max_score:
            joueurs_max.append(joueurs["joueur_C"]["nom"])
        if w == max_score:
            joueurs_max.append(joueurs["joueur_D"]["nom"])

        if len(joueurs_max) == 1:
            return joueurs_max[0]
        else:
           return v
        
def manche(Nbre,joueurs):
    """
    Permet de gérer une manche entière et de gérer l'affichage des scores de la manche.
    :param   Nbre: (int) Nombre de joueurs participant à la manche
    :param   joueurs: (dico) dictionnaire contenant les dictionnaires de chaque joueur.
    """
    if Nbre==2:
        ordre_2_joueurs=random.randint(0,1)
        if ordre_2_joueurs==0:
            joueur1=joueurs["joueur_A"]
            joueur2=joueurs["joueur_B"]
        else:
            joueur1=joueurs["joueur_B"]
            joueur2=joueurs["joueur_A"]
        
        fltk.rectangle(0,0,1200,640,'White','white')
        fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        while case_disponible(plateau)==True:

            fltk.texte(950,200,"Tour : "+joueur1["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.cercle(1150,200,8,joueur1["couleur"],joueur1["couleur"],epaisseur=15,tag="tour1")
            coup_1=placer(joueur1)
            if coup_1=="forfait":
                break
            fltk.efface("tour1")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")

            fltk.texte(950,200,"Tour : "+joueur2["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour2")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour2")
            fltk.cercle(1150,200,8,joueur2["couleur"],joueur2["couleur"],epaisseur=15,tag="tour2")
            coup_2=placer(joueur2)
            if coup_2=="forfait":
                break
            fltk.efface("tour2")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            
        fltk.efface_tout()
        joueur1["points_total"]+=score(joueur1["couleur"])
        joueur2["points_total"]+=score(joueur2["couleur"])
        fltk.texte(600,270,"score de "+joueur1["nom"]+": "+str(score(joueur1["couleur"]))+" pts",couleur=joueur1["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,330,"score de "+joueur2["nom"]+": "+str(score(joueur2["couleur"]))+" pts",couleur=joueur2["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        gagnant_manche=determine_gagnant_manche(Nbre,joueurs)
        if gagnant_manche==joueur1["nom"]:
            joueur1["manches_gagnées"]+=1
            fltk.texte(600,400,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur2["nom"]:
            joueur2["manches_gagnées"]+=1
            fltk.texte(600,400,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if  gagnant_manche =="egalite":
            fltk.texte(600,400,"il y a une égalité",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        continuer()
            
    if Nbre==3:
        
        ordre_3_joueur=random.randint(0,2)
        if ordre_3_joueur==0:
            joueur1=joueurs["joueur_A"]
            joueur2=joueurs["joueur_B"]
            joueur3=joueurs["joueur_C"]
        if ordre_3_joueur==1:
            joueur1=joueurs["joueur_B"]
            joueur2=joueurs["joueur_C"]
            joueur3=joueurs["joueur_A"]
        if ordre_3_joueur==2:
            joueur1=joueurs["joueur_C"]
            joueur2=joueurs["joueur_A"]
            joueur3=joueurs["joueur_B"]
        fltk.rectangle(0,0,1200,640,'White','white')
        fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        while case_disponible(plateau)==True:

            fltk.texte(950,200,"Tour : "+joueur1["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.cercle(1150,200,8,joueur1["couleur"],joueur1["couleur"],epaisseur=15,tag="tour1")
            coup_1=placer(joueur1)
            if coup_1=="forfait":
                break
            fltk.efface("tour1")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")

            fltk.texte(950,200,"Tour : "+joueur2["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour2")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour2")
            fltk.cercle(1150,200,8,joueur2["couleur"],joueur2["couleur"],epaisseur=15,tag="tour2")
            coup_2=placer(joueur2)
            if coup_2=="forfait":
                break
            fltk.efface("tour2")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")

            fltk.texte(950,200,"Tour : "+joueur3["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour3")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour3")
            fltk.cercle(1150,200,8,joueur3["couleur"],joueur3["couleur"],epaisseur=15,tag="tour3")
            coup_3=placer(joueur3)
            if coup_3=="forfait":
                break
            fltk.efface("tour3")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            
        fltk.efface_tout()
        joueur1["points_total"]+=score(joueur1["couleur"])
        joueur2["points_total"]+=score(joueur2["couleur"])
        joueur3["points_total"]+=score(joueur3["couleur"])
        fltk.texte(600,250,"score de "+joueur1["nom"]+": "+str(score(joueur1["couleur"]))+" pts",couleur=joueur1["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,310,"score de "+joueur2["nom"]+": "+str(score(joueur2["couleur"]))+" pts",couleur=joueur2["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,370,"score de "+joueur3["nom"]+": "+str(score(joueur3["couleur"]))+" pts",couleur=joueur3["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        gagnant_manche=determine_gagnant_manche(Nbre,joueurs)
        if gagnant_manche==joueur1["nom"]:
            joueur1["manches_gagnées"]+=1
            fltk.texte(600,440,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur2["nom"]:
            joueur2["manches_gagnées"]+=1
            fltk.texte(600,440,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur3["nom"]:
            joueur3["manches_gagnées"]+=1
            fltk.texte(600,440,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if  gagnant_manche =="egalite":
            fltk.texte(600,440,"il y a une égalité",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        continuer()
            
    if Nbre==4:
        
        ordre_4_joueur=random.randint(0,3)
        if ordre_4_joueur==0:
            joueur1=joueurs["joueur_A"]
            joueur2=joueurs["joueur_B"]
            joueur3=joueurs["joueur_C"]
            joueur4=joueurs["joueur_D"]
        if ordre_4_joueur==1:
            joueur1=joueurs["joueur_B"]
            joueur2=joueurs["joueur_C"]
            joueur3=joueurs["joueur_D"]
            joueur4=joueurs["joueur_A"]
        if ordre_4_joueur==2:
            joueur1=joueurs["joueur_C"]
            joueur2=joueurs["joueur_D"]
            joueur3=joueurs["joueur_A"]
            joueur4=joueurs["joueur_B"]
        if ordre_4_joueur==3:
            joueur1=joueurs["joueur_D"]
            joueur2=joueurs["joueur_A"]
            joueur3=joueurs["joueur_B"]
            joueur4=joueurs["joueur_C"]
        fltk.rectangle(0,0,1200,640,'White','white')
        fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        fltk.texte(922,600,joueur4["nom"]+" : "+str(score(joueur4["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        while case_disponible(plateau)==True:

            fltk.texte(950,200,"Tour : "+joueur1["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour1")
            fltk.cercle(1150,200,8,joueur1["couleur"],joueur1["couleur"],epaisseur=15,tag="tour1")
            coup_1=placer(joueur1)
            if coup_1=="forfait":
                break
            fltk.efface("tour1")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,600,joueur4["nom"]+" : "+str(score(joueur4["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        
            

            fltk.texte(950,200,"Tour : "+joueur2["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour2")
            fltk.texte(1100,200,"Boule : ","black","center",taille=15,police="Lucida Calligraphy",tag="tour2")
            fltk.cercle(1150,200,8,joueur2["couleur"],joueur2["couleur"],epaisseur=15,tag="tour2")
            coup_2=placer(joueur2)
            if coup_2=="forfait":
                break
            fltk.efface("tour2")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,600,joueur4["nom"]+" : "+str(score(joueur4["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        

            fltk.texte(950,200,"Tour : "+joueur3["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour3")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour3")
            fltk.cercle(1150,200,8,joueur3["couleur"],joueur3["couleur"],epaisseur=15,tag="tour3")
            coup_3=placer(joueur3)
            if coup_3=="forfait":
                break
            fltk.efface("tour3")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,600,joueur4["nom"]+" : "+str(score(joueur4["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        

            fltk.texte(950,200,"Tour : "+joueur4["nom"],"black","center",police="Lucida Calligraphy",taille=15,tag="tour4")
            fltk.texte(1100,200,"Boule : ","black","center",police="Lucida Calligraphy",taille=15,tag="tour4")
            fltk.cercle(1150,200,8,joueur4["couleur"],joueur4["couleur"],epaisseur=15,tag="tour4")
            coup_4=placer(joueur4)
            if coup_4=="forfait":
                break
            fltk.efface("tour4")
            fltk.efface("points")
            fltk.texte(922,450,joueur1["nom"]+" : "+str(score(joueur1["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,500,joueur2["nom"]+" : "+str(score(joueur2["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,550,joueur3["nom"]+" : "+str(score(joueur3["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
            fltk.texte(922,600,joueur4["nom"]+" : "+str(score(joueur4["couleur"]))+" pts","black","center",police="Lucida Calligraphy",taille=15,tag="points")
        
            
        fltk.efface_tout()
        joueur1["points_total"]+=score(joueur1["couleur"])
        joueur2["points_total"]+=score(joueur2["couleur"])
        joueur3["points_total"]+=score(joueur3["couleur"])
        joueur4["points_total"]+=score(joueur1["couleur"])
        fltk.texte(600,210,"score de "+joueur1["nom"]+": "+str(score(joueur1["couleur"]))+" pts",couleur=joueur1["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,270,"score de "+joueur2["nom"]+": "+str(score(joueur2["couleur"]))+" pts",couleur=joueur2["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,330,"score de "+joueur3["nom"]+": "+str(score(joueur3["couleur"]))+" pts",couleur=joueur3["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        fltk.texte(600,390,"score de "+joueur4["nom"]+": "+str(score(joueur4["couleur"]))+" pts",couleur=joueur4["couleur"],ancrage='center',police="Lucida Calligraphy",taille=20)
        gagnant_manche=determine_gagnant_manche(Nbre,joueurs)
        if gagnant_manche==joueur1["nom"]:
            joueur1["manches_gagnées"]+=1
            fltk.texte(600,460,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur2["nom"]:
            joueur2["manches_gagnées"]+=1
            fltk.texte(600,460,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur3["nom"]:
            joueur3["manches_gagnées"]+=1
            fltk.texte(600,460,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if gagnant_manche==joueur4["nom"]:
            joueur4["manches_gagnées"]+=1
            fltk.texte(600,460,"Le gagnant de la manche est :"+gagnant_manche,couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        if  gagnant_manche =="egalite":
            fltk.texte(600,460,"il y a une égalité",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=20)
        continuer()

def premiere_page_regle():
    """
    Permet d'afficher la première page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.image(600,320,'règle_0.ppm',largeur=750, hauteur=421, ancrage='center')
    fltk.image(1000,350,'règle_1.ppm',largeur=150, hauteur=150, ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                deuxieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def deuxieme_page_regle():
    """
    Permet d'afficher la deuxième page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,280,'règle_2.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                troisieme_page_regle()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                premiere_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def troisieme_page_regle():
    """
    Permet d'afficher la troisième page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,280,'règle_3.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                quatrieme_page_regle()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                deuxieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def quatrieme_page_regle():
    """
    Permet d'afficher la quatrième page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,280,'règle_4.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                cinquieme_page_regle()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                troisieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def cinquieme_page_regle():
    """
    Permet d'afficher la cinquième page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,150,'règle_5.ppm',ancrage='center')
    fltk.image(600,440,'règle_6.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                sixieme_page_regle()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                quatrieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def sixieme_page_regle():
    """
    Permet d'afficher la sixième page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(640,570,700,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,280,'règle_7.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(670,602,'droite.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 640<x<700 and 570<y<630:
                fltk.efface_tout()
                septieme_page_regle()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                cinquieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
def septieme_page_regle():
    """
    Permet d'afficher la septieme page des règles.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.rectangle(500,570,560,630,"white",epaisseur=4)
    fltk.image(600,280,'règle_8.ppm',ancrage='center')
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    fltk.image(530,602,'gauche.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
            if 500<x<560 and 570<y<630:
                fltk.efface_tout()
                sixieme_page_regle()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()    

def menu():
    """
    Permet d'afficher le menu du jeu.
    """
    fltk.rectangle(0,0,1400,800,"white","white")
    fltk.image(600,350,'image_principale.ppm',largeur=750, hauteur=421, ancrage='center')
    fltk.texte(600,50,"Le jeu qui va vous faire perdre la boule !",couleur="black",ancrage='center',police="Lucida Calligraphy",taille= 20)
    fltk.rectangle(35,310,225,370,"lightblue","lightblue",epaisseur=4)
    fltk.rectangle(35,310,225,370,"black",epaisseur=4)
    fltk.texte(130,340,"Partie sauvegardée",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=13)
    fltk.rectangle(35,410,225,470,"lightblue","lightblue",epaisseur=4)
    fltk.rectangle(35,410,225,470,"black",epaisseur=4)
    fltk.texte(130,440,"Règles",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=13)
    fltk.rectangle(35,210,225,270,"lightblue","lightblue",epaisseur=4)
    fltk.rectangle(35,210,225,270,"black",epaisseur=4)
    fltk.texte(130,240,"Nouvelle partie",couleur="black",ancrage='center',police="Lucida Calligraphy",taille=13)
    partie_lancee = False
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        
        if typeEv == "ClicGauche":
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            
            if not partie_lancee and 35 < x < 225 and 210 < y < 270:
                fltk.efface_tout()
                jeu()  
                partie_lancee = True  
                
            if not partie_lancee and 35 < x < 225 and 310 < y < 370:
                fltk.efface_tout()
                reprendre_partie_sauvegardee()
                partie_lancee = True  
                
            if not partie_lancee and 35 < x < 225 and 410 < y < 470:
                fltk.efface_tout()
                premiere_page_regle()  

        if typeEv == "Quitte":
            fltk.ferme_fenetre()

def continuer():
    """
    Permet de continuer une partie après l'affichage des scores de la manche.
    """
    fltk.rectangle(530,580,675,620,"green")
    fltk.texte(600,600,"Continuer",couleur="green",ancrage='center',police="Lucida Calligraphy",taille=20)
    var=True
    while var:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x,y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 530<x<675 and 580<y<620:
                fltk.efface_tout()
                #fltk.mise_a_jour()
                var=False
def retour_au_menu():
    """
    Permet de revenir au menu du jeu.
    """
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    var=True
    while var:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x,y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 570<x<630 and 570<y<630:    
                fltk.efface_tout()
                menu()
        if typeEv == "Quitte":
            fltk.ferme_fenetre()    
def choix_nombre_joueurs():
    """
    Permet de choisir le nombre de joueurs souhaitant participer.
    """
    fltk.rectangle(0,0,1200,640,"white","white",epaisseur=4)
    fltk.texte(600,80,"Choix du nombre de joueurs",couleur="purple",ancrage='center',police="Lucida Calligraphy",taille=20)
    fltk.rectangle(220,425,380,475,"green")
    fltk.rectangle(520,425,680,475,"green")
    fltk.rectangle(820,425,990,475,"green")
    fltk.texte(301,443,"2 joueurs",couleur="green",ancrage='center',police="Lucida Calligraphy",taille=15)
    fltk.texte(601,443,"3 joueurs",couleur="green",ancrage='center',police="Lucida Calligraphy",taille=15)
    fltk.texte(906,443,"4 joueurs",couleur="green",ancrage='center',police="Lucida Calligraphy",taille=15)
    fltk.image(301,325,'2_pions.ppm',largeur=150, hauteur=150, ancrage='center')
    fltk.image(601,325,'3_pions.ppm',largeur=150, hauteur=150, ancrage='center')
    fltk.image(906,325,'4_pions.ppm',largeur=150, hauteur=150, ancrage='center')
    fltk.rectangle(570,570,630,630,"white",epaisseur=4)
    fltk.image(600,600,'menu.ppm',largeur=50, hauteur=50, ancrage='center')
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if 220<x<380 and 425<y<475:
                fltk.efface_tout()
                return 2           
            if 520<x<680 and 425<y<475:
                fltk.efface_tout()
                return 3
            if 820<x<990 and 425<y<475:
                fltk.efface_tout()
                return 4
            if 570<x<630 and 570<y<630:
                menu()
        if typeEv=="Quitte":
            fltk.ferme_fenetre()
#fonction pour savoir le gagnant de la partie
def determine_gagnant(Nbre,joueurs):
    """
    Permet de déterminer le gagnant final du jeu en fonction des manches jouées et des points accumulés par les joueurs.
    :param   Nbre: (int) Nombre de joueurs participant au jeu.
    :param   joueurs: (dico) dictionnaire contenant le dictionnaire de chaque joueur.
    :return: (str) Le nom du joueur gagnant la partie.
    """
    if Nbre==2:
        if joueurs["joueur_A"]["manches_gagnées"]>joueurs["joueur_B"]["manches_gagnées"]:
            return joueurs["joueur_A"]["nom"]
        elif joueurs["joueur_B"]["manches_gagnées"]>joueurs["joueur_A"]["manches_gagnées"]:
            return joueurs["joueur_B"]["nom"]
        else:
            if joueurs["joueur_A"]["points_total"]>joueurs["joueur_B"]["points_total"]:
                return joueurs["joueur_A"]["nom"]
            elif joueurs["joueur_B"]["points_total"]>joueurs["joueur_A"]["points_total"]:
                return joueurs["joueur_B"]["nom"]
            else:
                return random.choice([joueurs["joueur_A"]["nom"],joueurs["joueur_B"]["nom"]])
    elif Nbre== 3:
        lst =[joueurs["joueur_A"].get("manches_gagnées"),
            joueurs["joueur_B"].get("manches_gagnées"),
            joueurs["joueur_C"].get("manches_gagnées")]
        valeur_max = max(lst)
        count_max = lst.count(valeur_max)

        if count_max == 1:
            if lst[0] == valeur_max:
                return joueurs["joueur_A"]["nom"]
            elif lst[1] == valeur_max:
                return joueurs["joueur_B"]["nom"]
            else:
                return joueurs["joueur_C"]["nom"]
        else:
            occurences = []
            if lst[0] == valeur_max:
                occurences.append(joueurs["joueur_A"])
            if lst[1] == valeur_max:
                occurences.append(joueurs["joueur_B"])
            if lst[2] == valeur_max:
                occurences.append(joueurs["joueur_C"])
            max_points = 0
            for joueur in occurences:
                 if joueur["points_total"] > max_points:
                     max_points = joueur["points_total"]
                     
            joueur_max=[] 
            for joueur in occurences:
                if joueur["points_total"] == max_points:
                   joueur_max.append(joueur)
                   
            occurences=joueur_max
            if len(joueur_max)==1:
                return joueur_max[0]["nom"]
            else:
                noms_candidats = [] 
            for joueur in occurences:
                noms_candidats.append(joueur["nom"])  

            return random.choice(noms_candidats)
    elif Nbre == 4:
        lst = [joueurs["joueur_A"].get("manches_gagnées"),
               joueurs["joueur_B"].get("manches_gagnées"),
               joueurs["joueur_C"].get("manches_gagnées"),
               joueurs["joueur_D"].get("manches_gagnées")]

        valeur_max = max(lst)
        count_max = lst.count(valeur_max)

        if count_max == 1:
            if lst[0] == valeur_max:
                return joueurs["joueur_A"]["nom"]
            elif lst[1] == valeur_max:
                return joueurs["joueur_B"]["nom"]
            elif lst[2] == valeur_max:
                return joueurs["joueur_C"]["nom"]
            else:
                return joueurs["joueur_D"]["nom"]
        else:
            occurences = []
            if lst[0] == valeur_max:
                occurences.append(joueurs["joueur_A"])
            if lst[1] == valeur_max:
                occurences.append(joueurs["joueur_B"])
            if lst[2] == valeur_max:
                occurences.append(joueurs["joueur_C"])
            if lst[3] == valeur_max:
                occurences.append(joueurs["joueur_D"])
            max_points = 0
            for joueur in occurences:
                if joueur["points_total"] > max_points:
                    max_points = joueur["points_total"]
            
            joueur_max = [] 
            for joueur in occurences:
                if joueur["points_total"] == max_points:
                    joueur_max.append(joueur)
            
            occurences = joueur_max
            if len(joueur_max) == 1:
                return joueur_max[0]["nom"]
            else:
                noms_candidats = [] 
                for joueur in occurences:
                    noms_candidats.append(joueur["nom"])
                return random.choice(noms_candidats)    
def jeu():
    """
    Permet de recueillir les informations de chaque joueur, de répéter une manche en fonction du nombre de manches choisi,
    et de gérer l'affichage des scores finaux.
    """    
    global nb_manches
    global manche_actuel  
    Nbre_joueurs = choix_nombre_joueurs()
    nb_manches = clavier.saisie_nombre()
    global joueurs
    joueurs = {}
    
    if Nbre_joueurs == 2:
        nom_A = clavier.saisie_nom(1)
        nom_B = clavier.saisie_nom(2)
        couleur_A, couleur_B = couleur_choice.choix_couleur(2, nom_A, nom_B, "", "")
        joueurs["joueur_A"] = {"nom": nom_A, "couleur": couleur_A, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_B"] = {"nom": nom_B, "couleur": couleur_B, "manches_gagnées": 0, "points_total": 0}
    
    elif Nbre_joueurs == 3:
        nom_A = clavier.saisie_nom(1)
        nom_B = clavier.saisie_nom(2)
        nom_C = clavier.saisie_nom(3)
        couleur_A, couleur_B, couleur_C = couleur_choice.choix_couleur(3, nom_A, nom_B, nom_C, "")
        joueurs["joueur_A"] = {"nom": nom_A, "couleur": couleur_A, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_B"] = {"nom": nom_B, "couleur": couleur_B, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_C"] = {"nom": nom_C, "couleur": couleur_C, "manches_gagnées": 0, "points_total": 0}
    
    elif Nbre_joueurs == 4:
        nom_A = clavier.saisie_nom(1)
        nom_B = clavier.saisie_nom(2)
        nom_C = clavier.saisie_nom(3)
        nom_D = clavier.saisie_nom(4)
        couleur_A, couleur_B, couleur_C, couleur_D = couleur_choice.choix_couleur(4, nom_A, nom_B, nom_C, nom_D)
        joueurs["joueur_A"] = {"nom": nom_A, "couleur": couleur_A, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_B"] = {"nom": nom_B, "couleur": couleur_B, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_C"] = {"nom": nom_C, "couleur": couleur_C, "manches_gagnées": 0, "points_total": 0}
        joueurs["joueur_D"] = {"nom": nom_D, "couleur": couleur_D, "manches_gagnées": 0, "points_total": 0}
    
    
    manche_actuel = 1  

    for manches in range(1, nb_manches + 1):
        
        plateau = initialiser_plateau()
        
        manche(Nbre_joueurs, joueurs)

        manche_actuel += 1  

    fltk.rectangle(0, 0, 1200, 640, "white", "white")
    
    if Nbre_joueurs == 2:
        fltk.texte(600, 300, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    elif Nbre_joueurs == 3:
        fltk.texte(600, 240, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 300, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_C"]["nom"] + " a gagné " + str(joueurs["joueur_C"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_C"]["points_total"]) + " points au total", couleur=joueurs["joueur_C"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    elif Nbre_joueurs == 4:
        fltk.texte(600, 180, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 240, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 300, joueurs["joueur_C"]["nom"] + " a gagné " + str(joueurs["joueur_C"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_C"]["points_total"]) + " points au total", couleur=joueurs["joueur_C"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_D"]["nom"] + " a gagné " + str(joueurs["joueur_D"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_D"]["points_total"]) + " points au total", couleur=joueurs["joueur_D"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    gagnant_final = determine_gagnant(Nbre_joueurs, joueurs)
    fltk.texte(600, 430, "Le gagnant de cette partie est: " + gagnant_final + " 🏆", ancrage='center', police="Lucida Calligraphy", taille=15)
    retour_au_menu()
    
def sauvegarder_etat_jeu(joueurs, plateau, manche_actuel, nb_manches, nom_fichier="sauvegarde.json"):
    """
    Permet de sauvegarder les joueurs, le plateau, le nombre de manches, ainsi que la manche en cours au moment de la sauvegarde.
    :parm joueurs:(dict) Dictionnaire ou est stokée les données des joueurs.
    :parm plateau:(list) C'est la liste de liste qui permet de savoir ou son les boules et de quel couleur elles sont.
    :parm nb_manche:(int) C'est une valeur qui égal au nombre total de manche.
    :parm manche_actuel:(int) C'est une valeur qui permet de savoir a quel manche on est exactement.
    :parm nom nom_fichier="sauvegarde.json": (str) C'est se qui nomme le fichier quand sa vas le crée ou le remplacer.
    """
    etat_jeu = {"joueurs": joueurs, "plateau": plateau,"manche_actuel":manche_actuel,"nb_manches":nb_manches}
    
    with open(nom_fichier, "w") as fichier:
        json.dump(etat_jeu, fichier)

def charger_etat_jeu(nom_fichier="sauvegarde.json"):
    """
    fonction qui permet de charger les information sauvegarder

    :parm nom_fichier="sauvegarde.json": Sa sert a préciser de quel fichier on veut charger le contenue
    :return: le dictionnaire contenant l'information des joueurs(dict),le plateau(list) ,le nombre de manche actuelle(int) et le nombre de manches au total(int).
    ou sinon retourne un dictionnaire vide(dict) et trois None.
    """
    try:
        with open(nom_fichier, "r") as fichier:
            etat_jeu = json.load(fichier)
            return etat_jeu["joueurs"], etat_jeu["plateau"], etat_jeu["manche_actuel"], etat_jeu["nb_manches"]
    except FileNotFoundError:
        return {}, None, None, None 

def reprendre_partie_sauvegardee():
    """
    fonction qui permet de retracer le plateau sauvegarder et de jouer dans la partie sauvegarder en suivant la logique de la fonction jeu.
    """
    global joueurs
    global plateau
    global manche_actuel
    global nb_manches
    joueurs, plateau_sauvegarde, manche_actuel, nb_manches = charger_etat_jeu()
    
    if not joueurs:  
        jeu()
        return
    
    plateau = plateau_sauvegarde
    Nbre_joueurs = len(joueurs)
    manche_actuel_sauvegarde = manche_actuel
    while manche_actuel <= nb_manches:
        
        if manche_actuel > manche_actuel_sauvegarde :
            plateau = initialiser_plateau()  
        
        manche(Nbre_joueurs, joueurs)
        
        manche_actuel += 1
    
    fltk.rectangle(0, 0, 1200, 640, "white", "white")
    
    if Nbre_joueurs == 2:
        fltk.texte(600, 300, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    elif Nbre_joueurs == 3:
        fltk.texte(600, 240, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 300, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_C"]["nom"] + " a gagné " + str(joueurs["joueur_C"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_C"]["points_total"]) + " points au total", couleur=joueurs["joueur_C"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    elif Nbre_joueurs == 4:
        fltk.texte(600, 180, joueurs["joueur_A"]["nom"] + " a gagné " + str(joueurs["joueur_A"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_A"]["points_total"]) + " points au total", couleur=joueurs["joueur_A"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 240, joueurs["joueur_B"]["nom"] + " a gagné " + str(joueurs["joueur_B"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_B"]["points_total"]) + " points au total", couleur=joueurs["joueur_B"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 300, joueurs["joueur_C"]["nom"] + " a gagné " + str(joueurs["joueur_C"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_C"]["points_total"]) + " points au total", couleur=joueurs["joueur_C"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
        fltk.texte(600, 360, joueurs["joueur_D"]["nom"] + " a gagné " + str(joueurs["joueur_D"]["manches_gagnées"]) + " manches" + " et obtenu " + str(joueurs["joueur_D"]["points_total"]) + " points au total", couleur=joueurs["joueur_D"]["couleur"], ancrage='center', police="Lucida Calligraphy", taille=15)
    
    gagnant_final = determine_gagnant(Nbre_joueurs, joueurs)
    fltk.texte(600, 430, "Le gagnant de cette partie est: " + gagnant_final + " 🏆", ancrage='center', police="Lucida Calligraphy", taille=15)
    retour_au_menu()
#_______________Programme principal__________________
    
if __name__ == '__main__':
    
    plateau = [[" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "]]
    plateau[4][3] = "blue"
    plateau[3][4] = "yellow"
    plateau[3][3] = "red"       
    plateau[4][4] = "green"
    fltk.cree_fenetre(LARG,HAUT)
    menu()   











        

 