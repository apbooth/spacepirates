from random import randint

#set up player and enemy ships vars
class pirate_ship():
    captain_name = "Zolt"
    ship_health = 100
    ship_surrender = False

    def __init__(self):
        self.ship_ammo = {'laser': 25,
                        'cannon': 5 }
        self.ship_loot = 25

    def ships_status(self):
        print('You are captain {captain_name}\nYour ships health is {ships_health}%\nYou have {ships_ammo} rounds of ammo\nThe ships shields are at {ships_shields}%\nShips supplies are {ships_loot}% and morale is {ships_morale}%'.format(captain_name=self.captain_name,ships_health=self.ship_health, ships_ammo=self.ship_ammo, ships_loot=self.ship_loot))

    def select_weapon(self):
        print("boo")
        i = 0
        for weapon, number in self.ship_ammo.items():
            if number > 0:
                print('Press {i} to fire {weapon} {number} shots left..\n'.format(number=number, weapon=weapon, i=i+1))
                i += 1
        weapon_choice = int(input("\nenter weapon choice: "))
        while weapon_choice > i:
            weapon_choice = int(input("\nenter weapon choice: "))
        return weapon_choice

    def attack(self, weapon_used):
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
        
    def reduce_ammo(self, weapon_used):
        if weapon_used  == 1:
            self.ship_ammo['laser'] -= 1
        if weapon_used == 2:
            self.ship_ammo['cannon'] -= 1

    def health(self):
        if self.ship_health > 0:
            return True
        return False
    
    def player_surrender(self):
        if self.ship_health < 15:
            print("...Communications officer: Captain, receiving message...\n...The Galaxons are telling us to surrender...\n...what should I reply?...")
            reply = int(input("To surrender press 1 to fight on press 2"))
            while reply != 1 or reply != 2:
                reply = int(input("To surrender press 1 to fight on press 2"))
            if reply == 1:
                return True
 

    def looting(self, cargo, player):    
        print("\n...Crew: Captain, we have boarded the cargo ship and found {amount} space coins, Transfering to our ship..".format(amount=cargo))
        player += cargo
        cargo = 0    
        print("We now have {total_amount} space coins in the ships loot, captain...\n".format(total_amount=player))

class cago_ship():
    ship_surrender = False
    ship_health = 100
    def __init__(self):
        self.ship_ammo = {'laser': randint(20, 30),
                            'cannon': randint(1, 5)}
        self.ship_content = randint(50, 100)
    
    def select_weapon(self):
        i = 0
        for weapon, number in self.ship_ammo.items():
                    if number > 0:
                        i += 1 
        return randint(0, i) 
    
    def attack(self, weapon_used):
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
    
    def reduce_ammo(self, weapon_used):
        if weapon_used  == 1:
            self.ship_ammo['laser'] -= 1
        if weapon_used == 2:
            self.ship_ammo['cannon'] -= 1

    def health(self):
        if self.ship_health > 0:
            return True
        return False

    def cargo_surrender(self):
    #create random choice for cargo ship to surrender
        number = randint(0, 2)
        if self.ship_health < 20 and number == 0:
            return True
    

#game state to end the game when False
game_state = True
player = pirate_ship()
cargo_ship_one = cago_ship()

player.ships_status

while game_state == True:
    
    print("..Navigator: Now entering zone one, Captain..\n")
    print("..Tatical Officer: Captain, sensors have detected a ship approaching...\nit's a cargo ship..\n")

    while player.health and player.health and cargo_ship_one.health:
        if player.ship_ammo['laser'] > 0 or player.ship_ammo['cannon'] > 0:
            weapon_used = player.select_weapon()
            player_attack = player.attack(weapon_used)
            player.reduce_ammo(weapon_used)
            cargo_ship_one.ship_health -= player_attack
            print("\nWeapons operator: We have inflicted {damage}% damage to the cargo ship, Captain..\n".format(damage=player_attack))
        else:
            print("weapons operator: Captain, we have run out of Ammunition..\n")
            player.ship_surrender = True
            game_state = False
            break
        
        if not cargo_ship_one.cargo_surrender() and not player.player_surrender():
            if cargo_ship_one.health:
                weapon_used = cargo_ship_one.select_weapon()
                attack = cargo_ship_one.attack(weapon_used)
                cargo_ship_one.reduce_ammo(weapon_used)
                player.ship_health -= attack
                print("Tatical officer: Incoming fire..\n")
                print("Tatical officer: We have received {damage}% damage. You ship is at {health}%..\n".format(damage=attack, health=player.ship_health))
            else:
                print("...Tatical officer: Captain the cargo ship has been destroyed, no loot this time...")
                game_state = False
                break
        
        else:
            ship_surrender = True
            print("...Comunications officer: Captain incoming radio message...\nCargo ship is surrendering..\nPreparing to board the cargo ship...\n")
            player.looting(cargo_ship_one.ship_content, player.ship_loot)
            game_state = False
            break

        
    #check if player ship has been destroyed
    if player.ship_health <= 0:
        print("Game over your ship has been destroyed!!!")
        game_state = False
    elif cargo_ship_one.ship_surrender:
        print("Congratulations you got the loot and have won the game")
    elif player.ship_surrender:
        print("Game over, You had to surrender and now languish in space jail")

print("Game over")


