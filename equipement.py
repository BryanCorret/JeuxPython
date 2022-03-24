"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module equipement.py
    ce module gère les équipements ordinateurs et serveurs
"""

SERVEUR = 0
ORDINATEUR = 1


def creer_equipement(type_e, resistance):
    """créer un équipement avec resistance

    Args:
        type_e (int): type de l'équipement
        resistance (int): le nombre d'attaques nécessaires pour détruire l'équipement

    Returns:
        dict: une structure représentant l'équipement
    """
    equipement = dict()
    equipement["Type"] = type_e
    equipement["Resistance"] = resistance
    return equipement


def attaque(equipement):
    """Enlève une protection à l'équipement

    Args:
        equipement (dict): un équipement
    """
    equipement["Resistance"]-=1
    if equipement["Resistance"] <= 0:
        equipement["Resistance"]=0
    return get_resistance(equipement)

def est_detruit(equipement):
    """Indique si l'équipement est détruit (n'a plus de resistance)

    Args:
        equipement (dict): un équipement

    Returns:
        bool: True si l'équipement n'a plus de résistance et False sinon
    """
    if equipement["Resistance"] == 0 :
        return True
    return False


def get_resistance(equipement):
    """retourne la resistance de l'équipement

    Args:
        equipement (dict): un équipement

    Returns:
        int: la resistance restante de l'équipement
    """
    return equipement["Resistance"]


def get_type(equipement):
    """retourne le type de l'équipement

    Args:
        equipement (dict): un équipement

    Returns:
        int: le type de l'équipement
    """
    return equipement["Type"]


def set_resistance(equipement, resistance):
    """positionne la résistance d'un équipement à une valeur donnée

    Args:
        equipement (dict): un équipement
        resistance (int): la résistance restante de l'équipement
    """
    equipement["Resistance"] = resistance
