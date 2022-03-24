import trojan
"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module trojan.py
    ce module gère les chevaux de Troie appelés Trojan"""


def creer_quatre_trojans():
    t1=trojan.creer_trojan(1,2,'G')
    t2=trojan.creer_trojan(2,0,'D')
    t3=trojan.creer_trojan(3,5,'H')
    t4=trojan.creer_trojan(4,1,'B')
    return t1,t2,t3,t4


def test_get_createur():
    t1,t2,t3,t4=creer_quatre_trojans()
    assert trojan.get_createur(t1)==1
    assert trojan.get_createur(t2)==2
    assert trojan.get_createur(t3)==3
    assert trojan.get_createur(t4)==4
    


def test_get_type():
    t1,t2,t3,t4=creer_quatre_trojans()
    assert trojan.get_type(t1)==2
    assert trojan.get_type(t2)==0
    assert trojan.get_type(t3)==5
    assert trojan.get_type(t4)==1

def test_get_direction():
    t1,t2,t3,t4=creer_quatre_trojans()
    assert trojan.get_direction(t1)=='G'
    assert trojan.get_direction(t2)=='D'
    assert trojan.get_direction(t3)=='H'
    assert trojan.get_direction(t4)=='B'


def test_set_createur():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.set_createur(t1,4)
    assert trojan.get_createur(t1)==4 and trojan.get_type(t1)==2 and trojan.get_direction(t1)=='G'
    trojan.set_createur(t2,3)
    assert trojan.get_createur(t2)==3 and trojan.get_type(t2)==0 and trojan.get_direction(t2)=='D'
    trojan.set_createur(t3,2)
    assert trojan.get_createur(t3)==2 and trojan.get_type(t3)==5 and trojan.get_direction(t3)=='H'
    trojan.set_createur(t4,1)
    assert trojan.get_createur(t4)==1 and trojan.get_type(t4)==1 and trojan.get_direction(t4)=='B'


    


def test_set_direction():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.set_direction(t1,'H')
    assert trojan.get_createur(t1)==1 and trojan.get_type(t1)==2 and trojan.get_direction(t1)=='H'
    trojan.set_direction(t2,'B')
    assert trojan.get_createur(t2)==2 and trojan.get_type(t2)==0 and trojan.get_direction(t2)=='B'
    trojan.set_direction(t3,'G')
    assert trojan.get_createur(t3)==3 and trojan.get_type(t3)==5 and trojan.get_direction(t3)=='G'
    trojan.set_direction(t4,'D')
    assert trojan.get_createur(t4)==4 and trojan.get_type(t4)==1 and trojan.get_direction(t4)=='D'


def test_set_type():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.set_type(t1,0)
    assert trojan.get_createur(t1)==1 and trojan.get_type(t1)==0 and trojan.get_direction(t1)=='G'
    trojan.set_type(t2,3)
    assert trojan.get_createur(t2)==2 and trojan.get_type(t2)==3 and trojan.get_direction(t2)=='D'
    trojan.set_type(t3,1)
    assert trojan.get_createur(t3)==3 and trojan.get_type(t3)==1 and trojan.get_direction(t3)=='H'
    trojan.set_type(t4,6)
    assert trojan.get_createur(t4)==4 and trojan.get_type(t4)==6 and trojan.get_direction(t4)=='B'

def test_inverser_direction():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.inverser_direction(t1)
    assert trojan.get_createur(t1)==1 and trojan.get_type(t1)==2 and trojan.get_direction(t1)=='D'
    trojan.inverser_direction(t2)
    assert trojan.get_createur(t2)==2 and trojan.get_type(t2)==0 and trojan.get_direction(t2)=='G'
    trojan.inverser_direction(t3)
    assert trojan.get_createur(t3)==3 and trojan.get_type(t3)==5 and trojan.get_direction(t3)=='B'
    trojan.inverser_direction(t4)
    assert trojan.get_createur(t4)==4 and trojan.get_type(t4)==1 and trojan.get_direction(t4)=='H'

def test_changer_direction_angle_bdhg():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.changer_direction_angle_bdhg(t1)
    assert trojan.get_createur(t1)==1 and trojan.get_type(t1)==2 and trojan.get_direction(t1)=='H'
    trojan.changer_direction_angle_bdhg(t2)
    assert trojan.get_createur(t2)==2 and trojan.get_type(t2)==0 and trojan.get_direction(t2)=='B'
    trojan.changer_direction_angle_bdhg(t3)
    assert trojan.get_createur(t3)==3 and trojan.get_type(t3)==5 and trojan.get_direction(t3)=='D'
    trojan.changer_direction_angle_bdhg(t4)
    assert trojan.get_createur(t4)==4 and trojan.get_type(t4)==1 and trojan.get_direction(t4)=='G'


def test_changer_direction_angle_bghd():
    t1,t2,t3,t4=creer_quatre_trojans()
    trojan.changer_direction_angle_bghd(t1)
    assert trojan.get_createur(t1)==1 and trojan.get_type(t1)==2 and trojan.get_direction(t1)=='B'
    trojan.changer_direction_angle_bghd(t2)
    assert trojan.get_createur(t2)==2 and trojan.get_type(t2)==0 and trojan.get_direction(t2)=='H'
    trojan.changer_direction_angle_bghd(t3)
    assert trojan.get_createur(t3)==3 and trojan.get_type(t3)==5 and trojan.get_direction(t3)=='G'
    trojan.changer_direction_angle_bghd(t4)
    assert trojan.get_createur(t4)==4 and trojan.get_type(t4)==1 and trojan.get_direction(t4)=='D'
