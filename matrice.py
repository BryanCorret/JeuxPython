"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module matrice.py
    Ce module de gestion des matrices
"""




def creer_matrice(nb_lig, nb_col, val_defaut=None):
    """créer une matrice contenant nb_lig lignes et nb_col colonnes avec
       pour valeur par défaut val_defaut

    Args:
        nb_lig (int): un entier strictement positif
        nb_col (int): un entier strictement positif
        val_defaut (Any, optional): La valeur par défaut des éléments de la matrice.
                                    Defaults to None.
    Returns:
        dict: la matrice
    """
    matrice = dict()
    matrice["lignes"] = nb_lig
    matrice["colonnes"] = nb_col
    matrice["listes_vals"] = []
    for ligne in range(nb_lig):
        matrice["listes_vals"].append([])
        for colonnes in range(nb_col):
            matrice["listes_vals"][ligne].append(val_defaut)
    return matrice



def get_nb_lignes(matrice):
    """retourne le nombre de lignes de la matrice

    Args:
        matrice (dict): une matrice

    Returns:
        int: le nombre de lignes de la matrice
    """
    return matrice["lignes"]


def get_nb_colonnes(matrice):
    """retourne le nombre de colonnes de la matrice

    Args:
        matrice (dict): une matrice

    Returns:
        int: le nombre de colonnes de la matrice
    """
    return matrice["colonnes"]


def get_val(matrice, lig, col):
    """retourne la valeur en lig, col de la matrice

    Args:
        matrice (dict): une matrice
        lig (int): numéro de la ligne (en commençant par 0)
        col (int): numéro de la colonne (en commençant par 0)

    Returns:
        Any: la valeur en lig, col de la matrice
    """
    return matrice["listes_vals"][lig-1][col-1]


def set_val(matrice, lig, col, val):
    """stocke la valeur val en lig, col de la matrice

    Args:
        matrice (dict): une matrice
        lig (int): numéro de la ligne (en commençant par 0)
        col (int): numéro de la colonne (en commençant par 0)
        val (Any): la valeur à stocker
    """
    matrice["listes_vals"][lig-1][col-1]=val


def max_matrice(matrice, interdits=None):
    """retourne la liste des coordonnées des cases contenant la valeur la plus grande de la matrice
        Ces case ne doivent pas être parmi les interdits.

    Args:
        matrice (dict): une matrice
        interdits (set): un ensemble de tuples (ligne,colonne) de case interdites. Defaults to None

    Returns:
        list: la liste des coordonnées de cases de valeur maximale dans la matrice (hors cases interdites)
    """
    res = []
    val = 0
    for x in range(matrice["lignes"]):
        for y in range(matrice["colonnes"]):
            if (val==None or get_val(matrice,x,y))>val and (interdits==None or (x,y) not in interdits):
                val=get_val(matrice,x,y)
                res= [(x,y)]
            elif (get_val(matrice,x,y)==val) and (interdits==None or (x,y) not in interdits):
                res.append((x,y))
    return res
        
      

DICO_DIR = {(-1, -1): 'HG', (-1, 0): 'HH', (-1, 1): 'HD', (0, -1): 'GG',
            (0, 1): 'DD', (1, -1): 'BG', (1, 0): 'BB', (1, 1): 'BD'}


def direction_max_voisin(matrice, ligne, colonne):
    """retourne la liste des directions qui permettent d'aller vers la case voisine de 
       la case (ligne,colonne) la plus grande. Le résultat doit aussi contenir la 
       direction qui permet de se rapprocher du milieu de la matrice
       si ligne,colonne n'est pas le milieu de la matrice

    Args:
        matrice (dict): une matrice
        ligne (int): le numéro de la ligne de la case considérée
        colonne (int): le numéro de la colonne de la case considérée

    Returns:
        list: une liste de chaines de deux lettres indiquant les directions des max et du milieu
                                                 DD -> droite , HD -> Haut Droite,
                                                 HH -> Haut, HG -> Haut gauche,
                                                 GG -> Gauche, BG -> Bas Gauche, BB -> Bas
    """
    res=[]
    maxi=None
    for l,c in DICO_DIR.keys():
        if maxi==None or maxi<=get_val(matrice,ligne+l,colonne+c):
            if maxi==get_val(matrice,ligne+l,colonne+c):
                res.append(DICO_DIR[(l,c)])
            else:    
                maxi=get_val(matrice,ligne+l,colonne+c)
                res=[DICO_DIR[(l,c)]]
    for l,c in DICO_DIR.keys():
        if (ligne+l,colonne+c)==(matrice["lignes"]//2,matrice["colonnes"]//2):
            res.append(DICO_DIR[(l,c)])
    return res
