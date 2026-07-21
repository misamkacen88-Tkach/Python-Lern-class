class Weapon:
    
    def attack(self):
        raise NotImplementedError

class Sword(Weapon):
    
    def attack(self):
        print("Slash!!!!")

class MagicStaff(Weapon):
    
    def attack(self):
        print("Bamg!!!!")
        
class Player:
    
    def __init__(self, weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()






plaeyr = Player(Sword())
plaeyr.attack()

plaeyr.weapon = MagicStaff()
plaeyr.attack()

