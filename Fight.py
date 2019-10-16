import Game
from Interface import c as c
from Interface import inp
import time
import Illustrations



class Fight(object):
    """To create a Fight object, that can be used for a battle in Game"""
    
    def __init__(self, floor, player, enemy):
        """
        Inputs:
            floor: A floor object in the game
            player: A Player object in the fight
            enemy: A Enemy object in the fight
            level: The floor level the fight is on
        Purpose: To simulate a battle with player and enemy
        """
        self.floor = floor
        self.player = player
        self.enemy = enemy
        
        
        
        
    def get_battle_options(self):
        """
        Purpose: To print the options for the player in battle
        """
        print("Your options are: ")
        print('Fight')
        print('Items')
        print('Run')
        
        
    def get_resting_options(self):
        """
        Purpose: To print options for the player out of battle
        """
        print("Your options are: ")
        print('Proceed')
        print('Items')
        print('Run')
        
        
        
    def illustrate(self, p_roll=None, e_roll=None):
        """
        Inputs:
            p_roll: Integer number of player's roll
            e_roll: Integer number of enemy's roll
        Purpose: To print illustrations of the roll's of the player and enemy during battle
        """
        if p_roll == None and e_roll == None:
            for i in range(14):
                print()

                
                
                
                
        elif e_roll == None and p_roll != None:
            for i in range(9):
                print()
                
            for j in Illustrations.match(p_roll):
                print(j)
                
                
        
        
        
        elif p_roll == None and e_roll != None:
            for i in Illustrations.match(e_roll):
                print(i)
                
            for j in range(9):
                print()
                
                
                
                
                
        else:
            for i in Illustrations.match(e_roll):
                print(i)
                
            for j in range(4):
                print()
                
            for k in Illustrations.match(p_roll):
                print(k)
                
                
                
                
                
            
    def get_fight_screen(self, player, enemy, p_roll=None, e_roll=None):
        """
        Inputs:
            player: The player of the game
            enemy: The enemy on the floor that the player is fighting
            p_roll: The player's roll against an enemy, default to None
            e_roll: The enemy's roll against the player, default to None
        Purpose: Prints the stats and options of the fight on the console
        """
        print('{}'.format(enemy.get_name()))
        print('HP:{}/{}'.format(enemy.get_HP(), enemy.get_maxHP()))

        self.illustrate(p_roll, e_roll)
        
        print()
        print('{}'.format(player.get_name()))
        print('HP:{}/{}'.format(player.get_HP(), player.get_maxHP()))
        print()
        print('--'*30)

        
        
    def get_resting_screen_action(self, player):
        """
        Purpose: Prints the screen between battles and takes in input action
        Output: String of action input by player in game
        """
        print('Congrats!')
        print()
        print('{}: {}/{}'.format(player.get_name(), player.get_HP(), player.get_maxHP()))
        print('---'*20)
        print()
        self.get_resting_options()
            
        action = inp('What do you want to do? ').lower().strip()
        return action
    
        
    def get_fight_action(self):
        """
        Purpose: Prints the options during a fight and waits for an input action
        Output: String of action input by player in game
        """
        self.get_battle_options()
        action = inp("What do you want to do? ").lower().strip()

        
        return action
        
    
    
    
    
    def get_item_prompt(self, player, enemy=None):
        """
        Inputs:
            player: A player object in the game
            battle: A boolean of whether the player is in battle
        Purpose: To print out the items and get player input for items
        Output: Boolean of whether an item was used or not
        """
        while True:
            c()
            
            items_dict = player.get_items()
            items_dict_lower = {i.lower():items_dict[i] for i in items_dict}
            
            
            print('Your items:')
            for name in items_dict:                                                        #Prints the descriptions            
                print('      {} ({})'.format(name, len(items_dict[name])))
            print()
            print('Back')
            print('---'*20)
            action = inp('Pick an item to inspect: ').lower().strip()
            c()
            
            
            if action == 'back':                                                           #If back from items screen, returns and restores to resting screen
                return False
    
    
            elif action in items_dict_lower:                                               #Else if item name is typed, inspect item closely, and give options
                item = items_dict_lower[action][0]
                while True:
                    print(item)  
            
                    print()
                    print('---'*20)
                    print('Your options are:')
                    print('Use')
                    print('Throw away')
                    print('Back')
                    print()
                    
                    item_action = inp('Choose an action: ').lower().strip()
        
        
                    if item_action == 'back':
                        break
                    
                    elif item_action == 'use':
                        c()
                        self.get_fight_screen(self.player, self.enemy)
                        item.use(self.player, self.enemy)

                        if item.uses == 0:
                            self.player.items.remove(item)
                            
                        if enemy != None:                                                          #If in battle, return as each item usage means getting hit by enemy
                            self.get_fight_screen(self.player, self.enemy)
                            self.enemy_turn(player, enemy, None, enemy.roll())
                            return
                        
                        break
                        
                    elif item_action == 'throw away':
                        c()
                        print("You've successfully thrown away a {}.".format(item.get_name()))
                        time.sleep(2)
                        self.player.items.remove(item)
                        c()
                        break
                        
                    
                        
                    
                    
    
    
    
    def player_fight(self, player, enemy, p_roll):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
        Purpose: To compact the commands for the player's fight turn into one function
        """
        time.sleep(1)                                                                   #Sleep in between showing rolls and doing damage to give time for player to see
        c()
        
        self.get_fight_screen(player, enemy)
        player.statuses()                                                               #Before rolling, activate any status effects of player
        c()
        self.get_fight_screen(player, enemy, p_roll)                                    #Get the fight screen with player roll
        
        time.sleep(1)
        print('You rolled a {}'.format(sum(p_roll)))
        time.sleep(1)
        
        self.enemy.damage(sum(p_roll))                                                  #Damage the enemy with the player's roll
        
        
        
        
        
        
        
        
    def enemy_turn(self, player, enemy, p_roll, e_roll):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
            e_roll: The enemy's roll in the battle
        Purpose: To compact commands for the enemy's turn into one function
        """
        if not enemy.is_alive():
            print("You've killed the enemy!")
            enemy.give_items(player)                                                #Give any of enemy's items to player
            
            return 'won'
            
        
        else:
            print('{} is still alive!'.format(enemy.get_name()))                    #If enemy is alive, let enemy do damage and show roll
            time.sleep(2)
            c()
            
            self.get_fight_screen(player, enemy, p_roll, e_roll)
            
            time.sleep(1)
            print('{} rolled a {}'.format(enemy.get_name(), sum(e_roll)))
            
            player.damage(sum(e_roll))
            
            
            
            
            if not player.is_alive():
                return 'lost'
                
        time.sleep(2)
        
    
    
    
    
    
    
    
    
    
    def turn(self):
        """
        Purpose: To simulate a turn in the battle
        """
        self.get_fight_screen(self.player, self.enemy)                                  #Display the fighting screen and wait for action input
        action = self.get_fight_action()


        if action == 'exit' or action == 'run':                                         #If exiting or running, return 'ran' to end game
            return 'ran'
           
        elif action == 'items':
            self.get_item_prompt(self.player, self.enemy)
        
        
        
        elif action == 'fight':                                                         #If fighting, calculate rolls and show fighting screen
            c()
            roll = self.player.roll()
            enemy_roll = self.enemy.roll()
            
            self.get_fight_screen(self.player, self.enemy)
            self.player_fight(self.player, self.enemy, roll)                            #To simulate the player's turn when action is to fight

            result = self.enemy_turn(self.player, self.enemy, roll, enemy_roll)
            if result != None:
                return result
            
                                                                                
        c()








    def battle(self):
        """
        Purpose: To simulate the entire battle between a player and enemy
        """
        
        while True:
            result = self.turn()
            
            if result != None:
                time.sleep(2)
                c()
            
            
            
                if result == 'won':
    
                    while True:                                                             #Another while loop, only break when player leaves floor or dies somehow
                        action = self.get_resting_screen_action(self.player)
                            
                        
                        if action == 'proceed':
                            c()
                            result = 'proceed'
                            break
                        
                        elif action == 'run':
                            c()
                            result = 'ran'
                            break
        
                        elif action == 'items':
                            self.get_item_prompt(self.player)
                        
                        c()
    
    
                if result == 'lost':
                    print('Oh noo! You died!')
    
                    
                if result == 'ran':
                    print('You escape the dungeon, and live to fight another day.')
            
                
                return result
            
            
