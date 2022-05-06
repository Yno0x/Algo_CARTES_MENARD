from heartstun import carte

class crystal(carte):
    def __init__(self):
        carte.__init__(self,"La Pièce",0,"Une pièce décorée d'un crystal bleu luisant dans la nuit","Augmente votre mana de 1 tant que la carte est sur le terrain")


class monster_Raptor(carte):
    def __init__(self,HP,atk):
        carte.__init__(self,"Raptor Rougefange",2,"un raptor vivant dans les forêt et ayant appris a grimper au arbres pour chasser.","")
        self.hp=HP
        self.atk=atk

class blast_flames(carte):
    def __init__(self,damage):
        carte.__init__(self,"Choc de Flammes",7,"Des flammes ardentes balayant le terrain.","Inflige 4 point de dégat au joueur ou a toute les créatures")
        self.damage = damage


class monster_Kargath(carte):
    def __init__(self,HP4,atk4):
        carte.__init__(self,"Kargath Lamepoing",4,"un guerrier ayant appris a se battre, la lame au poing.","Place la carte Primus Kargath dans votre main")
        self.hp = HP4
        self.atk=atk4

class monster_Primus_Kargath(carte):
    def __init__(self,HP10,atk10):
        carte.__init__(self,"Primus Kargath",8,"Kargath a évolué technologiquement et s'est transformé en arme de destruction.","")
        self.hp = HP10
        self.atk = atk10

class blast_warrior(carte):
    def __init__(self,damage):
        carte.__init__(self,"toubillon",1,"Un tourbillon de lme tranchante","inflige 1 point de dégat a tout les adversaires")
        self.damage = damage