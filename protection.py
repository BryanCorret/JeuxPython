
"""
              Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module protection.py
    gère les protections que les joueurs peuvent utiliser
"""

DPO = 0
FIREWALL_BDHG = 1
FIREWALL_BGHD = 2
DONNEES_PERSONNELLES = 3
ANTIVIRUS = 4
PAS_DE_PROTECTION = 5

RESISTANCE = 2


def creer_protection(type_p, resistance):
    """créer une protection

    Args:
        type_p (int): type de la protection
        resistance (int): nombre d'attaques que peut supporter la protection

    Returns:
        dict: une protection
    """
    protection = dict()
    protection["Type"] = type_p
    protection["Résistance"] = resistance
    return protection


def get_type(protection):
    """retourne le type de la protection

    Args:
        protection (dict): une protection

    Returns:
        int: le type de la protection
    """
    return protection["Type"]
    

def get_resistance(protection):
    """retourne la résistance de la protection

    Args:
        protection (dict): une protection

    Returns:
        int: la resistance de la protection
    """
    return protection["Résistance"]


def enlever_resistance(protection):
    """Enlève un point de résistance de la protection et retourne la resistance restante

    Args:
        protection (dict): une protection

    Returns:
        int: la resistance restante
    """
    protection["Résistance"]=protection["Résistance"]-1
    if protection["Résistance"] <= 0:
        protection["Résistance"] = 0
    return protection["Résistance"]