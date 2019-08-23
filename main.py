from classes.game import Person, bcolors

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 160},
         {'name': 'Water', 'cost': 15, 'dmg': 170},
         {'name': 'Earth', 'cost': 8, 'dmg': 155},
         {'name': 'Air', 'cost': 12, 'dmg': 165}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 64, 45, 25, magic)

running = True
i = 0

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + '\n' + spell + " deals", str(magic_dmg), 'points of damage' + bcolors.ENDC)


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
