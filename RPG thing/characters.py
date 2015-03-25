#Warrior and Thief Characters
#Done by Tyler Kapusniak
#Done on 3/9/15

import baseClass, random

    #Warrior Character
class Fighter(baseClass.Base):
    def __init__(self):
        ###Items to have for this character: Sword, Shield, and Chainmail
        self.base_hp = random.randint(1, 10)
        self.base_attack = random.randint(1, 10)
        self.xp = 0
        self.level = 1
        self.defence = 3
        self.dex = 13
        self.str = 16
        self.con = 16
        self.int = 8
        self.wis = 12
        self.cha = 10
        return self.base_hp, self.base_attack, self.xp, self.level, self.defence, self.dex, self.str, self.con, self.wis, self.cha, 

    #Thief Character
class Rogue(baseClass.Base):
    def __init__(self):
        ###Items to have for this ccharacter: Knife, Bow (short, long, or cross, doesn't matter), and Leather Armor
        self.base_hp = random.randint(1, 8)
        self.base_attack = random.randint(1, 6)
        self.xp = 0
        self.level = 1
        self.defence = 9
        self.dex = 17
        self.str = 10
        self.con = 14
        self.int = 14
        self.wis = 12
        self.cha = 8
        return self.base_hp, self.base_attack, self.xp, self.level, self.defence, self.dex, self.str, self.con, self.wis, self.cha,



    
