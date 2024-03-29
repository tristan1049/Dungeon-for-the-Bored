from Enemy import Enemy
from Floor import Floor
from Consumables import Consumable
from Util import c, inp, inp_clear
import time
import math
import Illustrations
from Player import Player


class Fight(object):
    """To create a Fight object, that can be used for a battle in Game"""
    def __init__(self, floor: Floor, player: Player, enemy: Enemy):
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
        self.intro = True
         
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

    def print_item_description(self, item: Consumable):
        """
        Inputs:
            item: Consumable object
        Purpose: To print out the description of an item as a header
        """
        print(item) 
        print()
        print('---'*20) 

    def print_item_options(self, item: Consumable):
        """
        Inputs:
            item: Consumable object in player's inventory
        Purpose: To print options for the player for consuming a selected item
        """
        self.print_item_description(item)
        print('Your options are:')
        print('Use')
        print('Throw away')
        print('Back')
        print()

    def print_level(self, player: Player):
        """
        Inputs:
            player: Player object
        Purpose: Print the level and experience bar for player
        """
        # Print out the experience bar for the player
        exp = player.get_exp()
        level_exp = player.get_exp_next_level()
        progress = min(math.floor(20 * exp / level_exp), 20)

        exp_bar = "[" + "*"*progress + " "*(20 - progress) + "]"
        print('Level {}'.format(player.get_level()))
        print(exp_bar)

    def item_throw(self, item: Consumable):
        """
        Inputs:
            item: Consumable object in player's inventory
        Purpose: To print out the description of an item as a header and throw
        away the item
        """
        c()
        self.print_item_description(item)
        print("You've successfully thrown away a {}.".format(item.get_name()))
        self.player.remove_item(item)
        time.sleep(2)

    def get_items_list(self, items_dict: dict):
        """
        Inputs:
            items_dict: Dictionary of item names to item objects that are in 
                the player's inventory
        Purpose: To print out the list of items and amounts in the player's inventory.
        Output: Name of item to inspect
        """
        c()
        print('Your items:')
        
        # Map each item name to an integer for hotkey inputs, and print items
        item_names = list(items_dict.keys())
        for ind in range(len(item_names)): 
            name = item_names[ind]
            items = items_dict[name]
            print('   {}:     {} ({})'.format(str(ind+1), name, len(items)))
        print()
        print('Back')
        print('---'*20)

        # Return the input item name, and convert if given hotkey
        result = inp_clear('Pick an item to inspect: ').lower().strip()
        if result.isnumeric():
            index = int(result) - 1
            # If input index is valid, return the associated name
            if index >= 0 and index < len(item_names):
                return item_names[index].lower()
        return result

    def illustrate(self, p_roll: int=0, e_roll: int=0):
        """
        Inputs:
            p_roll: Integer number of player's roll
            e_roll: Integer number of enemy's roll
        Purpose: To print illustrations of the roll's of the player and enemy during battle
        """
        # Get the number of lines of dice for the player and enemy, adjust dice output accordingly
        num_lines_player = ((len(self.player.Dice)-1) // 10) + 1
        num_lines_enemy = ((len(self.enemy.Dice)-1) // 10) + 1
        screen_spacing = 4
        dice_height = 5

        # Define spacing parameters for screen based on number of dice
        total_enemy_spacing = num_lines_enemy * dice_height
        total_player_spacing = num_lines_player * dice_height
        total_screen_height = total_enemy_spacing + screen_spacing + total_player_spacing

        if not p_roll and not e_roll:
            for i in range(total_screen_height):
                print() 
                
        elif not e_roll and p_roll:
            for i in range(total_enemy_spacing + screen_spacing):
                print()
            for j in Illustrations.match(p_roll):
                print(j)

        elif not p_roll and e_roll:
            for i in Illustrations.match(e_roll):
                print(i)
            for j in range(total_player_spacing + screen_spacing):
                print()
                
        else:
            for i in Illustrations.match(e_roll):
                print(i)
            for j in range(screen_spacing):
                print()
            for k in Illustrations.match(p_roll):
                print(k)
        
    def get_fight_screen(self, player: Player, enemy: Enemy, p_roll: int=0, e_roll :int=0):
        """
        Inputs:
            player: The player of the game
            enemy: The enemy on the floor that the player is fighting
            p_roll: The player's roll against an enemy, default to None
            e_roll: The enemy's roll against the player, default to None
        Purpose: Prints the stats of the fight on the console
        """
        c()
        print('{}'.format(enemy.get_name()))
        print('HP:{}/{}'.format(enemy.get_HP(), enemy.get_maxHP()))

        self.illustrate(p_roll, e_roll)
        
        print()
        print('{}'.format(player.get_name()))
        print('HP:{}/{}'.format(player.get_HP(), player.get_maxHP()))
        print()

        # Print out the experience bar for the player
        self.print_level(player)
        print()
        print('--'*30)

    def get_resting_screen_action(self, player: Player):
        """
        Purpose: Prints the screen between battles and takes in input action
        Output: String of action input by player in game
        """
        c()
        print('Congrats!')
        print()
        print('{}: {}/{}'.format(player.get_name(), player.get_HP(), player.get_maxHP()))
        print()
        self.print_level(player)
        print('---'*20)
        print()
        self.get_resting_options()
            
        action = inp('What would you like to do? ').lower().strip()
        return action
    
    def get_fight_action(self):
        """
        Purpose: Prints the options during a fight and waits for an input action
        Output: String of action input by player in game
        """
        if self.intro:
            print(self.floor)
            print()
            self.intro = False

        self.get_battle_options()
        action = inp("What do you want to do? ").lower().strip()
        return action

    def get_item_prompt(self, player: Player, enemy: Enemy=None):
        """
        Inputs:
            player: A player object in the game
            battle: A boolean of whether the player is in battle
        Purpose: To print out the items and get player input for items
        Output: State of the battle
        """
        while True:
            # Get all of the player's items as a dictionary of name to object
            items_dict = player.get_items()
            items_dict_lower = {i.lower():items_dict[i] for i in items_dict}
            
            # Print each item as a separate screen and wait for item action
            action = self.get_items_list(items_dict)

            # If back from items screen, returns to previous screen
            if action in ['back', 'b']:                                                 
                return "ongoing"
            # Else if item name is typed, inspect item closely, and give options
            if action in items_dict_lower:                                       
                item = items_dict_lower[action][0]
                while True:
                    # Print out the description and options for selected item
                    c()
                    self.print_item_options(item)
                    
                    # Wait for action on selected item
                    item_action = inp('Choose an action: ').lower().strip()
                    # Go back to items list if back selected
                    if item_action in ['back', 'b']:
                        break
                    # If using item, update player and enemy if applicable
                    if item_action in ['use', 'u']:
                        c()
                        if enemy != None:
                            # If in battle, return as each item usage means getting hit by enemy 
                            if enemy.is_alive():
                                self.get_fight_screen(self.player, self.enemy)
                                item.use(self.player, self.enemy)

                                # Update statuses for the player
                                self.get_fight_screen(self.player, self.enemy)
                                self.player.update_statuses()
                                time.sleep(1)

                                # Continue to enemy turn after status update
                                self.get_fight_screen(self.player, self.enemy)
                                result = self.enemy_turn(player, enemy, 0, enemy.roll())
                                return result

                        # Otherwise not in battle. Use item with item options screen
                        else:
                            self.print_item_description(item)
                            item.use(self.player)
                            break
                        
                    # If throwing item away, print 
                    elif item_action in ['throw away', 'throw', 't']:
                        self.item_throw(item)
                        break
                        
    def leveling(self, player: Player, enemy: Enemy, p_roll: int, e_roll: int):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle, used for printing
            e_roll: The enemy's roll in the battle, used for printing
        Purpose: Given exp to increase the player's current exp by, add
            exp to player's stats and print out appropriate updates
        """
        cur_level = player.get_level()
        enemy_exp = enemy.get_exp()
        new_level = player.add_exp(enemy_exp)
        levels_increased = new_level - cur_level

        print("You earned {} experience!".format(str(enemy_exp)))
        time.sleep(2)
        print()
        # If increased in level, output congrats to player
        if levels_increased > 0:
            for l in range(1, levels_increased+1):
                print("Congrats!! You've reached level {}!".format(str(cur_level + l)))
                time.sleep(1)
            time.sleep(1.5)
        return


    def player_fight(self, player: Player, enemy: Enemy, p_roll: int):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
        Purpose: Plays out a player's turn in battle
        """
        # Get the fight stats and 
        self.get_fight_screen(player, enemy) 
        self.player.update_statuses()

        #Sleep in between showing rolls and doing damage to give time for player to see
        time.sleep(1)                                                               
        
        self.get_fight_screen(player, enemy)
        self.get_fight_screen(player, enemy, p_roll)                             
        
        time.sleep(1)
        print('You rolled a {}'.format(sum(p_roll)))
        time.sleep(1)

        #Damage the enemy with the player's roll 
        self.enemy.damage(sum(p_roll))                                 
        

    def enemy_turn(self, player: Player, enemy: Enemy, p_roll: int, e_roll: int):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
            e_roll: The enemy's roll in the battle
        Purpose: Plays out a enemy's turn in battle
        """
        # Give all of the enemy's items and experience to player 
        if not enemy.is_alive():
            print("You've killed the enemy!")
            enemy.give_items(player)
            time.sleep(1)
            print()
            self.leveling(player, enemy, p_roll, 0)
            return 'won'
    
        # If enemy is alive, let enemy do damage and show roll
        print('{} is still alive!'.format(enemy.get_name())) 
        time.sleep(2)
        
        self.get_fight_screen(player, enemy, p_roll, e_roll)
        
        time.sleep(1)
        print('{} rolled a {}'.format(enemy.get_name(), sum(e_roll)))
        
        player.damage(sum(e_roll))
        
        time.sleep(2)
        if not player.is_alive(): 
            return 'lost'
        return 'ongoing'
        
    def turn(self):
        """
        Purpose: To simulate a turn in the battle
        """
        while True:
            # Display the fighting screen and wait for action input
            self.get_fight_screen(self.player, self.enemy)                 
            action = self.get_fight_action()

            # If exiting or running, return 'ran' to end game
            if action in ['exit', 'e', 'run', 'r']:
                self.get_fight_screen(self.player, self.enemy)   
                return 'ran'
            
            # If viewing items, give interactive inventory prompt.
            elif action in ['items', 'i']:
                # Check if the battle ended with the use of an item
                result = self.get_item_prompt(self.player, self.enemy)
                if result in ["won", "lost"]:
                    return result

            # If fighting, calculate rolls and show fighting screen 
            elif action in ['fight', 'f']:                              
                roll = self.player.roll()
                enemy_roll = self.enemy.roll()

                # Simulate the player's turn when action is to fight
                self.player_fight(self.player, self.enemy, roll)  

                # Simulate the enemy's turn and get the result of the end of turn
                return self.enemy_turn(self.player, self.enemy, roll, enemy_roll)


    def battle(self):
        """
        Purpose: To simulate the entire battle between a player and enemy
        """
        # Start battle one turn at a time
        while True:
            result = self.turn()
            
            if result == 'won':
                while True:           #Another while loop, only break when player leaves floor or dies somehow
                    action = self.get_resting_screen_action(self.player)
                    if action in ['proceed', 'p']:
                        return 'proceed'
                    
                    elif action in ['run', 'r']:
                        return 'ran'
    
                    elif action in ['items', 'i']:
                        self.get_item_prompt(self.player)
            
            if result == 'lost' or result == 'ran':
                return result