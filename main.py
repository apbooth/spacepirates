from random import randint

#set up player and enemy ships vars

player_captain_name = "Zolt"
player_ship_health = 100
player_ship_ammo = {'laser': 25,
                    'cannon': 5 }
player_ship_shields = False
player_ship_loot = 25
player_ship_morale = randint(75, 100)


cargo_ship_health = 100
cargo_ship_ammo = {'laser': 50,
                    'cannon': 2}
cargo_ship_health_shields = True
cargo_ship_content = randint(25, 100)


force_ship_health = 100
force_ship_ammo = {'laser': 50,
                    'cannon': 7}
force_ship_shields = True


#game areas
game_areas = [1, 2, 3]

#game state
game_state = True

def ships_status():
    print('You are captain {captain_name}\nYour ships health is {ships_health}%\nYou have {ships_ammo} rounds of ammo\nThe ships shields are at {ships_shields}%\nShips supplies are {ships_loot}% and morale is {ships_morale}%'.format(captain_name=player_captain_name,ships_health=player_ship_health, ships_ammo=player_ship_ammo, ships_shields=player_ship_shields, ships_loot=player_ship_loot, ships_morale=player_ship_morale ))


def battle(ship):
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

def reduce_ammo(ship, weapon_used):
    if ship == 'pirate':
        if weapon_used  == 1:
            player_ship_ammo['laser'] -= 1
        if weapon_used == 2:
            player_ship_ammo['cannon'] -= 1
    if ship == 'cargo':
        if weapon_used  == 1:
            cargo_ship_ammo['laser'] -= 1
        if weapon_used == 2:
            cargo_ship_ammo['cannon'] -= 1


def select_weapon(ship):
    if ship == 'pirate':
        i = 1
        for weapon, number in player_ship_ammo.items():
            if number > 0:
                print('Press {i} to fire {weapon} {number} shots left..\n'.format(number=number, weapon=weapon, i=i))
                i += 1
            # else:
            #     print('You have no weapons')
            #     return 0
        weapon_choice = int(input("\nenter weapon choice: "))
        while weapon_choice > i:
            weapon_choice = int(input("\nenter weapon choice: "))
        return weapon_choice
        
    if ship == 'cargo':
        i = 0
        for weapon, number in player_ship_ammo.items():
                    if number > 0:
                        i += 1
                    else:
                        return 0 
        return randint(0, i) 

def ship_health(ship):
    if ship > 0:
        return True

def cargo_ship_surrender():
    #create random choice for cargo ship to surrender
    number = randint(0, 2)
    if cargo_ship_health < 20 and number == 0:
        return True
    return False


def looting(cargo, player):
    print("\nCrew: ...Captian, we have boarded the cargo ship and found {amount} space coins, Transfering to our ship...\n".format(amount=cargo))
    player += cargo
    cargo = 0    
    print("\n...We now have {total_amount} in loot, captain...\n".format(total_amount=player))


ships_status()

surrender = False
while game_state == True:
    choose_area = int(input('Please enter which area of space to patrol, {game_areas}: '.format(game_areas=game_areas)))
    print(choose_area)
    if choose_area == 1:
        print("..Navigator: Now entering zone one, Captain..\n")
        print("..Tatical Officer: Captain, sensors have detected a ship approaching...\nit's a cargo ship..\n")
        #check player and enemy has health to continue with game
        while ship_health(player_ship_health) and ship_health(cargo_ship_health) and not surrender:

            if player_ship_ammo['laser'] > 0 or player_ship_ammo['cannon'] > 0:
                weapon_used = select_weapon("pirate")
                player_attack = battle('pirate')
                reduce_ammo("pirate", weapon_used)
                cargo_ship_health -= player_attack
                print("\nWeapons operator: We have inflicted {damage}% damage to the cargo ship, Captain..\n".format(damage=player_attack))
            else:
                print("weapons operator: Captian, we have run out of Ammunition..\n")
                game_state = False
            
            if not cargo_ship_surrender():
                if ship_health(cargo_ship_health):
                    cargo_ship_attack = battle('cargo')
                    player_ship_health -= cargo_ship_attack
                    print("Tatical officer: Incoming fire..\n")
                    print("Tatical officer: We have received {damage}% damage. You ship is at {health}%..\n".format(damage=cargo_ship_attack, health=player_ship_health))
            else:
                surrender = True
                print("comunications officer: Captain incoming radio message...\nCargo ship is surrendering..\nPreparing to board the cargo ship...")
                looting(cargo_ship_content, player_ship_loot)
                game_state = False
    #check if any ship has been destroyed and announce winner
    if player_ship_health <= 0:
        print("Game over your ship has been destroyed!!!")
        game_state = False
    elif cargo_ship_health <= 0:
        print("You have won!, enemyship has been destroyed")
        game_state = False

