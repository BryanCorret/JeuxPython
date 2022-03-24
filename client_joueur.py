# coding: utf-8
import argparse
import client
import jeu


if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu=le_client.prochaine_commande()
        if ok:
            # ICI REMPLACER PAR L'APPEL A VOTRE FONCTION D'IA
            actions_joueur=jeu.joueur_aleatoire(le_jeu,id_joueur)
            le_client.envoyer_commande_client( actions_joueur)
    le_client.afficher_msg("terminé")
