from heartstun import Mage

class sorcerer(Mage):
    def __init__(self):
        Mage.__init__(self,"Sorcerer",30,1,["Raptor Rougefange","Choc de Flammes","La Pièce"],[],[])

class Warrior(Mage):
    def __init__(self):
        Mage.__init__(self,"Warrior",30,1,["kargath","tourbillon","La Pièce"],[],[])