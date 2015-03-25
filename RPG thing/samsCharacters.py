# RPG Character class
# Authors: Sam Coon
# Wizard and Cleric for group character creation


import baseClass, random

class Wizard(baseClass.Base):
    def __init__(self):
        super(Wizard).__init__(self)
        self.spells = []
        self.spellBook = []
        self.dailylimit = 0
        
        
class Cleric(baseClass.Base):
    def __init__(self):
        super(Cleric).__init__(self)
        self.base_spells = []
        self.deity = ""
        self.domains = []
        self.dailyLimit = 0

class charCreate(object):
    def __init__(self, points = 20, skillMod = ""):
        self.points = points
        
    def Create(self):
        addPoints = ""
        self.name = input("What's your character's name? ")
        self.dex = 10
        self.str = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10
        self.base_items = []
        
        # Skill Assignment
        while self.points != 0:
            print("-------------------------")
            print("Dexterity:", self.dex)
            print("Strength:", self.str)
            print("Constitution:", self.con)
            print("Intelligence:", self.int)
            print("Wisdom:", self.wis)
            print("Charisma:", self.cha)
            print("\nPoints:", self.points)
            print("-------------------------")

            skillMod = input("\nAdd or subtract points(+/-)? ")

            # Add Skill points 
            if skillMod == "+":
                skillChoice = input("\nChoose the skill to add to(Dex/Str/Con/Int/Wis/Cha): ")

                #Adding points to Dexterity
                if skillChoice == "Dex":
                    while addPoints != "n":
                        addpoints = input("\nEnter (+) to add a point enter (n) to stop: ")
                    # Subtracting point values
                        if addpoints == "+":
                            self.dex += 1
                            if self.dex <= 13:
                                self.points -= 1
                                print(self.points)

                            elif self.dex == 14 or self.dex == 15:
                                self.points -= 2

                            elif self.dex == 16 or self.dex == 17:
                                self.points -= 3

                            elif self.dex == 18:
                                self.points -= 4

                            else:
                                print("
                # Adding points to Strength    
                elif skillChoice == "Str":
                    amount = int(input("How many points do you want to put into Str ? "))
                    self.str += amount
                    
                    # Subtracting point values
                    if self.str <= 13:
                        points -= amount

                    elif self.str == 14:
                        points -= 5

                    elif self.str == 15:
                        points -= 7

                    elif self.str == 16:
                        points -= 10

                    elif self.str == 17:
                        points -= 13

                    elif self.str == 18:
                        points -= 17

                    else:
                        print("Sorry not enough points for that.")
                    
                # Adding points to Constitution
                elif skillChoice == "Con":
                    amount = int(input("How many points do you want to put into Con? "))
                    self.con += amount
                    
                    # Subtracting point values
                    if self.con <= 13:
                        points -= amount

                    elif self.con == 14:
                        points -= 5

                    elif self.con == 15:
                        points -= 7

                    elif self.con == 16:
                        points -= 10

                    elif self.con == 17:
                        points -= 13

                    elif self.con == 18:
                        points -= 17

                    else:
                        print("Sorry not enough points for that.")

                # Adding points to Intelligence
                elif skillChoice == "Int":
                    amount = int(input("How many points do you want to put into Int? "))
                    self.int += amount
                    
                    # Subtracting point values
                    if self.int <= 13:
                        points -= amount

                    elif self.int == 14:
                        points -= 5

                    elif self.int == 15:
                        points -= 7

                    elif self.int == 16:
                        points -= 10

                    elif self.int == 17:
                        points -= 13

                    elif self.int == 18:
                        points -= 17

                    else:
                        print("Sorry not enough points for that.")

                # Adding points to Wisdom
                elif skillChoice == "Wis":
                    amount = int(input("How many points do you want to put into Wis? "))
                    self.Wis += amount

                    # Subtracting point values
                    if self.wis <= 13:
                        points -= amount

                    elif self.wis == 14:
                        points -= 5

                    elif self.wis == 15:
                        points -= 7

                    elif self.wis == 16:
                        points -= 10

                    elif self.wis == 17:
                        points -= 13

                    elif self.wis == 18:
                        points -= 17

                    else:
                        print("Sorry not enough points for that.")

                #Adding points to Charisma
                elif skillChoice == "Cha":
                    amount = int(input("How many points do you want to put into Cha? "))
                    self.cha += amount

                    # Subtracting point values
                    if self.dex <= 13:
                        points -= amount

                    elif self.dex == 14:
                        points -= 5

                    elif self.dex == 15:
                        points -= 7

                    elif self.dex == 16:
                        points -= 10

                    elif self.dex == 17:
                        points -= 13

                    elif self.dex == 18:
                        points -= 17

                    else:
                        print("Sorry not enough points for that.")

            # Subtract skill points
            elif skillMod == "-":
                skillChoice = input("Choose the skill to sub to(Dex/Str/Con/Int/Wis/Cha): ")

                # Subtracting points from Dexterity
                if skillChoice == "Dex":
                    amount = int(input("How many points do you want to take from Dex? "))
                    self.dex += amount
                    points -= amount
                    print(points)
                    
                elif skillChoice == "Str":
                    amount = int(input("How many points do you want to take from Str ? "))
                    self.str -= amount
                    points += amount
                    print(points)

                elif skillChoice == "Con":
                    amount = int(input("How many points do you want to take from Con? "))
                    self.con -= amount
                    points += amount

                elif skillChoice == "Int":
                    amount = int(input("How many points do you want to take from Int? "))
                    self.int -= amount
                    points += amount

                elif skillChoice == "Wis":
                    amount = int(input("How many points do you want to take from into Wis? "))
                    self.Wis -= amount
                    points += amount

                elif skillChoice == "Cha":
                    amount = int(input("How many points do you want to take from Cha? "))
                    self.cha -= amount
                    points += amount
                    
        
def main():
    Creating = charCreate()
    Creating.Create()
    
main()
