import random
from .magic import Spell


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
    def __init__(self, hp, mp, attk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attkl = attk - 10
        self.attkh = attk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ['Attack', 'Magic', 'Item']

    # нанесение урона
    def generate_damage(self):
        return random.randrange(self.attkl, self.attkh)

    # принятие урона
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # лечение
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    # количество жизни
    def get_hp(self):
        return self.hp

    # максимальное количество жизни
    def get_max_hp(self):
        return self.maxhp

    # количество магии
    def get_mp(self):
        return self.mp

    # максимальное количество магии
    def get_max_mp(self):
        return self.maxmp

    # уменьшение магии при заклинаниях
    def reduce_mp(self, cost):
        self.mp -= cost

    # выбор действия
    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'ACTION' + bcolors.ENDC)
        for item in self.action:
            print(f'\t{i}. {item}')
            i += 1

    # выбор магии
    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'MAGIC:' + bcolors.ENDC)
        for spell in self.magic:
            if spell.school == 'black':
                print(f'\t{i}: {spell.name} (cost: {spell.cost}, damage: {spell.dmg})')
            else:
                print(f'\t{i}: {spell.name} (cost: {spell.cost}, heal: {spell.dmg})')

            i += 1

    # выбор предмета
    def choose_item(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'ITEM:' + bcolors.ENDC)
        for item in self.items:
            print(f'\t{i}: {item.name}, {item.description}, 5x')
            i += 1
