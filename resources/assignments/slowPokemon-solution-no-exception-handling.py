# -------------------------------------------------
#        Name: R. JORDAN CROUSER
#    Filename: slowPokemon-solution.py
#        Date: 14 NOVEMBER 2018
#
# Description: Slow Pokeon Game - Sample Solution
#              (practice with classes / inheritance)
# -------------------------------------------------


from random import randint

class Pokemon:

    # Parent class constructor
    def __init__(self, name):
        self.name = name
        self.type = "NORMAL"
        self.max_hp = randint(10, 100)
        self.current_hp = self.max_hp
        self.defensive_power = randint(1,self.max_hp)
        self.attack_power = randint(1,self.max_hp)
        self.fainted = False
        self.revives_used = 0
        self.strengths = []
        self.weaknesses = []

    # Print a Pokemon's stats / info
    def printStats(self):
        print(self.name, "the", type(self).__name__, "now has the following stats:")
        print("     HP:", self.current_hp, "/", self.max_hp, end = "")
        if (self.fainted):
            print(" - FAINTED!")
        else:
            print()
        print(" Attack:", self.attack_power)
        print("Defense:", self.defensive_power)
        print()
        

    # Attack (call opponent's .defend() method)
    # Input: a reference to the opponent (class: Pokemon) being attacked
    def attack(self, opponent):
        print(self.name, "the", type(self).__name__, "attacks", opponent.name, "the", type(opponent).__name__)
        opponent.defend(self)

    # Defend (where the real work happens)
    # Input: a reference to the attacking opponent (class: Pokemon)
    def defend(self, opponent):

        # Determine base damage:
        #    opponent's attack power - 0.5*defender's defensive power
        #    minimum damage: 10
        damage = max([opponent.attack_power - 0.5*self.defensive_power, 10])

        # Determine bonus/penalty based on players' types
        if self.type in opponent.strengths:
            multiplier = 2.0
        elif self.type in opponent.weaknesses:
            multiplier = 0.5
        else:
            multiplier = 1.0

        # Apply damage
        self.current_hp -= int(multiplier * damage)

        # Check for faint
        if self.current_hp <= 0:
            self.current_hp = 0
            self.fainted = True

    def revive(self):
        
        # Check to see if pokemon can be revived, and if so, do it
        if (self.revives_used < 3):
            print("REVIVING", self.name, "the", type(self).__name__)
            self.current_hp = self.max_hp//2
            self.revives_used += 1
            self.fainted = False
            
            # Give warning if player is on their last revive
            if (self.revives_used == 3):
                print("CAUTION! NO REVIVES REMAINING")
        else:
            print("CANNOT REVIVE", self.name, "the", type(self).__name__)

# Child classes with modified type (and associated strengths / weaknesses)
# Note: strengths / weaknesses are restricted to the relevant types that
#       appear in this game, they are not complete listings
class Pikachu(Pokemon):

    def __init__(self, name):
        super().__init__(name)
        self.type = "ELECTRIC"
        self.strengths = ["WATER"]
        self.weaknesses = ["GRASS", "ELECTRIC"]

class Squirtle(Pokemon):

    def __init__(self, name):
        super().__init__(name)
        self.type = "WATER"
        self.strengths = ["FIRE"]
        self.weaknesses = ["WATER", "GRASS"]

class Bulbasaur(Pokemon):

    def __init__(self, name):
        super().__init__(name)
        self.type = "GRASS"
        self.strengths = ["WATER"]
        self.weaknesses = ["FIRE", "GRASS"]

class Charmander(Pokemon):

    def __init__(self, name):
        super().__init__(name)
        self.type = "FIRE"
        self.strengths = ["GRASS"]
        self.weaknesses = ["FIRE", "WATER"]


# Helper function to control gameplay loop
def battle(p1, p2):

    # As long as both players are still standing
    while (not p1.fainted and not p2.fainted):

        # Player 1 attacks, check Player 2's stats        
        p1.attack(p2)
        p2.printStats()
        if (p2.fainted):
            p2.revive()
        print("*******************")
            
        if (not p2.fainted):

            # Player 2 attacks back, check Player 1's stats
            p2.attack(p1)
            p1.printStats()
            if (p1.fainted):
                p1.revive()
            print("*******************")

    # Determine winner
    if p1.fainted:
        print(p2.name, "the", type(p2).__name__, "WINS!")
    else:
        print(p1.name, "the", type(p1).__name__, "WINS!")

        
def main():

    # Note: most students will not use .globals(), but will instead use
    #       a big conditional statement to create an instance of the
    #       appropriate subclass - that's fine
    possible_classes = globals()

    # Ask Player 1 to select their Pokemon
    p1_choice = input("Select your pokemon (Pikachu, Bulbasaur, Squirtle, Charmander): ").capitalize()
    
    # Instatiate P1's selected pokemon
    p1_class = possible_classes[p1_choice]
    p1 = p1_class(input("Give your pokemon a name: ").capitalize())
    print()
    p1.printStats()
    
    # Ask Player 2 to select their Pokemon
    p2_choice = input("Select your pokemon (Pikachu, Bulbasaur, Squirtle, Charmander): ").capitalize()
    
    # Instatiate P2's selected pokemon
    p2_class = possible_classes[p2_choice]
    p2 = p2_class(input("Give your pokemon a name: ").capitalize())
    print()
    p2.printStats()

    # Print battle banner
    print("*******************")
    print(p1.name, "the", type(p1).__name__)
    print("     ~VS~")
    print(p2.name, "the", type(p2).__name__)
    print("*******************")
    print()

    # Start battle
    battle(p1, p2)

if __name__ == "__main__":
    main()
