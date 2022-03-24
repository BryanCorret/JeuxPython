"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module equipement.py
    ce module gère le plateau des joueurs  équipements ordinateurs et serveurs
"""
import matrice
import case
import equipement
import trojan
import protection
import joueur

# direction de déplacement possible pour l'avatar
DIRECTIONS_AVATAR = {'DD', 'GG', 'HH', 'BB', 'HD', 'HG', 'BD', 'BG'}

# A AJOUTER DANS VOTRE FICHIER
# points par action
PENALITE = -5
TROJAN_ELIMINE = 10
TROJAN_PIEGE = 5
DEPLACEMENT_TROJAN = 1
EQUIPEMENT_TOUCHE = -15
CONT_PROTECTION = 0
# FIN AJOUT

def creer_plateau(id_joueur, nom_joueur, taille_plateau=5, resistance_serveur=40,
                  resistance_pc=50, nb_points=0):
    """créer un nouveau plateau

    Args:
        id_joueur (int): l'identifiant du joueur à qui appartient le plateau
        nom_joueur (str): le nom du joueur à qui appartient le plateau
        taille_plateau (int, optional): la taille du plateau. Defaults to 5.
        resistance_serveur (int, optional): la resistance initiale du serveur. Defaults to 4.
        resistance_pc (int, optional): la resistance initiale des PC. Defaults to 5.
        nb_points (int,optional): le nombre de points du joueur. Defaults to 0.
    Returns:
        dict: un plateau tel que décrit dans le sujet
    """
    plateau = dict()
    plateau["joueur"] = joueur.creer_joueur(id_joueur, nom_joueur,nb_points)
    plateau["serveur"] = equipement.creer_equipement(equipement.SERVEUR, resistance_serveur)
    plateau["ordinateur"]=equipement.creer_equipement(equipement.ORDINATEUR, resistance_pc)
    plateau["matrice"] = matrice.creer_matrice(taille_plateau,taille_plateau,None)
    plateau["entrants"] = []
    plateau["sortants"] = []

    for ligne in range(matrice.get_nb_lignes(plateau["matrice"])):
        for col in range(matrice.get_nb_colonnes(plateau["matrice"])):
            if ligne == 2 and col == 2:
                matrice.set_val(plateau["matrice"],ligne, col,case.creer_case("",None,plateau["serveur"],[]))
                poser_avatar(plateau, ligne , col)
            elif (ligne == 0 and col == 2) or (ligne == 1 and col == 2) or (ligne == 4 and col == 2) :
                matrice.set_val(plateau["matrice"], ligne, col, case.creer_case('B',None,None,[]))
            elif (ligne == 2 and col == 1 )  :
                matrice.set_val(plateau["matrice"], ligne, col, case.creer_case('D',None,None,[]))
            elif (ligne == 2 and col == 3 ) :
                matrice.set_val(plateau["matrice"], ligne, col, case.creer_case('G',None,None,[]))
            elif (ligne == 3 and col == 2 ) :
                matrice.set_val(plateau["matrice"], ligne, col, case.creer_case('H',None,None,[]))
            else :
                matrice.set_val(plateau["matrice"], ligne, col, case.creer_case(None,None,None,[]))
    return plateau

def get_id_joueur(plateau):
    """retourne l'identifiant du joueur à qui appartient le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        int: l'identifiant du joueur
    """
    return plateau["joueur"]["Identifiant"]


def get_nom_joueur(plateau):
    """retourne le nom du joueur à qui appartient le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        str: le nom du joueur
    """
    return plateau["joueur"]["Nom"]


def get_trojans_entrants(plateau):
    """retourne la liste des trojans arrivants sur le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        list: la liste des trojans arrivants sur le plateau
    """
    return plateau["entrants"]

def get_trojans_sortants(plateau, direction):
    """retourne la liste des trojans sortants du plateau pour la destination direction

    Args:
        plateau (dict): un plateau
        direction (str): une des quatre directions H, B, D, G

    Returns:
        list: la liste des trojans sortants du plateau vers la direction indiquée
    """
    return plateau["sortants"]


def get_taille(plateau):
    """retourne la taille de la matrice du plateau

    Args:
        plateau (dict): un plateau

    Returns:
        int: la taille du plateau
    """
    return plateau["matrice"]["lignes"]


def get_case(plateau, ligne, colonne):
    """retourne la case qui se trouve en ligne,colonne sur le plateau

    Args:
        plateau (dict): un plateau
        ligne (int): le numéro de la ligne
        colonne (int): le numéro de la colonne

    Returns:
        dict: une case
    """
    return matrice.get_val(plateau["matrice"],ligne,colonne)


def get_points(plateau):
    """retourne le nombre de points de joueur à qui appartient le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        int: le nombre de points du joueur
    """
    return plateau["joueur"]["Nombre de points"]


def get_nb_ordis_restants(plateau):
    """indique combien il reste d'ordinateurs sur le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        int: le nombre d'ordinateurs restants
    """
    return equipement.get_resistance(plateau["ordinateur"])//10 



def get_resistance_serveur(plateau):
    """indique combien de resistance il reste au serveur

    Args:
        plateau (dict): un plateau

    Returns:
        int: le niveau de resistance restant au serveur
    """
    return equipement.get_resistance(plateau["serveur"])


def get_serveur(plateau):
    """retourne le serveur du plateau

    Args:
        plateau (dict): un plateau

    Returns:
        dict: un équipement de type serveur
    """
    return plateau["serveur"]


def get_pos_avatar(plateau):
    """retourne la position de l'avatar sur le plateau

    Args:
        plateau (dict): un plateau

    Returns:
        (int,int): la ligne et la colonne où se trouve l'avatar sur le plateau
    """
    for x in range(matrice.get_nb_lignes(plateau['matrice'])): # ligne
        for y in range(matrice.get_nb_colonnes(plateau["matrice"])): # colonne
              if case.contient_avatar(get_case(plateau,x,y)):
                return (x,y)
    return None

def get_ordis(plateau):
    """retourne les ordinateurs du plateau

    Args:
        plateau (dict): un plateau

    Returns:
        dict: un équipement de type ordinateurs
    """
    return plateau["ordinateur"]


def get_matrice(plateau):
    """retourne la matrice associée au plateau

    Args:
        plateau (dict): un plateau

    Returns:
        dict: une matrice
    """
    return plateau["matrice"]


def poser_avatar(plateau, ligne, colonne):
    """pose l'avatar sur la case en ligne,colonne

    Args:
        plateau (dict): un plateau
        ligne (int): le numéro de la ligne
        colonne (int): le numéro de la colonne
    """
    case.poser_avatar(get_case(plateau,ligne,colonne))


def poser_protection(plateau, type_protection, ligne, colonne):
    """pose une protection sur le plateau avec les règles suivantes:
        1. aucune autre protection n'est sur le plateau
        2. la protection n'a pas été détruite
        3. aucun trojan ne se trouve sur la case où on mets la protection
        4. la ligne et la colonne existent
      La fonction retourne True si la pose der
        type_protection (int): le type de la protection à mettre
        ligne (int): le numéro de la ligne
        colonne (int): le numéro de la colonne

    Returns:
        bool: True si la pose s'est bien passée et False sinon
    """

    la_case = get_case(plateau,ligne,colonne)
    taille = get_taille(plateau)
    cont_protec = 0
    if ligne > taille or colonne > taille:
        return False
    
    # VErifie si il n'y a pas de protection sur le plateau
    for x in range(matrice.get_nb_lignes(plateau['matrice'])): # ligne
        for y in range(matrice.get_nb_colonnes(plateau["matrice"])): # colonne
            la_case2 = get_case(plateau,x,y) 
            contient_protection = case.get_protection(la_case2)
            if contient_protection != None :
                cont_protec = 1
                break


    if la_case["protection"] != None or la_case["serveur"] != None or la_case["presents"] != [] or la_case["avatar"] != False or cont_protec == 1:
        return False
    else :
        la_protection = protection.creer_protection(type_protection, protection.RESISTANCE)
        case.set_protection(get_case(plateau,ligne,colonne),la_protection)
        return True
            
def set_trojans_entrants(plateau, les_trojans):
    """Met les trojans entrants sur le plateau

    Args:
        plateau (dict): un plateau
        les_trojans (list): une liste de trojans
    """
    if type(les_trojans) == dict:
        plateau["entrants"] = [les_trojans]
    else:
        plateau["entrants"] = les_trojans

def set_trojans_sortants(plateau, direction, les_trojans):
    """mets les trojans devant sortir vers la direction indiquée

    Args:
        plateau (dict): un plateau
        direction (str): une des directions H, B, D, G
        les_trojans (list): une liste de trojans
    """
    for trojan in les_trojans:
        if type(trojan) == str:
            les_trojans["Direction"] = direction
            plateau["sortants"].append(les_trojans)
            break
        elif type(trojan) == dict:
            trojan["Direction"] = direction
            plateau["sortants"].append(trojan)

# FIN DES FONCTIONS NECESSAIRES POUR LA SAUVEGARDE/RESTAURATION D'UN PLATEAU

def id_joueur_droite(plateau):
    """retourne l'identifiant du joueur de droite

    Args:
        plateau (dict): un plateau

    Returns:
        int: l'identifiant du joueur de droite
    """
    id_droite = plateau["joueur"]["Identifiant"] + 1
    if id_droite > 4:
        id_droite = id_droite - 4 
    return id_droite


def id_joueur_gauche(plateau):
    """retourne l'identifiant du joueur de gauche

    Args:
        plateau (dict): un plateau

    Returns:
        int: l'identifiant du joueur de gauche
    """
    id_gauche = plateau["joueur"]["Identifiant"] + 3
    if id_gauche > 4:
        id_gauche = id_gauche - 4 
    return id_gauche


def id_joueur_haut(plateau):
    """retourne l'identifiant du joueur du haut

    Args:
        plateau (dict): un plateau

    Returns:
        int: l'identifiant du joueur du haut
    """
    id_haut = plateau["joueur"]["Identifiant"] + 2
    if id_haut > 4:
        id_haut = id_haut - 4 
    return id_haut


def ajouter_points(plateau, nb_points):
    """ajoute le nombre de point nb_points au joueur du plateau

    Args:
        plateau (dict): un plateau
        nb_points (int): le nombre de points (éventuellement négatif)

    Returns:
        int: le nombre de points total du joueur du plateau
    """
    plateau["joueur"]["Nombre de points"] = nb_points
    return plateau["joueur"]["Nombre de points"]

def ajouter_trojan(plateau, liste_trojan):
    """ajoute une liste de nouveaux trojan à la liste des trojan qui vont entrer
       sur le plateau lors du prochain tour

    Args:
        plateau (dict): un plateau
        liste_trojan (list): la liste des trojans à ajouter
    """
    plateau["entrants"].append(liste_trojan)
    


def attaquer_ordinateurs(plateau):
    """enlève une resistance aux ordinateurs du plateau

    Args:
        plateau (dict): un plateau

    Returns:
        int: le nombre d'ordinateurs restants
    """
    plateau["ordinateur"]["Résistance"] -= 1
    return plateau["ordinateur"] 


def a_perdu(plateau):
    """indique si le joueur de ce plateau a perdu

    Args:
        plateau (dict): un plateau

    Returns:
        bool: True si le plateau est perdant et False sinon
    """
    if plateau["ordinateur"] == None and plateau["serveurs"] == None:
        return True
    return False


def deplacer_avatar(plateau, direction):
    """déplace l'avatar dans une des directions 'DD', 'GG', 'HH', 'BB', 'HD', 'HG', 'BD', 'BG'
       Le joueur sera pénalisé de 5 points si l'avatar ne peut pas se déplacer
       dans la direction indiquée et il gagnera 5 points par trojans détruits

    Args:
        plateau (dict): un plateau
        direction (str): la direction vers où se déplace l'avatar
    """
    DICO_DIR = {(-1, -1): 'HG', (-1, 0): 'HH', (-1, 1): 'HD', (0, -1): 'GG',
            (0, 1): 'DD', (1, -1): 'BG', (1, 0): 'BB', (1, 1): 'BD'}
    #trouver l'avatar
    coord = get_pos_avatar(plateau)
    for cle, direction_dict in DICO_DIR.items(): #cle = tuple
        if direction == direction_dict:
            new_coord = (coord[0]+cle[0],coord[1]+cle[1])
            if (new_coord[0] >= 0 and new_coord[1] >= 0) or (new_coord[0] <= 4  and new_coord[1] <= 4 ):
                poser_avatar(plateau, new_coord[0], new_coord[1])
                case.enlever_avatar(get_case(plateau,coord[0],coord[1]))

                if len(case.get_trojans(get_case(plateau,new_coord[0],new_coord[1]))) > 0:
                    plateau["joueur"]["Nombre de points"] += 5*len(case.get_trojans(get_case(plateau,new_coord[0],new_coord[1])))
            else:
                 plateau["joueur"]["Nombre de points"] -= 5


def preparer_trojan(plateau, destinataire, type_t):
    """creer un nouveau trojan appartenant au joueur du plateau, à destination d'un des voisins
        et avec un type défini

    Args:
        plateau (dict): un plateau
        destinataire (str): une des direction D, G ou H
        type (int): un nombre entre 0 et taille-1
    """
    trojan_dest = trojan.creer_trojan(plateau["joueur"]["Identifiant"],type_t,destinataire)
    if destinataire == "H":
        joueur_dest = joueur.id_joueur_haut(plateau["joueur"]["Identifiant"])
    elif  destinataire == "D":
        joueur_dest = joueur.id_joueur_droite(plateau["joueur"]["Identifiant"])
    else:
       joueur_dest = joueur.id_joueur_gauche(plateau["joueur"]["Identifiant"])


def diriger_trojan(plateau):
    """Dirige tous les trojans adjascents à des données personnelles vers ces données personnelles

    Args:
        plateau (dict): un plateau
    """
    la_matrice = get_matrice(plateau)
    for x in range(la_matrice["lignes"]):# nb lignes
        for y in range(la_matrice["colonnes"]):# nb colonnes
            if case.get_protection(get_case(plateau, x, y)) == protection.DONNEES_PERSONNELLES:
                coord  = (x,y)
                for x2 in range(la_matrice["lignes"]): # horizontale
                    for y2 in range(la_matrice["colonnes"]) :  #verticale
                        coord2 = (x2,y2)
                        if coord2[0] == coord[0]:
                            trojans = case.get_trojans(get_case(plateau,x2,y2))
                            if len(trojans) != 0:
                                if y2 > y:
                                    for trojan in trojans:
                                        trojan["Direction"] = 'G'
                                elif y2 < y:
                                    for trojan in trojans:
                                        trojan["Direction"] = 'D'
                        elif coord2[1] == coord[1]:
                            trojans = case.get_trojans(get_case(plateau,x2,y2))
                            if len(trojans) != 0:
                                if x2 > x:
                                    for trojan in trojans:
                                        trojan["Direction"] = 'H'
                                elif x2 < x:
                                    for trojan in trojans:
                                        trojan["Direction"] = 'B'

def deplacer_trojan_phase1(plateau):
    """déplace les chevaux de Troie présents sur les cases en fonction de leur direction
       cette fonction introduit aussi les trojans entrants du plateau
       Si le déplacement provoque la sortie du trojan du plateau, ce trojans est placés
       dans les trojans sortants du plateau

    Args:
        plateau (dict): un plateau
    """
    DICO_DIR = {(-1, -1): 'HG', (-1, 0): 'HH', (-1, 1): 'HD', (0, -1): 'GG',
            (0, 1): 'DD', (1, -1): 'BG', (1, 0): 'BB', (1, 1): 'BD'}
    for x in range(plateau["matrice"]["lignes"]):
        for y in range(plateau["matrice"]["colonnes"]):
            la_case = get_case(plateau,x,y)
            les_trojans = case.get_trojans(la_case)
            for trojan in les_trojans:
                for (val_dir,dire) in DICO_DIR.items():
                    if dire[0] == trojan["Direction"] and dire[1] == trojan["Direction"]:
                        coord = (x+val_dir[0],y+val_dir[1])
                        if coord[0]>0 and coord[0] <= plateau["matrice"]["lignes"] and coord[1]>0 and coord[1] <= plateau["matrice"]["colonnes"]:
                            new_case = get_case(plateau,coord[0],coord[1])
                            case.ajouter_trojan(new_case,trojan)
                            ajouter_trojan(plateau, trojan)
                            case.get_trojans(la_case).pop(trojan)
                        else:
                            plateau["sortants"].append(trojan)
                            case.get_trojans(la_case.pop(trojan))

def appliquer_dpo(plateau, ligne_protection, colonne_protection, les_trojans):
    """Cette fonction applique l'effet de la protection Data Protection Officer
       posée en ligne_protection, colonne_protection à une liste de trojans

    Args:
        plateau (dict): un plateau
        ligne_protection (int): la ligne de la protection
        colonne_protection (int): la colonne de la protection
        les_trojans (list): une liste de trojans
    """
    la_case = get_case(plateau,ligne_protection,colonne_protection)
    if matrice.get_val(plateau["matrice"],ligne_protection-1,colonne_protection) == get_case(plateau,ligne_protection-1,colonne_protection):
        for le_trojan in les_trojans:
            trojan.inverser_direction(le_trojan) # on inverse pour chaque trojan adjacent
    elif matrice.get_val(plateau["matrice"],ligne_protection,colonne_protection-1) == case.get_trojans(get_case(plateau,ligne_protection,colonne_protection-1)):
        for le_trojan in case.get_trojans(get_case(plateau,ligne_protection,colonne_protection-1)):
            trojan.inverser_direction(le_trojan)  

    elif matrice.get_val(plateau["matrice"],ligne_protection+1,colonne_protection) == case.get_trojans(get_case(plateau,ligne_protection+1,colonne_protection)):
        for le_trojan in case.get_trojans(get_case(plateau,ligne_protection+1,colonne_protection)):
            trojan.inverser_direction(le_trojan)

    elif matrice.get_val(plateau["matrice"],ligne_protection,colonne_protection+1) == case.get_trojans(get_case(plateau,ligne_protection,colonne_protection+1)):
        for le_trojan in case.get_trojans(get_case(plateau,ligne_protection,colonne_protection+1)):
            trojan.inverser_direction(le_trojan)

    elif matrice.get_val(plateau["matrice"],ligne_protection,colonne_protection) == case.get_trojans(la_case):
        for le_trojan in case.get_trojans(la_case):
            trojan.inverser_direction(le_trojan)
        


def appliquer_firewall_bdhg(plateau, ligne_protection, colonne_protection, les_trojans):
    """Cette fonction applique l'effet de la protection firewall basdroit-hautgauche
       posée en ligne_protection, colonne_protection à une liste de trojans

    Args:
        plateau (dict): un plateau
        ligne_protection (int): la ligne de la protection
        colonne_protection (int): la colonne de la protection
        les_trojans (list): une liste de trojans
    """
    la_case = get_case(plateau,ligne_protection,colonne_protection)
    for le_trojan in les_trojans:
        if le_trojan in case.get_trojans(la_case) :
            trojan.changer_direction_angle_bdhg(le_trojan)

def appliquer_firewall_bghd(plateau, ligne_protection, colonne_protection, les_trojans):
    """Cette fonction applique l'effet de la protection firewall basgauche-hautdroit
       posée en ligne_protection, colonne_protection à une liste de trojans

    Args:
        plateau (dict): un plateau
        ligne_protection (int): la ligne de la protection
        colonne_protection (int): la colonne de la protection
        les_trojans (list): une liste de trojans
    """
    la_case = get_case(plateau,ligne_protection,colonne_protection)
    for le_trojan in les_trojans:
        if le_trojan in case.get_trojans(la_case) :
            trojan.changer_direction_angle_bghd(le_trojan)


def appliquer_antivirus(plateau, ligne_protection, colonne_protection, les_trojans):
    """Cette fonction applique l'effet de la protection antivirus
       posée en ligne_protection, colonne_protection à une liste de trojans

    Args:
        plateau (dict): un plateau
        les_trojans (list): une liste de trojans
    """
    la_case = get_case(plateau,ligne_protection,colonne_protection)
    for le_trojan in les_trojans:
        if le_trojan in case.get_trojans(la_case) :
            plateau["sortants"].append(le_trojan)
            le_trojan["Createur"] = plateau["joueur"]["Identifiant"]
            
def deplacer_trojan_phase2(plateau):
    """Finalise le déplacements des chevaux de Troies en appliquant les protections

    Args:
        plateau (dict): un plateau

    Returns:
        dict: un dictionnaire donnant pour chaque joueur le nombre de trojans restant sur le plateau
    """
    res = dict()
    for x in range(plateau["matrice"]["lignes"]):
        for y in range(plateau["matrice"]["colonnes"]):
            la_case = get_case(plateau,x,y)
            case.set_les_trojans(la_case, case.get_trojans(la_case).extend(plateau["entrants"]), [])
            la_proc = case.get_protection(la_case)
            if case.contient_avatar(la_case): # note : les appels de fonctions ont l'air de faire mieux fonctionner le jeu
                case.set_les_trojans(la_case, [], [])
            elif la_proc == protection.ANTIVIRUS:
                appliquer_antivirus(plateau, x, y, case.get_trojans(la_case))
                protection.enlever_resistance(la_proc)
                if protection.get_resistance(la_proc) == 0:
                    protection.enlever_resistance(case.get_protection(get_case(plateau,x,y)))

            elif la_proc == protection.FIREWALL_BDHG:
                appliquer_firewall_bdhg(plateau, x, y, case.get_trojans(la_case))
                protection.enlever_resistance(la_proc)
                if protection.get_resistance(la_proc) == 0:
                    protection.enlever_resistance(case.get_protection(get_case(plateau,x,y)))

            elif la_proc == protection.FIREWALL_BGHD:
                appliquer_firewall_bghd(plateau, x, y, case.get_trojans(la_case))
                protection.enlever_resistance(la_proc)
                if protection.get_resistance(la_proc) == 0:
                    protection.enlever_resistance(case.get_protection(get_case(plateau,x,y)))

            elif la_proc == protection.DPO:
                    appliquer_dpo(plateau, x, y, case.get_trojans(la_case))
                    protection.enlever_resistance(la_proc)
                    if protection.get_resistance(la_proc) == 0:
                        protection.enlever_resistance(case.get_protection(get_case(plateau,x,y)))
            elif la_proc == protection.DONNEES_PERSONNELLES:
                    diriger_trojan(plateau)
                    protection.enlever_resistance(la_proc)
                    if protection.get_resistance(la_proc) == 0:
                        protection.enlever_resistance(case.get_protection(get_case(plateau,x,y)))
            elif case.get_serveur(la_case) != None:
                if case.get_trojans(la_case) != []:
                    if case.get_serveur(la_case)["Type"] == 0:
                        case.set_les_trojans(la_case, [], [])
                        equipement.attaque(plateau["serveur"])
                    else :
                        if case.get_trojans(la_case) !=[] :
                            if x==4:
                                directs = 'BDHG'
                                if trojan.get_direction(case.get_trojans(la_case)) == directs[plateau["joueur"]["Identifiant"]-1]:
                                    equipement.attaque(plateau["ordinateur"])
                    case.set_les_trojans(la_case,[],[])
            elif case.get_trojans(la_case) == None:
                case.set_les_trojans(la_case, [], case.get_trojans_entrants(la_case))
                if case.get_trojans(la_case) != [] :
                    if len(case.get_trojans(la_case)) > 1:
                        for trojan in case.get_trojans(la_case):
                            if trojan["Createur"] not in res.keys():
                                res[trojan["Createur"]] = 1
                            else:
                                res[trojan["Createur"]] += 1
                    else:
                        if res[trojan["Createur"]] not in res.keys():
                            res[trojan["Createur"]] = 1
                        else:
                            res[trojan["Createur"]] += 1
    return res

def reinit_les_sorties(plateau):
    """Reinitialise les sorties du plateau à vide

    Args:
        plateau (dict): un plateau
    """
    plateau["sortants"] = []


def nb_trojans_prochain(plateau):
    """fonction qui retourne une matrice indiquant combien de trojans se trouverontS
       sur chaque case du plateau au prochain tour

    Args:
        plateau (dict): un plateau

    Returns:
        dict: une matrice d'entiers
    """
    nb_l = matrice.get_nb_lignes(plateau["matrice"])
    nb_c = matrice.get_nb_colonnes(plateau["matrice"])
    res = matrice.creer_matrice(nb_l,nb_c,0)
    for x in plateau["matrice"]["lignes"]:
        for y in plateau["matrice"]["colonnes"]:
            case_valeur = get_case(plateau,x,y)
            case_val_trojan =  case.get_trojans(case_valeur)
            if  case_val_trojan != []:
                nb_trojans = len(case_val_trojan)
                matrice.set_val(res,x,y,nb_trojans)
    return res

def executer_ordres(plateau, ordres):
    """Exécute les ordres choisis par le joueur. Les ordres sont donnés sous la forme
       d'une chaine de caractères dont les deux premiers indique le déplacement de l'avatar
       le troisième caractère est
       soit un A pour une attaque
       soit un P pour une protection
       En cas d'attaque, les caractères suivants sont GxHyDz où
                    x y et z sont des chiffres entre 0 et 4 indiquant le numéro de la
                             ligne ou de la colonne où sera envoyé le trojan
       En cas de pose d'une protection les caractère suivants seront trois chiffre tlc où
                    t est le type de la protection
                    l la ligne où poser la protection
                    c la colonne où poser la protection
        Si la chaine est non conforme où l'action non permise le joueur perd 5 points.
        Notez que les points et les pénalités liés au déplacement de l'avatar sont gérés dans
        deplacer_avatar

    Args:
        plateau (dict): un plateau
        ordres (str): une chaine de caractères donnant les ordres du joueur
    """
    # GxHyDz ( JGauche x Jhaut y JDroite z)
    autorise = True
    dep_avatar = ordres[:2] #les indices AVANT le 3ème str de ordres
    print(ordres)
    if dep_avatar in DIRECTIONS_AVATAR:
        deplacer_avatar(plateau,dep_avatar)
    else:
        autorise = False

    if autorise:
        if len(ordres) > 2 :
            if ordres[2] == 'A': #si l'ordre est une attaque / Passer en commentaire pour avoir + de Trois tours 
                for ordre in range(3,len(ordres),2):
                    set_trojans_sortants(plateau,ordres[ordre],[trojan.creer_trojan(get_id_joueur(plateau),int(ordres[ordre+1]),ordres[ordre])])

            if ordres[2] == 'P': # si l'ordre est une protection
                type_p = int(ordres[3])
                lig = int(ordres[4])
                col = int(ordres[5])
                poser_protection(plateau,type_p,lig,col)
                protection = poser_protection(plateau,int(ordres[3]),int(ordres[4])-1,int(ordres[5])-1)
                if protection == False:
                    plateau["joueur"]["Nombre de points"] -= PENALITE
                    autorise = False
            else:
                plateau["joueur"]["Nombre de points"] -= PENALITE
                autorise = False
        if autorise:
            deplacer_trojan_phase1(plateau)
            deplacer_trojan_phase2(plateau)

# FONCTIONS A RECOPIER DANS VOTRE FICHIER
#-------------------------------------------------------------#
# Fonctions pour la sauvegarde et la restoration d'un plateau #
#-------------------------------------------------------------#


def plateau_2_str(plateau, separateur=";"):
    """sauvegarde un plateau sous la forme d'une chaîne de caractères

    Args:
        plateau (dict): un plateau
        separateur (str, optional): le séparateur utilisé pour séparer les champs
                                    sur une même ligne. Defaults to ";".

    Returns:
        str: la chaîne caractères représentant le plateau
    """
    pos_av = get_pos_avatar(plateau)
    res = "plateau"+separateur+str(get_taille(plateau))+"\n" +\
        "joueur"+separateur+str(get_id_joueur(plateau))+separateur+get_nom_joueur(plateau) +\
        separateur+str(get_points(plateau))+"\n" +\
        "avatar"+separateur+str(pos_av[0])+separateur+str(pos_av[1])+"\n" +\
        "serveur"+separateur+str(get_resistance_serveur(plateau))+"\n" +\
        "ordinateurs"+separateur+str(get_nb_ordis_restants(plateau))+"\n"
    res += "trojans entrants\n"
    for troj in get_trojans_entrants(plateau):
        res += str(trojan.get_createur(troj))+separateur+str(trojan.get_type(troj)) +\
            separateur+str(trojan.get_direction(troj))+"\n"
    res += "trojans sortants\n"
    for dest in "HBDG":
        res += dest+'\n'
        for troj in get_trojans_sortants(plateau, dest):
            res += str(trojan.get_createur(troj))+separateur+str(trojan.get_type(troj)) +\
                separateur+str(trojan.get_direction(troj))+"\n"
    res += "matrice\n"
    taille = get_taille(plateau)
    mat = get_matrice(plateau)
    for ligne in range(taille):
        for colonne in range(taille):
            la_case = matrice.get_val(mat, ligne, colonne)
            if case.get_trojans(la_case) != [] or case.get_trojans_entrants(la_case) != [] or\
                    case.get_protection(la_case) is not None:
                res += "case"+separateur + \
                    str(ligne)+separateur+str(colonne)+"\n"
                protec = case.get_protection(la_case)
                if protec is None:
                    res += "protection\n"
                else:
                    res += "protection"+separateur + \
                        str(protection.get_type(protec))+";" + \
                        str(protection.get_resistance(protec))+"\n"
                res += "trojans presents\n"
                for troj in case.get_trojans(la_case):
                    res += str(trojan.get_createur(troj))+separateur+str(
                        trojan.get_type(troj))+separateur+str(trojan.get_direction(troj))+"\n"
                res += "trojans entrants\n"
                for troj in case.get_trojans_entrants(la_case):
                    res += str(trojan.get_createur(troj))+separateur+str(
                        trojan.get_type(troj))+separateur+str(trojan.get_direction(troj))+"\n"
    return res+'fin plateau\n'


def valider_mot_cle(champs, indice, mot_cle, types_champs):
    """fonction outil permettant de valider un mot clé dans une chaine représentant un plateau

    Args:
        champs (list): liste des champs trouvé sur la ligne
        indice (int): numéro de la ligne dans la chaîne (utilisé pour les message d'erreur)
        mot_cle (str): le mot clé recherché
        types_champs (list): une liste de booléens indiquant les champs qui doivent être
                             convertis en entiers

    Raises:
        Exception: si le nombre de champs ne correspond pas à la longeur des types de champs +1
        Exception: si le mot clé n'est pas le premier champs
        Exception: si une convertion en entier s'est mal passée

    Returns:
        list: la liste des champs associés au mot clé
    """
    if len(champs) != len(types_champs)+1:
        raise Exception("ligne "+str(indice)+": comporte " +
                        str(len(champs))+" champs au lieu de "+str(len(types_champs)+1))

    if champs[0] != mot_cle:
        raise Exception("ligne "+str(indice) +
                        ": ne commence pas par le mot clé '"+mot_cle+"'")
    res = []
    for ind in range(len(types_champs)):
        if types_champs[ind]:
            try:
                res.append(int(champs[ind+1]))
            except:
                raise Exception("ligne "+str(indice)+": le "+str(ind+1) +
                                "eme champs devrait être un entier\n"+str(champs))
        else:
            res.append(champs[ind+1])
    return res


def liste_trojans_from_str(lignes, ind_debut, separateur):
    """récupère une liste de trojans dans les lignes à partir de ind_début

    Args:
        lignes (list): une liste de chaines de caractères correspondant à
            des lignes de la chaines représentant un plateau
        ind_debut (int): indice dans la liste lignes à partir de laquelle
            on recherche les trojans
        separateur (str): le caractère séparateur des champs dans une ligne

    Returns:
        int,list: le numéro de la ligne où s'arrête la liste de trojans, la
                  liste des trojans
    """
    res = []
    num_lig = ind_debut
    while True:
        champs = lignes[num_lig].split(separateur)
        if len(champs) != 3:
            break
        try:
            res.append(trojan.creer_trojan(
                int(champs[0]), int(champs[1]), champs[2]))
        except:
            break
        num_lig += 1
    return num_lig, res


def creer_plateau_from_str(chaine, separateur=';'):
    """recréer un plateau à partir d'une chaine de caractères

    Args:
        chaine (str): la chaine de caractère représentant le plateau
        separateur (str, optional): le caractère séparateur des champs au sein d'une ligne.
                                    Defaults to ';'.

    Raises:
        Des exceptions sont levées en cas d'erreur de format de la chaine d'entrée

    Returns:
        dict: le plateau correcpondant à la chaine de caractères
    """
    lignes = chaine.split("\n")
    # ligne 0
    champs = lignes[0].split(separateur)
    [taille] = valider_mot_cle(champs, 0, "plateau", [True])
    # ligne 1 : le joueur
    champs = lignes[1].split(separateur)
    [id_joueur, nom_joueur, nb_points] = valider_mot_cle(
        champs, 1, "joueur", [True, False, True])
    if id_joueur < 1 or id_joueur > 4:
        raise Exception("ligne 1: l'identifiant du joueur n'est pas correcte")
    # ligne 2 : l'avatar
    champs = lignes[2].split(separateur)
    [ligne_av, colonne_av] = valider_mot_cle(champs, 2, "avatar", [True, True])
    if ligne_av < 0 or ligne_av > taille or colonne_av < 0 or colonne_av > taille:
        raise Exception("ligne 2: la position de l'avatar est incorrecte")
    # ligne 3 serveur
    champs = lignes[3].split(separateur)
    [protec_serveur] = valider_mot_cle(champs, 3, "serveur", [True])
    if protec_serveur < 0: #or protec_serveur > 4:
        raise Exception("ligne 3: la protection du serveur est incorrecte")
    # ligne 4 ordinateurs
    champs = lignes[4].split(separateur)
    [protec_ordis] = valider_mot_cle(champs, 4, "ordinateurs", [True])
    if protec_ordis < 0 : #or protec_ordis > 5:
        raise Exception(
            "ligne 4: la protection des ordinateurs est incorrecte")
    # ligne 5 protection en cours
    champs = lignes[5].split(separateur)
    num_lig = 5
    valider_mot_cle(champs, num_lig, "trojans entrants", [])
    num_lig += 1
    num_lig, trojans_entrants = liste_trojans_from_str(
        lignes, num_lig, separateur)
    champs = lignes[num_lig].split(separateur)
    valider_mot_cle(champs, num_lig, "trojans sortants", [])
    num_lig += 1
    trojans_sortants = {}
    for direct in "HBDG":
        champs = lignes[num_lig].split(separateur)
        if len(champs) != 1:
            raise Exception("ligne "+str(num_lig)+": contient " +
                            str(len(champs))+" champs au lieu de 1")
        if champs[0] != direct:
            raise Exception("ligne "+str(num_lig) +
                            ": direction "+direct+" manquante")
        num_lig += 1
        num_lig, liste_trojans = liste_trojans_from_str(
            lignes, num_lig, separateur)
        trojans_sortants[direct] = liste_trojans

    le_plateau = creer_plateau(id_joueur, nom_joueur, taille)
    ajouter_points(le_plateau, nb_points)
    case.enlever_avatar(matrice.get_val(
        get_matrice(le_plateau), taille//2, taille//2))
    poser_avatar(le_plateau, ligne_av, colonne_av)
    set_trojans_entrants(le_plateau, trojans_entrants)
    for direct in trojans_sortants:
        set_trojans_sortants(le_plateau, direct, trojans_sortants[direct])
    equipement.set_resistance(get_serveur(le_plateau), protec_serveur)
    equipement.set_resistance(get_ordis(le_plateau), protec_ordis)
    champs = lignes[num_lig].split(separateur)
    valider_mot_cle(champs, num_lig, "matrice", [])
    num_lig += 1
    la_matrice = get_matrice(le_plateau)
    while True:
        champs = lignes[num_lig].split(separateur)
        if champs[0] != "case":
            break
        if len(champs) != 3:
            raise Exception("ligne "+str(num_lig)+": contient " +
                            str(len(champs))+" champs au lieu de 3")
        try:
            ligne = int(champs[1])
            colonne = int(champs[2])
            if ligne < 0 or ligne >= taille or colonne < 0 or colonne >= taille:
                raise Exception()
        except:
            raise Exception("ligne "+str(num_lig) +
                            ": la spécification de la case n'est pas correcte")
        num_lig += 1
        champs = lignes[num_lig].split(separateur)
        protect = None
        if len(champs) != 1 and len(champs) != 3:
            raise Exception("ligne "+str(num_lig) +
                            " : la ligne doit comporter 1 ou 3 champs")
        if champs[0] != "protection":
            raise Exception("ligne "+str(num_lig) +
                            " : mot cle protection manquant")
        if len(champs) == 3:
            try:
                type_p = int(champs[1])
                res_p = int(champs[2])
                if type_p < 0 or type_p >= protection.PAS_DE_PROTECTION or res_p > 2 or res_p <= 0:
                    raise Exception()
                protect = protection.creer_protection(type_p, res_p)
            except:
                raise Exception("ligne "+str(num_lig) +
                                " : la protection est mal spécifiée")
        num_lig += 1
        champs = lignes[num_lig].split(separateur)
        valider_mot_cle(champs, num_lig, "trojans presents", [])
        num_lig += 1
        num_lig, trojan_cp = liste_trojans_from_str(
            lignes, num_lig, separateur)
        champs = lignes[num_lig].split(separateur)
        valider_mot_cle(champs, num_lig, "trojans entrants", [])
        num_lig += 1
        num_lig, trojan_ce = liste_trojans_from_str(
            lignes, num_lig, separateur)
        la_case = matrice.get_val(la_matrice, ligne, colonne)
        case.set_les_trojans(la_case, trojan_cp, trojan_ce)
        if protect is not None:
            case.set_protection(la_case, protect)
    champs = lignes[num_lig].split(separateur)
    valider_mot_cle(champs, num_lig, "fin plateau", [])
    return le_plateau


def sauver_plateau(plateau, nom_fic, separateur=';'):
    """sauvegarde un plateau dans un fichier

    Args:
        plateau (dict): un plateau
        nom_fic (str): le nom du fichier où sauvegarder le plateau
        separateur (str, optional): caractère séparateur utiliser dans le fichier. Defaults to ';'.
    """
    with open(nom_fic, "w") as fic:
        fic.write(plateau_2_str(plateau, separateur))


def charger_plateau(nom_fic, separateur=";"):
    """charge un plateau sauvegardé dans un fichier

    Args:
        nom_fic (str): nom du fichier
        separateur (str, optional): caractère séparateur utiliser dans le fichier. Defaults to ";".

    Returns:
        plateau: un plateau
    """
    with open(nom_fic) as fic:
        chaine = fic.read()
        return creer_plateau_from_str(chaine, separateur)

# fonctions additionnelles sur le plateau
def set_nom_joueur(plateau, nom_joueur):
    """change le nom du joueur de ce plateau

    Args:
        plateau (dict): le plateau
        nom_joueur (str): le nom du joueur
    """    
    plateau["nom"] = nom_joueur
