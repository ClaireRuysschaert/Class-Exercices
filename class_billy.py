"""
Exercices de Classes

Le but de ces exercices est de créer des classes et leurs méthodes qui permettront à un Billy d'affronter un adversaire.
N'hésite pas à commit entre chaque exercice !
1) Crée un répertoire Exercices de classes sur GitHub
2) Initialise un répertoire comme répertoire git (git init)
3) Ajoute le répertoire de GitHub en remote (git remote add origin url)
4) Fais un premier commit avec ce fichier (git add puis git commit)

"""


"""
Exercice 1:
Crée une classe "Ennemi" qui aura ces attributs : Nom, Habilité, PV, Armure, Dégats.
"""

# Ton code ici
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
class Billy():
    def __init__(self, hability, endurance, skill, damages, armor):
        self.hability = hability
        self.endurance = endurance
        self.skill = skill
        self.damages = damages
        self.armor = armor

    def __str__(self) -> str:
        return f"Habilitiy = {self.hability}; Endurence = {self.endurance}; Skill = {self.skill}; Damages = {self.damages}, Armor = {self.armor} "

billy = Billy(10, 15, 5, 8, 4)
print(billy)

"""
Exercice 3:
Ajoute à la classe "Billy" une méthode "Combattre" qui prend en paramètre un objet de type "Ennemi".
Cette méthode affiche les différents lancers de dès, puis affiche le résultat de la bataille.

Note:
Cette méthode peut implémenter d'autre méthodes qui permettront de calculer les dégats infligés, 
d'afficher les PV restants de chacun des participants, etc. (N'hésite pas à casser le problème en morceaux !)
"""

# Ton code ici


"""Pour les exercices suivants, tu vas devoir modifier ta classe Billy"""
"""
Exercice 4:
Crée d'abord une classe "Arme" qui aura ces attributs : Nom, Dégats.
Ajoute à Billy un attribut "arme" qui sera un objet de type "Arme".
Cette nouvelle arme doit être prise en compte dans le calcul des dégats : il faut ajouter les dégats de l'arme à ceux de Billy.
"""

"""
Exercice 5:
Crée une classe "Armure" qui aura ces attributs : Nom, Armure.
Ajoute à Billy un attribut "armure" qui sera un objet de type "Armure".
Cette nouvelle armure doit être prise en compte dans le calcul des dégats : il faut ajouter les dégats de l'armure à ceux de Billy.
"""

"""
Exercice 6:
Ajoute à la classe "Billy" un attribut "Inventaire" qui sera un dictionnaire avec les clés "Arme" et "Armure".
Ajoute également à la classe "Billy" une méthode "AfficherInventaire" qui affiche le contenu de l'inventaire.
Enfin, ajoute à la classe "Billy" une méthode "AjouterArme" qui prend en paramètre un objet de type "Arme" et qui ajoute cette arme à l'inventaire.
Fait de même pour l'armure.
"""
