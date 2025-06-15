from random import randint

#set up player and enemy ships vars

player_captain_name = "Zolt"
player_ship_health = 90
player_ship_ammo = {'laser': 100,
                    'cannon': 25 }
player_ship_shields = 100
player_ship_supplies = 25
player_ship_morale = 100

first_main_enemy_name = "Space guard one"
first_main_enemy_health = 100
first_main_enemy_ammo = 100
first_main_enemy_shields = 100
first_main_enemy_content = 50

second_main_enemy_name = "Space guard two"
second_main_enemy_health = 90
second_main_enemy_ammo = 80
second_main_enemy_shields = 90
second_main_enemy_content = 30

third_main_enemy_name = "Space guard three"
third_main_enemy_health = 70
third_main_enemy_ammo = 60
third_main_enemy_shields = 40
third_main_enemy_content = 10

first_cargo_ship_name = "Cargo ship one"
first_cargo_ship_health = 100
first_cargo_ship_shields = 50
first_cargo_ship_ammo = 50
first_cargo_ship_cargo = 100

second_cargo_ship_name = "Cargo ship two"
second_cargo_ship_health = 100
second_cargo_ship_shields = 90
second_cargo_ship_ammo = 45
second_cargo_ship_cargo = 90

third_cargo_ship_name = "Cargo ship three"
third_cargo_ship_health = 100
third_cargo_ship_shields = 80
third_cargo_ship_ammo = 100
third_cargo_ship_cargo = 68

fourth_cargo_ship_name = "Cargo ship four"
fourth_cargo_ship_health = 100
fourth_cargo_ship_shields = 100
fourth_cargo_ship_ammo = 100
fourth_cargo_ship_cargo = 100

fith_cargo_ship_name = "Cargo ship five"
fith_cargo_ship_health = 100
fith_cargo_ship_shields = 50
fith_cargo_ship_ammo = 50
fith_cargo_ship_cargo = 100

#game areas
game_areas = [1, 2, 3]

#game state
game_state = True

def ships_status():
    print('You are captain {captain_name}\nYour ships health is {ships_health}%\nYou have {ships_ammo} rounds of ammo\nThe ships shields are at {ships_shields}%\nShips supplies are {ships_supplies}% and morale is {ships_morale}%'.format(captain_name=player_captain_name,ships_health=player_ship_health, ships_ammo=player_ship_ammo, ships_shields=player_ship_shields, ships_supplies=player_ship_supplies, ships_morale=player_ship_morale ))


def battle(ship):
    weapon_used = select_weapon(ship)
    min_damage = 0
    max_damage = 0
    if weapon_used != 0:
        if weapon_used == 1:
            min_damage = 0
            max_damage = 5
        if weapon_used == 2:
            min_damage = 5
            max_damage = 10
        return randint(min_damage, max_damage)
    else:
        return 0


def select_weapon(ship):
    if ship == 'pirate':
        i = 1
        for weapon, number in player_ship_ammo.items():
            if number > 0:
                print('To fire {weapon} {number} left, press {i} to fire'.format(number=number, weapon=weapon, i=i))
                i += 1
            else:
                print('You have no weapons')
                return 0
        weapon_choice = int(input("enter weapon choice"))
        return weapon_choice
    if ship == 'cargo':
        if first_cargo_ship_ammo > 0:

            return randint(1, 2)
        else:
            return 0  

def ship_health(ship):
    if ship > 0:
        return True

ships_status()

while game_state == True:
    choose_area = int(input('Please enter which area of space to patrol, {game_areas}: '.format(game_areas=game_areas)))
    print(choose_area)
    if choose_area == 1:
        print("You head into area 1\nIt isn't long before your ship's sensors detect another ship approaching...it's a cargo ship\n You order your crew to battle stations..")
        while ship_health(player_ship_health) and ship_health(first_cargo_ship_health):
            pirate_attack = battle('pirate')
            first_cargo_ship_health -= pirate_attack
            print('You have inflicted {damage}% damage to the cargo ship'.format(damage=pirate_attack))
            if ship_health(first_cargo_ship_health):
                first_cargo_ship_attack = battle('cargo')
                player_ship_health -= first_cargo_ship_attack
            print('You ship has received {damage}%. You ship is at {health}'.format(damage=first_cargo_ship_attack, health=player_ship_health))
            if player_ship_health <= 0:
                print("Your ship has been destroyed!!!")
                game_state = False

    elif choose_area == 2:        
        print("You head into area 2")
    elif choose_area == 3:
        print("You head into area 3")
    else:
        print('Invalid choice, please try again')

