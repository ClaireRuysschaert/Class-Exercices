"""
Exercices de Classes

Le but de ces exercices est de créer des classes et leurs méthodes qui permettront à un Billy d'affronter un adversaire.
N'hésite pas à commit entre chaque exercice !
1) Crée un répertoire Exercices de classes sur GitHub
2) Initialise un répertoire comme répertoire git (git init)
3) Dire à git où envoyer le fichier modifié sur gitHub à distance (git remote add origin url)
4) Ajouter des changements = prépa du commit (= prendre la pose) (git add (ajouter) 
5) Faire le commit puis git commit (valider = appuyer sur le déclencheur)
6) Push un nouveau commit (git -> github) (git push (-u origin master si première fois) ou publish branch si pas de branche) 

"""


"""
Exercice 1:
Crée une classe "Ennemi" qui aura ces attributs : Nom, Habilité, PV, Armure, Dégats.
"""

# Ton code ici
import random


class Ennemi:
    def __init__(self, name, hability, PV, armor, damages):
        self.name = name
        self.hability = hability
        self.PV = PV
        self.armor = armor
        self.damages = damages

"""
Exercice 2:
Crée une classe "Billy" qui aura presque les mêmes attributs que le billy de ton livre. (Habilité, Endurance, Adresse, Dégats, Armure)
Cette classe dispose d'une méthode qui permet d'afficher un résumé au travers d'un print.
"""
# Ton code ici
 
class Weapon():
    def __init__(self, weapon_name, weapon_damages):
        self.weapon_name = weapon_name
        self.weapon_damages = weapon_damages

class Helmet():
    def __init__(self, helmet_name, helmet_protection):
        self.helmet_name = helmet_name
        self.helmet_protection  = helmet_protection
class Billy():
    def __init__(self, hability, PV, skill, damages, armor, weapon: Weapon, helmet: Helmet):
        self.hability = hability
        self.PV = PV
        self.skill = skill
        self.damages = damages
        self.armor = armor
        self.weapon = weapon
        self.helmet = helmet

    def __str__(self) -> str:
        return f"Habilitiy = {self.hability}; Endurence = {self.PV}; Skill = {self.skill}; Damages = {self.damages}, Armor = {self.armor}, Weapon = {self.weapon}"

    
    def fight(self, ennemi: Ennemi):
        # Le combat dure jusqu'à ce qu'un joueur n'ait plus de PV.
        while self.PV > 0 and ennemi.PV > 0:
            dice = random.randint(1,6)
            ratio = self.hability/ennemi.hability
            billy_damages = self.damages + self.weapon.weapon_damages + (dice*ratio) - ennemi.armor
            ennemi.PV -= billy_damages
            ennemi_damages = ennemi.damages + ((7-(dice*(1/ratio)))) - billy.armor - self.helmet.helmet_protection
            self.PV -= ennemi_damages
            print(f"\nBilly damages = {billy_damages}; ennemi PV left = {ennemi.PV}, \nEnnemi damages = {ennemi.damages}; billy PV left = {billy.PV}.\n")
            print(f"Billy attacks with {self.weapon.weapon_name} and wears {self.helmet.helmet_name}." )


"""
Exercice 3:
Ajoute à la classe "Billy" une méthode "Combattre" qui prend en paramètre un objet de type "Ennemi".
Cette méthode affiche les différents lancers de dès, puis affiche le résultat de la bataille.

Note:
Cette méthode peut implémenter d'autre méthodes qui permettront de calculer les dégats infligés, 
d'afficher les PV restants de chacun des participants, etc. (N'hésite pas à casser le problème en morceaux !)
"""
# Comparer l'habilité B/E
# Simuler un lancer de dé
# Multiplier le lancer de dès par le rapport de l'habilité = dégats 
# Ajouter ces dégats aux dégats du lancer de dès 
# Soustraire l'armure
# Retirer les dégats totaux des PV
# Afficher les résultats de chaque tour

# Ton code ici


"""Pour les exercices suivants, tu vas devoir modifier ta classe Billy"""
"""
Exercice 4:
Crée d'abord une classe "Arme" qui aura ces attributs : Nom, Dégats.
Ajoute à Billy un attribut "arme" qui sera un objet de type "Arme".
Cette nouvelle arme doit être prise en compte dans le calcul des dégats : il faut ajouter les dégats de l'arme à ceux de Billy.
"""

marjolaine = Weapon("marjolaine", 5)
bathing_cap = Helmet("Bathing cap", 1)
billy = Billy(hability=10, PV=15, skill=15, damages=2, armor=1, weapon=marjolaine, helmet=bathing_cap)
dwarf = Ennemi(name="Tyron", hability=8, PV=23, armor=12, damages=11)
billy.fight(dwarf)

"""
Exercice 5:
Crée une classe "Casque" qui aura ces attributs : Nom, casque.
Ajoute à Billy un attribut "casque" qui sera un objet de type "casque".
ce nouveau casque doit être pris en compte dans le calcul des dégats : il faut ajouter l'armure du casque à ceux de Billy.
"""

"""
Exercice 6:
Ajoute à la classe "Billy" un attribut "Inventaire" qui sera un dictionnaire avec les clés "Arme" et "Armure".
Ajoute également à la classe "Billy" une méthode "AfficherInventaire" qui affiche le contenu de l'inventaire.
Enfin, ajoute à la classe "Billy" une méthode "AjouterArme" qui prend en paramètre un objet de type "Arme" et qui ajoute cette arme à l'inventaire.
Fait de même pour l'armure.
"""
