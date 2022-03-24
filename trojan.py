"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module trojan.py
    ce module gère les chevaux de Troie appelés Trojan"""



def creer_trojan(createur, type_t, direction):
    """Créer un nouveau trojan

    Args:
        createur (int): identifiant du créateur
        type_t (int): le type du trojan (un nombre entre 0 et 4)
        direction (str): une des directions 'H' 'B' 'G' ou 'D

    Returns:
        dict: un trojan
    """
    trojan = dict()
    trojan["Createur"] = createur
    trojan["Type"] = type_t
    trojan["Direction"] = direction
    return trojan


def get_createur(trojan):
    """retourne l'identifiant du créateur du trojan

    Args:
        trojan (dict): un trojan

    Returns:
        int: l'identifiant du créateur
    """
    return trojan["Createur"]



def get_type(trojan):
    """retourne le type du trojan

    Args:
        trojan (dict): un trojan

    Returns:
        int: le  type du trojan (un nombre entre 0 et 4)
    """
    return trojan["Type"]


def get_direction(trojan):
    """retourne la direction dans laquelle le trojan se dirige

    Args:
        trojan (dict): un trojan

    Returns:
        int: la direction du trojan
    """
    return trojan["Direction"]


def set_createur(trojan, createur):
    """change le créateur d'un trojan

    Args:
        trojan (dict): un trojan
        createur (int): l'identifiant du nouveau créateur
    """
    trojan["Createur"] = createur


def set_direction(trojan, direction):
    """change le créateur d'un trojan

    Args:
        trojan (dict): un trojan
        direction (str): une des directions 'H' 'B' 'G' ou 'D
    """
    trojan["Direction"] = direction


def set_type(trojan, type_t):
    """positionne le type du trojan

    Args:
        trojan (dict): un trojan
        type_t (int): un nombre entre 0 et 4
    """
    trojan["Type"] = type_t


def inverser_direction(trojan):
    """permet d'inverser la direction d'un trojan suivant le principe
       D -> G, G -> D, H -> B et B -> H

    Args:
        trojan (dict): un trojan
    """
    if trojan["Direction"] == "D" :
        set_direction(trojan,"G")
    elif trojan["Direction"] == "G" :
        set_direction(trojan,"D")
    elif trojan["Direction"] == "B" :
        set_direction(trojan,"H")
    elif trojan["Direction"] == "H" :
        set_direction(trojan,"B")


def changer_direction_angle_bdhg(trojan):
    """permet de faire rebondir un trojan de 45° sur un mur allant de bas droit  vers haut gauche
       D -> B, G ->H, H -> D et B -> G

    Args:
        trojan  (dict): un trojan
    """
    if trojan["Direction"] == "D" :
        set_direction(trojan,"B")
    elif trojan["Direction"] == "G" :
        set_direction(trojan,"H")
    elif trojan["Direction"] == "B" :
        set_direction(trojan,"G")
    elif trojan["Direction"] == "H" :
        set_direction(trojan,"D")


def changer_direction_angle_bghd(trojan):
    """permet de faire rebondir un trojan de 45° sur un mur allant de bas gauche  vers haut droit
       D -> H, G ->B, H -> G et B -> D

    Args:
        trojan  (dict): un trojan
    """
    if trojan["Direction"] == "D" :
        set_direction(trojan,"H")
    elif trojan["Direction"] == "G" :
        set_direction(trojan,"B")
    elif trojan["Direction"] == "B" :
        set_direction(trojan,"D")
    elif trojan["Direction"] == "H" :
        set_direction(trojan,"G")
