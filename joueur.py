"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module joueur.py
Module de gestion des joueurs
"""


def creer_joueur(id_joueur, nom_joueur, nb_points=0):
    """créer un nouveau joueur

    Args:
        id_joueur (int): l'identifiant du joueur (un entier de 1 à 4)
        nom_joueur (str): le nom du joueur
        nb_points (int, optional): le nombre de points du joueur. Defaults to 0.

    Returns:
        dict: le joueur
    """
    joueur = dict()
    joueur["Identifiant"] = id_joueur
    joueur["Nom"] = nom_joueur
    joueur["Nombre de points"] = nb_points
    return joueur


def get_id(joueur):
    """retourne l'identifiant du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur
    """
    return joueur["Identifiant"]


def get_nom(joueur):
    """retourne le nom du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        str: nom du joueur
    """
    return joueur["Nom"]


def get_points(joueur):
    """retourne le nombre de points du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: le nombre de points du joueur
    """
    return joueur["Nombre de points"]


def ajouter_points(joueur, points):
    """ajoute des points au joueur

    Args:
        joueur (dict): un joueur
        points (int): le nombre de points à ajouter

    Returns:
        int: le nombre de points du joueur
    """
    joueur["Nombre de points"] += points
    return joueur["Nombre de points"]


def id_joueur_droite(joueur):
    """retourne l'identifiant du joueur à droite d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur de droite
    """
    id_droite = joueur["Identifiant"] + 1
    if id_droite > 4:
        id_droite = id_droite - 4
    return id_droite


def id_joueur_gauche(joueur):
    """retourne l'identifiant du joueur à gauche d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur de gauche
    """
    id_gauche = joueur["Identifiant"] + 3
    if id_gauche > 4:
        id_gauche = id_gauche - 4
    return id_gauche


def id_joueur_haut(joueur):
    """retourne l'identifiant du joueur au dessus d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur du haut
    """
    id_haut = joueur["Identifiant"] + 2
    if id_haut > 4:
        id_haut = id_haut - 4 
    return id_haut

# fonctions additionnelles sur joueur
def set_nom(joueur, nom_joueur):
    """change le nom du joueur

    Args:
        joueur (dict): le joueur
        nom_joueur (str): le nom du joueur
    """    
    joueur["Nom"] = nom_joueur 