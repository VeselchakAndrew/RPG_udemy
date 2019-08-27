from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# magic
# Create Black Magic
fire = Spell('Fire', 10, 150, "black")
thunder = Spell('Thunder', 12, 170, "black")
blizzard = Spell('Blizzard', 15, 200, "black")
meteor = Spell('Meteor', 20, 250, "black")
quake = Spell('Quake', 8, 120, "black")

# Create White Magic
cure = Spell('Cure', 10, 150, "white")
cura = Spell('Cura', 18, 250, "white")

#Items
potion = Item("Potion", "potion", "Restore 50HP", 50)
hipotion = Item("Hi-Potion", "hipotion", "Restore 100HP", 100)
superpotion = Item("SuperPotion", "superpotion", "Restore 200HP", 200)
elixir = Item("Elixir", "elixir", "Fully restore HP/MP for one member of party", 9999)
hielixir = Item("HiElixir", "hielixir", "Fully restore HP/MP for all members of party", 9999)

grenade = Item("Grenade", "attack", "Deal 500HP damage", 500)

player_spell = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_item = [potion, hipotion, superpotion, elixir, hielixir, grenade]
# Initiate Players
player = Person(460, 65, 60, 34, player_spell, player_item)
enemy = Person(1200, 64, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!!!" + bcolors.ENDC)

while running:
    print('=' * 50)
    player.choose_action()
    choice = int(input('Choice action: ')) - 1

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attacked for {bcolors.FAIL}{bcolors.BOLD}{dmg}{bcolors.ENDC} points of damage. Enemy HP: {enemy.get_hp()}')

    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input('Choice magic: ')) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_magic_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.ENDC)
            continue

        if spell.school == "white":
            player.heal(magic_dmg)
            print(f'{spell.name} heal you for {bcolors.OKGREEN}{magic_dmg}{bcolors.ENDC} HP')

        elif spell.school == "black":
            enemy.take_damage(magic_dmg)
            print(f"{bcolors.OKBLUE} \n{spell.name}  deals {magic_dmg} points of damage {bcolors.ENDC}")

    elif choice == 2:
        player.choose_item()
        print('Type 0 to exit')
        item_choice = int(input('Choose Item: ')) - 1

        if item_choice == -1:
            continue

        item = player_item[item_choice]

        if item.type == 'potion':
            player.heal(item.prop)
            print(f"{bcolors.OKBLUE} \n{item.name} heal {item.prop}HP. You HP: {player.get_hp()} {bcolors.ENDC}")



        

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f'Enemy attacks for {bcolors.FAIL}{bcolors.BOLD}{enemy_dmg}{bcolors.ENDC} points of damage. Your HP: {player.get_hp()}')

    print('-' * 50)
    print(f'Enemy HP: {bcolors.FAIL}{enemy.get_hp()} / {enemy.get_max_hp()}{bcolors.ENDC}\n')

    print(f'Your HP: {bcolors.OKGREEN}{player.get_hp()} / {player.get_max_hp()}{bcolors.ENDC}')
    print(f'Your MP: {bcolors.OKBLUE}{player.get_mp()} / {player.get_max_mp()}{bcolors.ENDC}')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!!!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Loose the battle" + bcolors.ENDC)
        running = False
