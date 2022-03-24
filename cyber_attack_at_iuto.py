from pygame import surface
import plateau
import jeu
import trojan
import case
import equipement
import protection
import pygame
import os


class cyber_attack_at_iuto(object):
    def __init__(self, le_jeu, titre="CyberAttack@IUT'O", couleur=(209, 238, 238), prefixe_image="./images") -> None:
        super().__init__()
        self.messageInfo = None
        self.imgInfo = None
        self.jeu = le_jeu
        self.fini = False
        self.couleur_texte = couleur
        self.taille_plateau = jeu.get_taille_plateau(le_jeu)
        self.titre = titre
        self.charger_images(prefixe_image)
        pygame.init()
        pygame.display.set_mode(
            (1500, 1500), pygame.RESIZABLE | pygame.DOUBLEBUF)
        pygame.display.set_icon(self.icone)
        self.dimensions_aff = pygame.display.get_window_size()
        self.taille_utile = min(self.dimensions_aff)
        pygame.display.set_caption(titre)
        self.calculer_tailles()


    def charger_images(self, prefixe_image):
        self.icone = pygame.image.load(os.path.join(prefixe_image + "/", "logo_cyber_attack.png"))
        self.images_trojan={}
        self.images_cases={}
        self.images_avatars={}
        for i in range(1, 5):
            s=pygame.image.load(os.path.join(
                prefixe_image + "/", "pion"+str(i)+".png"))
            self.images_trojan[i]=s
            self.images_cases[i]=pygame.image.load(
                os.path.join(prefixe_image + "/", "case"+str(i)+".png"))
            self.images_avatars[i]=pygame.image.load(
                os.path.join(prefixe_image + "/", "joueur"+str(i)+".png"))
        self.images_serveurs={}
        for i in range(5):
            self.images_serveurs[i]=pygame.image.load(
                os.path.join(prefixe_image + "/", "serveur"+str(i)+".png"))
        self.images_ordis={}
        for i in range(2):
            self.images_ordis[i]=pygame.image.load(
                os.path.join(prefixe_image + "/", "ordi"+str(i)+".png"))

        self.images_protections={}
        self.images_protections[protection.DPO]=[pygame.image.load(os.path.join(prefixe_image + "/", "dpo0.png")),
                                                 pygame.image.load(os.path.join(prefixe_image + "/", "dpo1.png"))]
        self.images_protections[protection.FIREWALL_BDHG]=[pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bdhg0.png")),
                                                 pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bdhg1.png"))]
        self.images_protections[protection.FIREWALL_BGHD]=[pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bghd0.png")),
                                                 pygame.image.load(os.path.join(prefixe_image + "/", "firewall_bghd1.png"))]
        self.images_protections[protection.DONNEES_PERSONNELLES]=[pygame.image.load(os.path.join(prefixe_image + "/", "donnees_perso0.png")),
                                                 pygame.image.load(os.path.join(prefixe_image + "/", "donnees_perso1.png"))]
        self.images_protections[protection.ANTIVIRUS]=[pygame.image.load(os.path.join(prefixe_image + "/", "antivirus0.png")),
                                                 pygame.image.load(os.path.join(prefixe_image + "/", "antivirus1.png"))]
        self.image_fleche_case=pygame.image.load(
            os.path.join(prefixe_image + "/", "fleche_case.png"))

    def surface_trojan(self, le_trojan):
        createur=trojan.get_createur(le_trojan)
        direction=trojan.get_direction(le_trojan)
        surf_trojan=self.images_trojan_ajustees[createur]
        if direction == 'B':
            surf_trojan=pygame.transform.rotate(surf_trojan, 180)
        elif direction == 'D':
            surf_trojan=pygame.transform.rotate(surf_trojan, -90)
        elif direction == 'G':
            surf_trojan=pygame.transform.rotate(surf_trojan, 90)
        return surf_trojan

    def trojan_case(self, surf_plateau, la_case, x, y, pas):
        nb_par_dir={'B': 0, 'H': 0, 'D': 0, 'G': 0}
        for un_trojan in case.get_trojans(la_case):
            dir=trojan.get_direction(un_trojan)
            if dir == 'B':
                surf_plateau.blit(self.surface_trojan(
                    un_trojan), (x+nb_par_dir['B']*self.taille_trojan, y+pas))
            elif dir == 'H':
                surf_plateau.blit(self.surface_trojan(
                    un_trojan), (x+nb_par_dir['H']*self.taille_trojan, y+self.taille_trojan*2-pas))
            elif dir == 'D':
                surf_plateau.blit(self.surface_trojan(
                    un_trojan), (x+pas, y+nb_par_dir['D']*self.taille_trojan))
            elif dir == 'G':
                surf_plateau.blit(self.surface_trojan(
                    un_trojan), (x+self.taille_trojan*2-pas, y+nb_par_dir['G']*self.taille_trojan))
            else:
                print("affiche_case: problème direction trojan")
            nb_par_dir[dir] += 1

    def surface_case(self, la_case, id_joueur, pas=0):
        surf_case=pygame.Surface((self.taille_case, self.taille_case))
        surf_case.blit(self.images_cases_ajustees[id_joueur], (0, 0))
        fleche=case.get_fleche(la_case)

        le_serveur=case.get_serveur(la_case)
        if le_serveur != None:
            niv_protection=equipement.get_resistance(le_serveur)
            surf_serveur=self.images_serveurs_ajustees[niv_protection//10]
            surf_case.blit(surf_serveur, (0, 0))
        if fleche == 'H':
            surf_fleche=self.image_fleche_case_ajustee
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'B':
            surf_fleche=self.image_fleche_case_ajustee
            surf_fleche=pygame.transform.rotate(surf_fleche, 180)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'G':
            surf_fleche=self.image_fleche_case_ajustee
            surf_fleche=pygame.transform.rotate(surf_fleche, 90)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))
        elif fleche == 'D':
            surf_fleche=self.image_fleche_case_ajustee
            surf_fleche=pygame.transform.rotate(surf_fleche, -90)
            surf_case.blit(
                surf_fleche, (self.taille_case//4, self.taille_case//4))

        la_protection=case.get_protection(la_case)
        if la_protection != None:
            type_protection=protection.get_type(la_protection)
            resistance=protection.get_resistance(la_protection)
            surf_protection=self.images_protections_ajustees[type_protection][resistance-1]
            surf_case.blit(surf_protection,
                           (self.taille_case//6, self.taille_case//6))
        if case.contient_avatar(la_case):
            surf_case.blit(
                self.images_avatars_ajustees[id_joueur], (self.taille_case//6, self.taille_case//6))

        return surf_case

    def mise_a_echelle(self, dico, dim):
        res={}
        for cle, valeur in dico.items():
            if type(valeur) == list:
                nouv_list_img=[]
                for img in valeur:
                    nouv_list_img.append(
                        pygame.transform.smoothscale(img, dim))
                res[cle]=nouv_list_img
            else:
                res[cle]=pygame.transform.smoothscale(valeur, dim)
        return res

    def calculer_tailles(self, pas=0):
        self.surface=pygame.display.get_surface()
        self.dimensions_aff=pygame.display.get_window_size()
        self.taille_utile=min(self.dimensions_aff)
        self.marge=self.taille_utile//16
        self.taille_plateau=(self.taille_utile-2*self.marge)//3
        self.taille_case=self.taille_plateau//jeu.get_taille_plateau(le_jeu)
        self.taille_trojan=self.taille_case//3
        self.taille_font=self.marge//2
        self.images_serveurs_ajustees=self.mise_a_echelle(
            self.images_serveurs, (self.taille_case, self.taille_case))
        self.images_avatars_ajustees=self.mise_a_echelle(
            self.images_avatars, (2*self.taille_case//3, 2*self.taille_case//3))
        self.images_cases_ajustees=self.mise_a_echelle(
            self.images_cases, (self.taille_case, self.taille_case))
        self.images_ordis_ajustees=self.mise_a_echelle(
            self.images_ordis, (self.taille_case//2, self.taille_case//2))
        self.images_protections_ajustees=self.mise_a_echelle(
            self.images_protections, (2*self.taille_case//3, 2*self.taille_case//3))
        self.images_trojan_ajustees=self.mise_a_echelle(
            self.images_trojan, (self.taille_trojan, self.taille_trojan))
        self.image_fleche_case_ajustee=pygame.transform.smoothscale(
            self.image_fleche_case, (self.taille_case//2, self.taille_case//2))
        self.font=pygame.font.Font(None, self.taille_font)


    def surface_communications(self, liste_trojans):
        surf_com=pygame.Surface((self.taille_case, self.taille_case))
        lin=2
        col=0
        for un_trojan in liste_trojans:
            surf_com.blit(self.surface_trojan(un_trojan),
                          (col*self.taille_trojan, lin*self.taille_trojan))
            col += 1
            if col > 2:
                col=0
                lin -= 1
        return surf_com

    def afficher_scores(self):
        for i in range(1, 5):
            nom_joueur=plateau.get_nom_joueur(jeu.get_plateau(self.jeu, i))
            score=plateau.get_points(jeu.get_plateau(self.jeu, i))
            texte=self.font.render(
                nom_joueur[:12].ljust(12), True, (255, 0, 0))
            self.surface.blit(texte, (self.taille_plateau+3*self.marge//2,
                              self.taille_plateau+self.marge+self.taille_font+i*2*self.taille_font))
            texte=self.font.render(str(score).rjust(8), True, (255, 0, 0))
            self.surface.blit(texte, (3*self.taille_plateau//2+self.marge,
                              self.taille_plateau+self.marge+self.taille_font+i*2*self.taille_font))

    def dessiner_plateau(self, le_plateau, pas=0):
        nom_joueur=plateau.get_nom_joueur(le_plateau)
        id_joueur=plateau.get_id_joueur(le_plateau)
        texte=self.font.render(nom_joueur[:12], True, (255, 0, 0))
        res=pygame.Surface(
            (self.taille_plateau, self.taille_case+self.marge+self.taille_plateau))
        res.blit(texte, ((self.taille_plateau-texte.get_width())//2,
                 self.taille_case+self.taille_plateau+self.marge//2))
        nb_ordis_restants=plateau.get_nb_ordis_restants(le_plateau)
        res.blit(self.surface_communications(
            plateau.get_trojans_entrants(le_plateau)), (self.taille_case, 0))
        sortants=plateau.get_trojans_sortants(le_plateau, 'H')
        for dir in 'DBG':
            sortants.extend(plateau.get_trojans_sortants(le_plateau, dir))
        res.blit(self.surface_communications(
            sortants), (3*self.taille_case, 0))
        for i in range(5):
            if i < nb_ordis_restants:
                res.blit(self.images_ordis_ajustees[1],
                        (i*self.taille_case//2, self.taille_case+self.taille_plateau))
            else:
                res.blit(self.images_ordis_ajustees[0],
                        (i*self.taille_case//2, self.taille_case+self.taille_plateau))

        for i in range(5):
            for j in range(5):
                res.blit(self.surface_case(plateau.get_case(le_plateau, i, j), id_joueur, pas), (
                    j*self.taille_case, (i+1)*self.taille_case, self.taille_case, self.taille_case))
        for i in range(5):
            for j in range(5):
                self.trojan_case(res, plateau.get_case(
                    le_plateau, i, j), j*self.taille_case, (i+1)*self.taille_case, pas)

        return res

    def afficher_jeu(self, pas=0):
        self.surface.fill((0, 0, 0))
        pos=[(self.marge+self.taille_plateau, self.marge+2*self.taille_plateau-self.taille_case),
        (self.marge+2*self.taille_plateau -
         self.taille_case, self.marge+self.taille_plateau),
        (self.marge+self.taille_plateau, 0), (0, self.marge+self.taille_plateau)]
        for i in range(4):
            res=self.dessiner_plateau(jeu.get_plateau(self.jeu, i+1), pas)
            res=pygame.transform.rotate(res, 90.*i)
            self.surface.blit(res, pos[i])
        self.afficher_scores()
        pygame.display.flip()

    def demarrer(self):
        """
        démarre l'environnement graphique et la boucle d'écoute des événements
        """
        pygame.time.set_timer(pygame.USEREVENT + 1, 400)
        # pygame.time.set_timer(pygame.USEREVENT + 2, 100)


        clock=pygame.time.Clock()
        action=0
        pas=self.taille_case//60
        nb_tours=0
        while (True):
            ev=pygame.event.wait()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(
                    ev.size, pygame.RESIZABLE | pygame.DOUBLEBUF)
                self.calculer_tailles()
                self.afficher_jeu()
            if ev.type == pygame.USEREVENT + 1:
                if jeu.est_fini(self.jeu):
                    print("terminé", nb_tours)
                    break
                if action == 0:
                    nb_tours += 1
                    jeu.actions_joueur(self.jeu)
                elif action == 1:
                    jeu.diriger_trojan(self.jeu)
                elif action == 2:
                    jeu.phase1(self.jeu)
                elif action == 3:
                    jeu.phase2(self.jeu)
                    pas=0
                action=(action+1) % 4
                self.afficher_jeu()
            if ev.type == pygame.USEREVENT + 2:
                if action < 3:
                    pas += self.taille_case//6
                    self.afficher_jeu(pas)
        input()



if __name__ == '__main__':
    print("Bienvenue dans le jeu trojan attack")
    print("Veuillez entrer la liste des joueurs")
    liste_joueurs=[]
    for id_joueur in range(1,5):
         nom=input("Nom du joueur "+str(id_joueur)+"? ")
         liste_joueurs.append(nom)
    le_jeu=jeu.creer_jeu(liste_joueurs, humain=False)
    ag=cyber_attack_at_iuto(le_jeu, prefixe_image="./images")
    ag.demarrer()
    pygame.quit()
