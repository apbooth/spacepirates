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
cargo_ship_content = randint(50, 100)

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
    if ship == 'galaxon':
        if weapon_used  == 1:
            cargo_ship_ammo['laser'] -= 1
        if weapon_used == 2:
            cargo_ship_ammo['cannon'] -= 1


def select_weapon(ship):
    if ship == 'pirate':
        i = 0
        for weapon, number in player_ship_ammo.items():
            if number > 0:
                print('Press {i} to fire {weapon} {number} shots left..\n'.format(number=number, weapon=weapon, i=i+1))
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
        for weapon, number in cargo_ship_ammo.items():
                    if number > 0:
                        i += 1 
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

def player_surrender():
    if player_ship_health < 15:
        print("...Communications officer: Captain, receiving message...\n...The Galaxons are telling us to surrender...\n...what should I reply?...")
        reply = int(input("To surrender press 1 to fight on press 2"))
        while reply != 1 or reply != 2:
            reply = int(input("To surrender press 1 to fight on press 2"))
        if reply == 1:
            return True
        if reply == 2:
            return False

def looting(cargo, player):    
    print("\n...Crew: Captain, we have boarded the cargo ship and found {amount} space coins, Transfering to our ship..".format(amount=cargo))
    player += cargo
    cargo = 0    
    print("We now have {total_amount} space coins in the ships loot, captain...\n".format(total_amount=player))


ships_status()

cargo_surrender = False
player_surrender = False

while game_state == True:
    
    print("..Navigator: Now entering zone one, Captain..\n")
    print("..Tatical Officer: Captain, sensors have detected a ship approaching...\nit's a cargo ship..\n")

    while ship_health(player_ship_health) and not player_surrender and not cargo_surrender:

        if player_ship_ammo['laser'] > 0 or player_ship_ammo['cannon'] > 0:
            weapon_used = select_weapon("pirate")
            player_attack = battle('pirate')
            reduce_ammo("pirate", weapon_used)
            cargo_ship_health -= player_attack
            print("\nWeapons operator: We have inflicted {damage}% damage to the cargo ship, Captain..\n".format(damage=player_attack))
        else:
            print("weapons operator: Captain, we have run out of Ammunition..\n")
            player_surrender = True
            game_state = False
        
        if not cargo_ship_surrender() and not player_surrender:
            if ship_health(cargo_ship_health):
                weapon_used = select_weapon('cargo')
                cargo_ship_attack = battle('cargo')
                reduce_ammo("cargo", weapon_used)
                player_ship_health -= cargo_ship_attack
                print("Tatical officer: Incoming fire..\n")
                print("Tatical officer: We have received {damage}% damage. You ship is at {health}%..\n".format(damage=cargo_ship_attack, health=player_ship_health))
            else:
                print("...Tatical officer: Captain the cargo ship has been destroyed, no loot this time...")
                game_state = False
        
        else:
            cargo_surrender = True
            print("...Comunications officer: Captain incoming radio message...\nCargo ship is surrendering..\nPreparing to board the cargo ship...\n")
            looting(cargo_ship_content, player_ship_loot)
            game_state = False

        
    #check if player ship has been destroyed
    if player_ship_health <= 0:
        print("Game over your ship has been destroyed!!!")
        game_state = False
    elif cargo_surrender:
        print("Congratulations you got the loot and have won the game")
    elif player_surrender:
        print("Game over, You had to surrender and now languish in space jail")

print("Game over")


