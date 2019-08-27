import random

class Spell:
    def __init__(self, name, cost, dmg, school):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.school = school

    def generate_magic_damage(self):
        low = self.dmg - 15
        hi = self.dmg + 15
        magic_damage = random.randrange(low, hi)
        return magic_damage
