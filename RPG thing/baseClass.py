# Brianna Melius, Zachary Golik, Tyler Kapusniak, Sam Coon, Andrew "Mad 
# Character/Monster base class
# 
# The base class to the monsters and characters
import characters, samsCharacters

class Base(object):
    """ The base class for any character/monster. """
    def __init__(self):
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.xp = xp
        self.level = level
        self.defense = 0
        self.dex = dexterity
        self.str = strength
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma
        self.AC = armor_class
        self.speed = speed
        self.CMD = CMD
        self.CMB = CMB
        self.Fort = fortitude
        self.Ref = reflex
        self.Will = will
        self.skills = skills
        self.melee = melee
        self.range = ranged
        """Ability Mods for armor class and stuff """
        self.str_Mod = __setmods(self.str)
        self.wis_Mod = __setmods(self.wis)
        self.int_Mod = __setmods(self.int)
        self.con_Mod = __setmods(self.con)
        self.dex_Mod = __setmods(self.dex)
        self.cha_Mod = __setmods(self.cha)

    def __setmods(self,attribute, character):
        modifier = 0
        people = character
        if attribute = 1 :
            addition = modifier -= 5
        if attribute = 2 or attribute = 3 :
            addition = modifier -= 4
        if attribute = 4 or attribute = 5 :
            addition = modifier -= 3
        if attribute = 6 or attribute = 7 :
            addition = modifier -= 2
        if attribute = 8 or attribute = 9 :
            addition = modifier -= 1
        if attribute = 12 or attribute = 13 :
            addition = modifier += 1
        if attribute = 14 or attribute = 15 :
            addition = modifier += 2
        if attribute = 16 or attribute = 17 :
            addition = modifier += 3
        if attribute = 18 or attribute = 19 :
            addition = modifier += 4
        if attribute = 20 or attribute = 21 :
            addition = modifier += 5
        if attribute = 22 or attribute = 23 :
            addition = modifier += 6
        if attribute = 24 or attribute = 25 :
            addition = modifier += 7
        if attribute = 26 or attribute = 27 :
            addition = modifier += 8
        if attribute = 28 or attribute = 29 :
            addition = modifier += 9
        if attribute = 30 or attribute = 31 :
            addition = modifier += 10
        if attribute = 32 or attribute = 33 :
            addition = modifier += 11
        if attribute = 34 or attribute = 35 :
            addition = modifier += 12
        if attribute = 36 or attribute = 37 :
            addition = modifier += 13
        if attribute = 38 or attribute = 39 :
            addition = modifier += 14
        if attribute = 40 or attribute = 41 :
            addition = modifier += 15
        if attribute = 42 or attribute = 43 :
            addition = modifier += 16

        if "Morningstar" in Cleric.inventory:
            
        return modifier
    
