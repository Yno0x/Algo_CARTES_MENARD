from carte import crystal,monster_Raptor,blast_flames,monster_Kargath,monster_Primus_Kargath,blast_warrior
from mage import sorcerer

class carte:
    def __init__(self,nom,mana_cost,description,effet):
        self.nom = nom
        self.cout = mana_cost
        self.description = description
        self.effet = effet

class Mage:
    def __init__(self,nom,HP,mana_total,main,cimetiere,playground):
        self.nom = nom
        self.hp = HP
        self.total_de_mana = mana_total
        self.main = main
        self.cimetiere = cimetiere
        self.playground = playground
        mana = mana_total


