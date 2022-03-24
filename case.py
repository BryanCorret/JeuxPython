"""
              Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module case.py
    ce module gère les cases du plateau
"""
import trojan
import protection

def creer_case(fleche, la_protection, serveur, liste_trojans):
    """créer une case du plateau

    Args:
        fleche (str): une des quatre directions 'H' 'B' 'G' 'D' ou '' si pas de flèche sur la case
        la_protection (dict): l'objet de protection posé sur la case (None si pas d'objet)
        serveur (dict): le serveur posé sur la case (None si pas de serveur)
        liste_trojan s(list): la liste des trojans présents sur le case

    Returns:
        dict: la représentation d'une case
    """
    case = dict()
    case["fleche"] = fleche
    case["protection"] = la_protection
    case["serveur"] = serveur
    if liste_trojans == None:
        case["presents"] == []
    else:
        case["presents"] = liste_trojans
    case["entrants"] = []
    case["avatar"] = False
    return case



def get_fleche(case):
    """retourne la direction de la flèche de la case

    Args:
        case (dict): une case

    Returns:
        str: la direction 'H', 'B', 'G', 'D' ou '' si pas de flèche sur la case
    """
    return case["fleche"]


def get_protection(case):
    """retourne l'objet de protection qui se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        dict: l'objet de protection présent sur la case (None si pas d'objet)
    """
    return case["protection"]


def get_serveur(case):
    """retourne le serveur qui se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        dict: le serveur présent sur la case (None si pas d'objet)
    """
    return case["serveur"]


def get_trojans(case):
    """retourne la liste des trojans présents sur la case

    Args:
        case (dict): une case

    Returns:
        list: la liste des trojans présents sur la case
    """
    return case["presents"]


def get_trojans_entrants(case):
    """retourne la liste des trojans qui vont arriver sur la case

    Args:
        case (dict): une case

    Returns:
        list: la liste des trojans qui vont arriver sur la case
    """
    return case["entrants"]


def set_fleche(case, direction):
    """affecte une direction à la case

    Args:
        case (dict): une case
        direction (dict): 'H', 'B', 'G', 'D' ou '' si pas de flèche sur la case
    """
    case["fleche"] = direction


def set_serveur(case, serveur):
    """affecte un serveur à la case

    Args:
        case (dict): une case
        serveur (str): le serveur
    """
    case["serveur"] = serveur


def set_protection(case, la_protection):
    """affecte une protection à la case

    Args:
        case (dict): une case
        la_protection (dict): la protection
    """
    case["protection"] = la_protection


def set_les_trojans(case, trojans_presents, trojans_entrants):
    """fixe la liste des trojans présents et les trojans arrivant sur la case

    Args:
        case (dict): une case
        trojans_presents (list): une liste de trojans
        trojans_entrants ([type]): une liste de trojans
    """
    case["presents"]=trojans_presents
    case["entrants"]=trojans_entrants


def ajouter_trojan(case, un_trojan):
    """ajouter un nouveau trojan arrivant à une case

    Args:
        case (dict): la case
        un_trojan (dict): le trojan à ajouter
    """
    case["entrants"].append(un_trojan)

def mettre_a_jour_case(case):
    """met les trojans arrivants comme présents et réinitialise les trojans arrivants
       change la direction du trojan si nécessaire (si la case comporte une flèche)
       la fonction retourne un dictionnaire qui indique pour chaque numéro de joueur
       le nombre de trojans qui vient d'arriver sur la case.
       La fonction enlève une resistance à protection qui se trouve sur elle et la détruit si
       la protection est arrivée à 0.

    Args:
        case (dict): la case

    Returns:
        dict: un dictionnaire dont les clés sont les numéros de joueur et les valeurs
              le nombre de trojans arrivés sur la case pour ce joueur
    """
    set_les_trojans(case,get_trojans_entrants(case), [])
    if get_fleche(case) != '':
        for trojan_act in get_trojans(case):
            trojan.set_direction(trojan_act, get_fleche(case))

    if get_protection(case) != None:  
        if protection.enlever_resistance(get_protection(case)) == 0:
            set_protection(case, None)
    
            
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for trojan_act in get_trojans(case):
        createur = trojan.get_createur(trojan_act)
        if createur in res.keys():
            res[createur] += 1  
    if get_protection(case) != None:  
        if protection.enlever_resistance(get_protection(case)) == 0:
            set_protection(case, None)    
    return res


def poser_avatar(case):
    """pose l'avatar sur cette case et élimines les trojans présents sur la case.
       la fonction indique combien de trojans ont été éliminés

    Args:
        case (dict): une case

    Returns:
        dict: un dictionnaire dont les clés sont les numéros de joueur et les valeurs le nombre
        de trojans éliminés pour ce joueur.
    """
    dico=dict()
    case['avatar'] = True
    if case['avatar'] == True:
        for les_trojans in get_trojans(case):
            if trojan.get_createur(les_trojans) not in dico.keys():
                dico [trojan.get_createur(les_trojans)] = 1
            else:
                dico [trojan.get_createur(les_trojans)] += 1

        set_les_trojans(case, [], [])
        for id in range(1, 5):
            if id not in dico.keys():
                dico[id]= 0
    return dico
            


def enlever_avatar(case):
    """enlève l'avatar de la case

    Args:
        case (dict): une case
    """
    if contient_avatar(case) == True:
        case["avatar"] = False

def contient_avatar(case):
    """vérifie si l'avatar se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        bool: True si l'avatar est sur la case et False sinon[type]: [description]
    """
    try:
        if case["avatar"]:
            return True
    except:
        return False


def reinit_trojans_entrants(case):
    """reinitialise la liste des trojans entrants à la liste vide

    Args:
        case ([type]): [description]
    """
    case["entrants"] = []
