#        Name: Jordan Crouser
#    Filename: slowPokemon-answer.py
#        Date: 9 Nov 2018
# Description: Sample solution for A7: Slow Pokemon

from random import randint

class Pokemon:

    def __init__(self, name):
        self.name = name
        self.pokemon_type = "NORMAL"
        self.max_hp = randint(100,1000)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.max_hp)
        self.defensive_power = randint(1, self.max_hp)
        self.fainted = False

    def printStats(self):
        print(40*"*")
        print(self.name)
        self.pokemon_type = "NORMAL"
        self.max_hp = randint(100,1000)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.max_hp)
        self.defensive_power = randint(1, self.max_hp)
        self.fainted = False

def main():
    p1 = Pokemon("George")
    p1.printStats()

if __name__ == "__main__":
    main()
