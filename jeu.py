"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module jeu.py
"""

import random
import plateau
import protection
import matrice
import trojan
DIRECTIONS_AVATAR2 = ['DD', 'GG', 'HH', 'BB', 'HD', 'HG', 'BD', 'BG']
def creer_jeu(liste_joueurs, taille_plateau=5, resistance_serveur=40, resistance_pc=50,
    resistance_protection=2, humain=False, nb_tours_max=-1, tour_actu=1):
    """Créer un nouveau jeu avec 4 joueurs

    Args:
        liste_joueurs (list): la liste des noms de joueur
        taille_plateau (int, optional): le coté du plateau. Defaults to 5.
        resistance_serveur (int, optional): la resistance du serveur. Defaults to 4.
        resistance_pc (int, optional): la resistance des PC. Defaults to 5.
        resistance_protection (int, optional): la resistance des protections. Defaults to 2.
        humain (bool, optional): indique si le joueur 1 est humain. Defaults to False.
        nb_tours_max (int, optional): indique le nombre de tours de la partie
                                      (-1 pour indiquer pas de limite). Defaults -1.

    Returns:
        dict: le jeu
    """
    jeu = dict()
    jeu["plateau"]=[]
    for i in range(len(liste_joueurs)):
        jeu["plateau"].append(plateau.creer_plateau(i+1, liste_joueurs[i],taille_plateau,resistance_serveur,resistance_pc))
    jeu["humain"] = humain
    jeu["taille"] = taille_plateau
    jeu["tours_max"] = nb_tours_max
    jeu["tour_actu"] = tour_actu
    jeu["def_protec"] = resistance_protection
    return jeu

def get_taille_plateau(jeu):
    """Retourne la taille des plateau

    Args:
        jeu (dict): un jeu

    Returns:
        int: la taille des plateau
    """
    
    return jeu["taille"]

def get_plateau(jeu, id_joueur):
    """ retourne le plateau de joueur indenfié par id_joueur

    Args:
        jeu (dict): un jeu
        id_joueur (int): l'identifiant du joueur (entre 1 et 4)

    Returns:
        dict: le plateau du joueur
    """
    return jeu["plateau"][id_joueur-1]


def est_fini(jeu):
    """indique si la partie est terminée

    Args:
        jeu (dict): un jeu

    Returns:
        bool: un booléen à True si au moins trois joueur sont éliminés ou
              que le nombre de tours max est atteint
    """
    if get_num_tour(jeu) == get_nb_tours_max(jeu):
        return True
    eliminer = []
    for i in [1,2,3,4]:
        if jeu["plateau"][i-1] is None:
            eliminer.append(i)
            if len(eliminer) == 3 :
                return True
    return False
     

def get_num_tour(jeu):
    """retourne le numéro du tour en cours

    Args:
        jeu (dict): un jeu

    Returns:
        int: le numéro du tour
    """
    return jeu["tour_actu"]


def echange_trojans(jeu):
    """Effectue les échanges de trojans entre les joueurs (des sorties vers les entrées)

    Args:plateau
        jeu (dict): un jeu
    """
    direction = ''
    for i in range(4): 
        for trojans in jeu["plateau"][i]["sortants"]:
            direction = trojan.get_direction(trojans)
            if direction == 'G':
                opposant = plateau.id_joueur_gauche(jeu["plateau"][i])-1
                plateau.set_trojans_entrants(jeu["plateau"][opposant], trojans)
            elif direction == 'D':
                opposant = plateau.id_joueur_droite(jeu["plateau"][i])-1
                plateau.set_trojans_entrants(jeu["plateau"][opposant], trojans)
            elif direction == 'H':
                opposant = plateau.id_joueur_haut(jeu["plateau"][i])-1
                plateau.set_trojans_entrants(jeu["plateau"][opposant], trojans)
        plateau.set_trojans_sortants(jeu["plateau"][i], direction, [])

def diriger_trojan(jeu):
    """Applique la protection DONNEES_PERSONNELLES sur les quatre plateaux

    Args:
        jeu (dict): un jeu
    """
    for i in [1,2,3,4]:
        plateau.diriger_trojan(jeu["plateau"][i-1])


def phase1(jeu):
    """Effectue les déplacements des trojans sur les 4 plateaux

    Args:
        jeu ((dict): un jeu
    """
    for i in [1,2,3,4]:
        plateau.deplacer_trojan_phase1(jeu["plateau"][i-1])


def phase2(jeu):
    """Finalise les déplacements des trojans sur les 4 plateaux.
       cette fonction doit augementer le numero du tour de jeu de 1

    Args:
        jeu ((dict): un jeu
    """
    for i in [1,2,3,4]:
        plateau.deplacer_trojan_phase2(jeu["plateau"][i-1])
    jeu["tour_actu"]+=1

# RECOPIER A PARTIR D'ICI DANS VOTRE FICHIER

def joueur_humain():
    """

    Returns:
        str: une chaine de caractères indiquant les ordres donnés par la personne
    """
    print("indiquez le direction de votre avatar")
    res = input()

    rep = input(
        "Souhaitez vous (P)oser une protection ou (A)ttaquer les adversaires? (P/A)")
    res += rep
    if rep == 'P':
        print(
            "indiquez le type de protection [O"+str(protection.PAS_DE_PROTECTION)+"]")
        type_protection = input()
        try:
            type_protection = int(type_protection)
        except:
            type_protection = protection.PAS_DE_PROTECTION
        if type_protection != protection.PAS_DE_PROTECTION:
            print("indiquez la position de votre protection")
            ligne = input("numero de la ligne ")
            colonne = input("numero de la colonne")
            try:
                ligne = int(ligne)
                colonne = int(colonne)
            except:
                type_protection = protection.PAS_DE_PROTECTION
        res += str(type_protection)+str(ligne)+str(colonne)
    elif rep == 'A':
        for direction in "GHD":
            print("indiquez le type de virus à envoyer vers "+direction)
            try:
                type_vir = int(input())
            except:
                type_vir = -1
            res += direction+str(type_vir)
    return res


def joueur_aleatoire(le_plateau):
    """produit des ordres aléatoires

    Args:
        le_plateau (dict): un plateau

    Returns:
        str: une chaine de caractères donnant des ordres compatibles mais aléatoires
        Les ordres sont donnés sous la forme
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
    """
    # choix du déplacement de l'avatar
    res = random.choice(list(plateau.DIRECTIONS_AVATAR))
    taille = plateau.get_taille(le_plateau)
    # choix entre poser une protection ou attaquer les adversaires
    if random.randint(0, 1) == 0:
        ligne = random.randint(0, taille-1)
        colonne = random.randint(0, taille-1)
        ind_protect = random.randint(0, protection.PAS_DE_PROTECTION-1)
        if ligne != taille//2 or colonne != taille//2:
            res += 'P'+str(ind_protect)+str(ligne)+str(colonne)
    else:  # on attaque les adversaires
        res += 'A'
        les_voisins = ['G', 'H', 'D']
        for direct in les_voisins:
            res += direct+str(random.randint(0, 4))
    return res


def actions_joueur(jeu):
    """Récolte et exécute les actions choisies par chacun des joueurs

    Args:
        jeu (dict): un jeu
    """
    for id_joueur in range(1, 5):
        le_plateau = get_plateau(jeu, id_joueur)
        if plateau.a_perdu(le_plateau):
            continue
        if id_joueur == 1 and est_humain(jeu):
            ordres = joueur_humain()
        else:
            ordres = joueur_aleatoire(le_plateau)

        plateau.executer_ordres(le_plateau, ordres)
    echange_trojans(jeu)


def actions_joueur_ext(jeu, ordres):
    """Permet de faire jouer chaque joueur un tour de jeu

    Args:
        jeu (dict): le jeu sur lequel on joue
        ordres (dict): un dictionnaire dont les clés sont les numéros de joueur 
                       et les valeurs les str donnant les ordres de chaque joueur
    """
    for id_joueur in range(1, 5):
        le_plateau = get_plateau(jeu, id_joueur)
        if plateau.a_perdu(le_plateau):
            continue
        plateau.executer_ordres(le_plateau, ordres[id_joueur])
    echange_trojans(jeu)


def jeu_2_str(jeu, sep="\n||----||\n"):
    """Transforme un jeu en str pour le transfert via le réseau

    Args:
        jeu (dict): le jeu à transformer
        sep (str, optional): ce qui sépare deux plateaux. Defaults to "\n||----||\n".

    Returns:
        str: la chaine de caractères qui encode le jeu
    """
    type_joueur = 'O'
    if est_humain(jeu):
        type_joueur = 'H'
    res = str(get_num_tour(jeu))+';'+str(get_nb_tours_max(jeu))+';'+type_joueur
    for i in range(1, 5):
        res += sep+plateau.plateau_2_str(get_plateau(jeu, i))
    return res


def creer_jeu_from_str(jeu_str, sep="\n||----||\n"):
    """creer un jeu à partir d'une chaine de caractères

    Args:
        jeu_str (str): la chaine de caractères qui encode le jeu
        sep (str, optional): le séparateur de plateau. Defaults to "\n||----||\n".

    Returns:
        dict: le jeu codé dans la chaine de caractères
    """
    plateaux = jeu_str.split(sep)
    nb_tours, nb_tours_max, type_joueur = plateaux[0].split(";")
    nb_tours = int(nb_tours)
    nb_tours_max = int(nb_tours_max)
    humain = type_joueur == 'H'
    liste_plateaux = []
    for ind in range(1,len(plateaux)):
        liste_plateaux.append(plateau.creer_plateau_from_str(plateaux[ind]))
    return creer_jeu_en_cours(nb_tours, nb_tours_max, humain, liste_plateaux)


def sauver_jeu(jeu, nom_fic):
    """sauvegarde un jeu dans un fichier

    Args:
        jeu (dict): le jeu à sauvegarder
        nom_fic (str): le nom du fichier où sauvegarder le jeu
    """
    with open(nom_fic, "w") as fic:
        fic.write(jeu_2_str(jeu))


def charger_jeu(nom_fic):
    """créer un jeu à partir d'une sauvegarde

    Args:
        nom_fic (str): le nom du fichier

    Returns:
        dict: le jeu lu dans le fichier
    """
    with open(nom_fic) as fic:
        chaine = fic.read()
        return creer_jeu_from_str(chaine)


# fonctions additionnelles sur le jeu
def set_nom_joueur(jeu, id_joueur, nom_joueur):
    """change le nom du joueur numéro id_joueur

    Args:
        jeu (dict): le jeu
        id_joueur (int): un nombre entre 1 et 4 indiquant le joueur que l'on veut modifier
        nom_joueur (str): le nom du joueur
    """
    plateau.set_nom_joueur(jeu["plateau"][id_joueur],nom_joueur)


def est_humain(jeu):
    """Indique si le joueur 1 est humain ou non

    Args:
        jeu (dict): le jeu

    Returns:
        bool: True si le joueur 1 est humain
    """
    return jeu["humain"]


def get_nb_tours_max(jeu):
    """Retourne le nombre de tours maximum pour la partie

    Args:
        jeu (dict): le jeu

    Returns:
        int: le nombre de tours maximum du jeu 
    """
    return jeu["tours_max"]


def creer_jeu_en_cours(num_tours, nb_tours_max, humain, liste_plateaux):
    """crée un jeu à partir des informations donnés en paramètres. liste_plateaux
       donne la liste des plateaux dans l'ordre des joueurs (liste_plateaux[0] est le plateau du joueur 1 etc.)


    Args:
        num_tours (int): le numéro du tour
        nb_tours_max (int): le nombre de tours maximum
        humain (bool): True si le joueur 1 est un humain
        liste_plateaux (list): la liste des 4 plateaux des 4 joueurs
    """
    liste_joueurs = []
    for plateau in liste_plateaux:
        liste_joueurs.append(plateau["joueur"])
    jeu_cours=creer_jeu(liste_joueurs,humain=humain,nb_tours_max=nb_tours_max,tour_actu=num_tours)
    for ind in range(4):
        jeu_cours["plateau"][ind] = liste_plateaux[ind]
    
def joueur_ia(jeu, id_joueur):
    """calcule les action du joueur id_joueur en fonction de l'état du jeu

    Args:
        jeu (dict): le jeu
        id_joueur (int): un nombre entre 1 et 4 indiquant quel joueur doit jouer
    Returns:
        str: la chaine de caractères donnant les ordres choisis par le joueur
    """
    # à titre d'exemple
    le_plateau = get_plateau(jeu, id_joueur)
    check_protection = False
    for x in range(jeu["plateau"][id_joueur]["matrice"]["lignes"]):
        for y in range(jeu["plateau"][id_joueur]["matrice"]["colonnes"]):
            la_case=plateau.get_case(le_plateau,x,y)
            if plateau.case.get_protection(la_case) != None:
                check_protection = True
                break
    ordres = DIRECTIONS_AVATAR2[random.randint(0,7)]
    if check_protection:
        plateau.executer_ordres(le_plateau,ordres+'AG1H2D3')
    else:
        protect_aleatoire = str(random.randint(1,4))
        endrois_aleatoire = str(random.randint(0,4))+str(random.randint(0,4))
        plateau.executer_ordres(le_plateau,ordres+'P'+protect_aleatoire+endrois_aleatoire)
    return joueur_aleatoire(le_plateau)
