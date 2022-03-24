from pygame import surface
import plateau
import trojan
import case
import equipement
import protection
import pygame
import os


class affichage_case(object):
    def __init__(self, la_case, titre="CyberAttack@IUT'O Affichage case", couleur=(209, 238, 238), prefixe_image="./images") -> None:
        super().__init__()
        self.messageInfo = None
        self.imgInfo = None
        self.case = la_case
        self.fini = False
        self.couleur_texte = couleur
        self.taille = 5
        self.titre = titre
        self.charger_images(prefixe_image)
        pygame.init()
        pygame.display.set_mode(
            (1500, 1500), pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.dimensions_aff = pygame.display.get_window_size()
        self.taille_utile = min(self.dimensions_aff)
        pygame.display.set_caption(titre)
        self.calculer_tailles()
        pygame.display.set_icon(self.icone)

    def charger_images(self, prefixe_image):
        self.images_trojan = {}
        self.images_cases = {}
        self.images_avatars = {}
        self.icone=pygame.image.load(os.path.join(prefixe_image + "/","logo_cyber_attack.png"))
        for i in range(1, 5):
            s = pygame.image.load(os.path.join(
                prefixe_image + "/", "pion"+str(i)+".png"))
            self.images_trojan[i] = s
            self.images_cases[i] = pygame.image.load(
                os.path.join(prefixe_image + "/", "case"+str(i)+".png"))
            self.images_avatars[i] = pygame.image.load(
                os.path.join(prefixe_image + "/", "joueur"+str(i)+".png"))
        self.images_serveurs = {}
        for i in range(5):
            self.images_serveurs[i] = pygame.image.load(
                os.path.join(prefixe_image + "/", "serveur"+str(i)+".png"))
        self.images_ordis = {}
        for i in range(2):
            self.images_ordis[i] = pygame.image.load(
                os.path.join(prefixe_image + "/", "ordi"+str(i)+".png"))

        self.images_protections = {}
        self.images_protections[protection.DPO] = [pygame.image.load(os.path.join(prefixe_image + "/", "dpo0.png")),
                                                   pygame.image.load(os.path.join(prefixe_image + "/", "dpo1.png"))]
        self.images_protections[protection.FIREWALL_BDHG] = [pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bdhg0.png")),
                                                             pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bdhg1.png"))]
        self.images_protections[protection.FIREWALL_BGHD] = [pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bghd0.png")),
                                                             pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bghd1.png"))]
        self.images_protections[protection.DONNEES_PERSONNELLES] = [pygame.image.load(os.path.join(prefixe_image + "/", "donnees_perso0.png")),
                                                                    pygame.image.load(os.path.join(prefixe_image + "/", "donnees_perso1.png"))]
        self.images_protections[protection.ANTIVIRUS] = [pygame.image.load(os.path.join(prefixe_image + "/", "antivirus0.png")),
                                                         pygame.image.load(os.path.join(prefixe_image + "/", "antivirus1.png"))]
        self.image_fleche_case = pygame.image.load(
            os.path.join(prefixe_image + "/", "fleche_case.png"))

    def surface_trojan(self, le_trojan):
        createur = trojan.get_createur(le_trojan)
        direction = trojan.get_direction(le_trojan)
        surf_trojan = self.images_trojan_ajustees[createur]
        if direction == 'B':
            surf_trojan = pygame.transform.rotate(surf_trojan, 180)
        elif direction == 'D':
            surf_trojan = pygame.transform.rotate(surf_trojan, -90)
        elif direction == 'G':
            surf_trojan = pygame.transform.rotate(surf_trojan, 90)
        return surf_trojan

    def trojan_case(self, surf_case, la_case):
        nb_par_dir = {'B': 0, 'H': 0, 'D': 0, 'G': 0}
        for un_trojan in case.get_trojans(la_case):
            dir = trojan.get_direction(un_trojan)
            if dir == 'B':
                surf_case.blit(self.surface_trojan(
                    un_trojan), (nb_par_dir['B']*self.taille_trojan, 0))
            elif dir == 'H':
                surf_case.blit(self.surface_trojan(
                    un_trojan), (nb_par_dir['H']*self.taille_trojan, self.taille_trojan*2))
            elif dir == 'D':
                surf_case.blit(self.surface_trojan(
                    un_trojan), (0, nb_par_dir['D']*self.taille_trojan))
            elif dir == 'G':
                surf_case.blit(self.surface_trojan(
                    un_trojan), (self.taille_trojan*2, nb_par_dir['G']*self.taille_trojan))
            else:
                print("affiche_case: problème direction trojan")
            nb_par_dir[dir] += 1

    def surface_case(self, la_case, id_joueur, pas=0):
        surf_case = pygame.Surface((self.taille_case, self.taille_case))
        surf_case.blit(self.images_cases_ajustees[id_joueur], (0, 0))
        fleche = case.get_fleche(la_case)

        le_serveur = case.get_serveur(la_case)
        if le_serveur != None:
            niv_protection = equipement.get_resistance(le_serveur)
            surf_serveur = self.images_serveurs_ajustees[niv_protection]
            surf_case.blit(surf_serveur, (0, 0))
        if fleche == 'H':
            surf_fleche = self.image_fleche_case_ajustee
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'B':
            surf_fleche = self.image_fleche_case_ajustee
            surf_fleche = pygame.transform.rotate(surf_fleche, 180)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'G':
            surf_fleche = self.image_fleche_case_ajustee
            surf_fleche = pygame.transform.rotate(surf_fleche, 90)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'D':
            surf_fleche = self.image_fleche_case_ajustee
            surf_fleche = pygame.transform.rotate(surf_fleche, -90)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))

        la_protection = case.get_protection(la_case)
        if la_protection != None:
            type_protection = protection.get_type(la_protection)
            resistance = protection.get_resistance(la_protection)
            surf_protection = self.images_protections_ajustees[type_protection][resistance-1]
            surf_case.blit(surf_protection,
                           (self.taille_case//6, self.taille_case//6))

        if case.contient_avatar(la_case):
            surf_case.blit(
                self.images_avatars_ajustees[id_joueur], (self.taille_case//6, self.taille_case//6))

        return surf_case

    def mise_a_echelle(self, dico, dim):
        res = {}
        for cle, valeur in dico.items():
            if type(valeur) == list:
                nouv_list_img = []
                for img in valeur:
                    nouv_list_img.append(
                        pygame.transform.smoothscale(img, dim))
                res[cle] = nouv_list_img
            else:
                res[cle] = pygame.transform.smoothscale(valeur, dim)
        return res

    def calculer_tailles(self, pas=0):
        self.surface = pygame.display.get_surface()
        self.dimensions_aff = pygame.display.get_window_size()
        self.taille_utile = min(self.dimensions_aff)
        self.marge = self.taille_utile//8
        self.taille_plateau = 2*(self.taille_utile-2*self.marge)
        self.taille_case = self.taille_plateau //4
        self.taille_trojan = self.taille_case//3
        self.taille_font = self.marge//2
        self.images_serveurs_ajustees = self.mise_a_echelle(
            self.images_serveurs, (self.taille_case, self.taille_case))
        self.images_avatars_ajustees = self.mise_a_echelle(
            self.images_avatars, (2*self.taille_case//3, 2*self.taille_case//3))
        self.images_cases_ajustees = self.mise_a_echelle(
            self.images_cases, (self.taille_case, self.taille_case))
        self.images_ordis_ajustees = self.mise_a_echelle(
            self.images_ordis, (self.taille_case//2, self.taille_case//2))
        self.images_protections_ajustees = self.mise_a_echelle(
            self.images_protections, (2*self.taille_case//3, 2*self.taille_case//3))
        self.images_trojan_ajustees = self.mise_a_echelle(
            self.images_trojan, (self.taille_trojan, self.taille_trojan))
        self.image_fleche_case_ajustee = pygame.transform.smoothscale(
            self.image_fleche_case, (self.taille_case//2, self.taille_case//2))
        self.font = pygame.font.Font(None, self.taille_font)

    def dessiner_case(self, la_case):
        texte = self.font.render('Trojans entrants', True, (255, 0, 0))
        res = pygame.Surface((2*self.taille_case, self.taille_case+self.marge))
        res.blit(texte, (0, 0))
        x=y=0
        for un_trojan in case.get_trojans_entrants(la_case):
            res.blit(self.surface_trojan(un_trojan),(x*self.taille_trojan,self.taille_font+2+y*self.taille_trojan))
            x+=1
            if x>2:
                x=0
                y+=1
        surf_case = self.surface_case(la_case, 1)
        self.trojan_case(surf_case, la_case)
        res.blit(surf_case, (self.taille_case, 0))
        return res

    def afficher_case(self):
        self.surface.blit(self.dessiner_case(
            self.case), (self.marge, self.marge))
        pygame.display.flip()

    def demarrer(self):
        """
        démarre l'environnement graphique et la boucle d'écoute des événements
        """
        pygame.time.set_timer(pygame.USEREVENT + 1, 400)

        while (True):
            ev = pygame.event.wait()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(
                    ev.size, pygame.RESIZABLE | pygame.DOUBLEBUF)
                self.calculer_tailles()
                self.afficher_case()


if __name__ == '__main__':
    print("Bienvenue dans le jeu CyberAttack@IUT'O")

    # # configuration de la case à afficher
    # # décommentez/modifiez les lignes qui vous intéressent
    liste_trojans=[]
    les_directions=' BDGH'
    # # créer une liste de 3 trojans à mettre sur la case
    # for i in range(1,4):
    #     liste_trojans.append(trojan.creer_trojan(i,2,les_directions[i]))
    # # créer une protection à mettre sur la case
    # la_protection=protection.creer_protection(2, 2)
    # # créer un serveur à mettre sur la case
    # le_serveur=equipement.creer_equipement(equipement.SERVEUR,3)
    # création de la case (vous pouvez remplacer les None par la protection et le serveur)
    la_case = case.creer_case('D', None, None, liste_trojans)
    # # ajoute l'avatar sur la case! Attention cela doit supprimer tous les trojans se trouvant sur la case
    # case.poser_avatar(la_case)
    # # ajoute 3 trojans dans les trojans entrants de la case
    # for i in range(1,5):
    #     case.ajouter_trojan(la_case,trojan.creer_trojan(i,2,les_directions[i]))
    # # effectue une mise à jour de la case (transfert des trojans arrivants vers les trojans présents)
    # case.mettre_a_jour_case(la_case)
    # fin de la configuration
    ag = affichage_case(la_case, prefixe_image="./images")
    ag.demarrer()
    pygame.quit()
