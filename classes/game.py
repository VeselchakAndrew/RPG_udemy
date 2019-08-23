import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, attk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attkl = attk - 10
        self.attkh = attk + 10
        self.df = df
        self.magic = magic
        self.action = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.attkl, self.attkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]['dmg'] - 5
        mgh = self.magic[i]['dmg'] + 5
        return random.randrange(mgl, mgh)

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'Action' + bcolors.ENDC)
        for item in self.action:
            print(str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'Magic' + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ':', spell['name'])
            i += 1
