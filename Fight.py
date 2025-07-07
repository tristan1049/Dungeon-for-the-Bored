from Enemy import Enemy
from Floor import Floor
from Consumables import Consumable
from Util import inp
from Util import add_to_queue, add_list_to_queue, print_queue, input_with_queue
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
        Purpose: To get the options for the player in battle
        """
        q = []
        add_to_queue(q, "Your options are:")
        add_to_queue(q, "Fight")
        add_to_queue(q, "Items")
        add_to_queue(q, "Run")
        return q
        
    def get_resting_options(self):
        """
        Purpose: To get the options for the player out of battle
        """
        q = []
        add_to_queue(q, "Your options are:")
        add_to_queue(q, "Proceed")
        add_to_queue(q, "Items")
        add_to_queue(q, "Run")
        return q

    def get_item_description(self, item: Consumable):
        """
        Inputs:
            item: Consumable object
        Purpose: To get the description of an item as a header
        """
        q = []
        add_to_queue(q, str(item))
        add_to_queue(q, "---"*20)
        add_to_queue(q, "")
        return q

    def get_item_options(self, item: Consumable):
        """
        Inputs:
            item: Consumable object in player's inventory
        Purpose: To get options for the player for consuming a selected item
        """
        q = []
        add_list_to_queue(q, self.get_item_description(item))
        add_to_queue(q, "Your options are:")
        add_to_queue(q, "Use")
        add_to_queue(q, "Throw away")
        add_to_queue(q, "Back")
        return q

    def get_player_level_text(self, player: Player):
        """
        Inputs:
            player: Player object
        Purpose: Gets the level and experience bar for player
        """
        q = []
        # Print out the experience bar for the player
        exp = player.get_exp()
        level_exp = player.get_exp_next_level()
        progress = min(math.floor(20 * exp / level_exp), 20)
        exp_bar = "[" + "*"*progress + " "*(20 - progress) + "]"
        add_to_queue(q, f"Level {player.get_level()}")
        add_to_queue(q, exp_bar)
        return q

    def print_throw_away_item(self, q, item: Consumable):
        """
        Inputs:
            item: Consumable object in player's inventory
        Purpose: To print the description of an item as a header and throw away the item
        """
        add_list_to_queue(q, self.get_item_description(item))
        add_to_queue(q, f"You've successfully thrown away a {item.get_name()}.")
        print_queue(q)
        self.player.remove_item(item)
        time.sleep(2)

    def prompt_items_list(self, player: Player, items_dict: dict):
        """
        Inputs:
            player: Player object
            items_dict: Dictionary of item names to item objects that are in 
                the player's inventory
        Purpose: To print out the list of items and amounts in the player's inventory.
        Output: Name of item to inspect
        """
        q = []
        q_header = self.get_item_menu_header(player)
        add_list_to_queue(q, q_header)
        add_to_queue(q, "Your items:")
        
        # Map each item name to an integer for hotkey inputs, and print items
        item_names = list(items_dict.keys())
        for ind in range(len(item_names)): 
            name = item_names[ind]
            items = items_dict[name]
            add_to_queue(q, f"   {str(ind+1)}:     {name} ({len(items)})")
        add_to_queue(q, "Back")
        add_to_queue(q, "---"*20)

        # Return the input item name, and convert if given hotkey
        result = input_with_queue(q, "Pick an item to inspect: ").lower()
        if result.isnumeric():
            index = int(result) - 1
            # If input index is valid, return the associated name
            if index >= 0 and index < len(item_names):
                return item_names[index].lower()
        return result

    def get_dice_illustration(self, p_roll: int=0, e_roll: int=0):
        """
        Inputs:
            p_roll: Integer number of player's roll
            e_roll: Integer number of enemy's roll
        Purpose: To get illustrations of the rolls of the player and enemy during battle
        """
        q = []
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
                add_to_queue(q, "")
                
        elif not e_roll and p_roll:
            for i in range(total_enemy_spacing + screen_spacing):
                add_to_queue(q, "")
            for j in Illustrations.match(p_roll):
                add_to_queue(q, f"{j}")

        elif not p_roll and e_roll:
            for i in Illustrations.match(e_roll):
                add_to_queue(q, f"{i}")
            for j in range(total_player_spacing + screen_spacing):
                add_to_queue(q, "")
                
        else:
            for i in Illustrations.match(e_roll):
                add_to_queue(q, f"{i}")
            for j in range(screen_spacing):
                add_to_queue(q, "")
            for k in Illustrations.match(p_roll):
                add_to_queue(q, f"{k}")
        
        return q
        
    def get_fight_screen(self, player: Player, enemy: Enemy, p_roll: int=0, e_roll :int=0):
        """
        Inputs:
            player: The player of the game
            enemy: The enemy on the floor that the player is fighting
            p_roll: The player's roll against an enemy, default to None
            e_roll: The enemy's roll against the player, default to None
        Purpose: Gets the stats of the fight for the console
        """
        q = []
        add_to_queue(q, f"{enemy.get_name()}")
        add_to_queue(q, f"HP:{enemy.get_HP()}/{enemy.get_maxHP()}")

        add_list_to_queue(q, self.get_dice_illustration(p_roll, e_roll))

        add_to_queue(q, f"\n{player.get_name()}")
        add_to_queue(q, f"HP:{player.get_HP()}/{player.get_maxHP()}")

        # Get the experience bar for the player
        add_list_to_queue(q, self.get_player_level_text(player))
        add_to_queue(q, "---"*20)
        return q

    def prompt_resting_screen_action(self, player: Player):
        """
        Purpose: Gets the screen between battles and takes in input action
        Output: String of action input by player in game
        """
        q = []
        add_to_queue(q, "Congrats!")
        add_to_queue(q, f"{player.get_name()}: {player.get_HP()}/{player.get_maxHP()}")
        add_list_to_queue(q, self.get_player_level_text(player))
        add_to_queue(q, "---"*20 + "")
        add_list_to_queue(q, self.get_resting_options())
        print_queue(q)
        action = inp("\nWhat would you like to do? ").lower().strip()
        return action
    
    def prompt_fight_action(self, q):
        """
        Purpose: Gets the options during a fight and waits for an input action
        Output: String of action input by player in game
        """
        add_to_queue(q, f"{self.floor}")
        if (self.intro):
            add_to_queue(q, f"There's a {self.enemy.get_name()}! Get ready to fight!")
            self.intro = False
        add_to_queue(q, "")
        add_list_to_queue(q, self.get_battle_options())
        action = input_with_queue(q, "\nWhat do you want to do? ").lower()
        return action

    def prompt_item_menu(self, player: Player, enemy: Enemy=None):
        """
        Inputs:
            player: A player object in the game
            battle: A boolean of whether the player is in battle
        Purpose: To print out the items and get player input for items
        Output: State of the battle
        q is emptied on this function call
        """
        q = []
        q_header = self.get_item_menu_header(player)
        while True:
            # Get all of the player's items as a dictionary of name to object
            items_dict = player.get_items()
            items_dict_lower = {i.lower():items_dict[i] for i in items_dict}

            # Print each item as a separate screen and wait for item action
            action = self.prompt_items_list(player, items_dict)

            # If back from items screen, returns to previous screen
            if action in ["back", "b"]:
                return "ongoing"
            # Else if item name is typed, inspect item closely, and give options
            if action in items_dict_lower:
                item = items_dict_lower[action][0]
                while True:
                    # Get the description and options for selected item
                    add_list_to_queue(q, q_header)
                    add_list_to_queue(q, self.get_item_options(item))
                    # Wait for action on selected item
                    item_action = input_with_queue(q, "Choose an action: ").strip()
                    # Go back to items list if back selected
                    if item_action in ["back", "b"]:
                        break
                    # If using item, update player and enemy if applicable
                    if item_action in ["use", "u"]:
                        if enemy is not None:
                            # If in battle, return as each item usage means getting hit by enemy
                            if enemy.is_alive():
                                add_list_to_queue(q, self.get_fight_screen(self.player, self.enemy))
                                print_queue(q)
                                if (item.does_interact_with_enemies()):
                                    item.use(self.player, self.enemy)
                                else:
                                    item.use(self.player)

                                # Update statuses for the player
                                add_list_to_queue(q, self.get_fight_screen(self.player, self.enemy))
                                print_queue(q)
                                self.player.update_statuses(self.enemy)
                                time.sleep(1)

                                # Continue to enemy turn after status update
                                return self.enemy_turn(q, player, enemy, [])

                        # Otherwise not in battle. Use item with item options screen
                        else:
                            add_list_to_queue(q, q_header)
                            add_list_to_queue(q, self.get_item_description(item))
                            print_queue(q)
                            item.use(self.player)
                            break
                        
                    # If throwing item away, print
                    elif item_action in ["throw away", "throw", "t"]:
                        print_queue(q_header, False)
                        add_list_to_queue(q, q_header)
                        self.print_throw_away_item(q, item)
                        break

    def get_item_menu_header(self, player: Player):
        """
        Inputs:
            player: The player object in the battle
        Purpose: Return queue of the item menu header text
        """
        q_start = []
        add_to_queue(q_start, f"{self.floor}")
        add_to_queue(q_start, f"{player.get_name()}")
        add_to_queue(q_start, f"HP:{player.get_HP()}/{player.get_maxHP()}")
        add_to_queue(q_start, "---"*20 + "\n")
        return q_start
                        
    def print_leveling(self, player: Player, enemy: Enemy):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
        Purpose: Given exp to increase the player's current exp by, add
            exp to player's stats and print out appropriate updates
        """
        cur_level = player.get_level()
        enemy_exp = enemy.get_exp()
        new_level = player.add_exp(enemy_exp)
        levels_increased = new_level - cur_level

        print(f"You earned {enemy_exp} experience")
        time.sleep(2)
        print()
        # If increased in level, output congrats to player
        if levels_increased > 0:
            for l in range(1, levels_increased+1):
                print(f"Congrats!! You've reached level {str(cur_level + l)}!")
                time.sleep(1)
            time.sleep(1.5)

    def player_fight(self, q, player: Player, enemy: Enemy):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
        Purpose: Plays out a player's turn in battle, and returns the player's roll
        q is left empty after this function
        """
        # Get the fight stats and update statuses
        add_list_to_queue(q, self.get_fight_screen(player, enemy))
        print_queue(q)
        self.player.update_statuses(enemy)

        # Get the player's roll after updating statuses
        p_roll = self.player.roll()

        #Sleep in between showing rolls and doing damage to give time for player to see
        time.sleep(1)
        add_list_to_queue(q, self.get_fight_screen(player, enemy, p_roll))
        print_queue(q)
        
        time.sleep(1)
        print(f"You rolled a {sum(p_roll)}")
        time.sleep(1)

        #Damage the enemy with the player's roll
        self.enemy.damage(sum(p_roll))

        # Give all of the enemy's items and experience to player
        if not enemy.is_alive():
            print("You've killed the enemy!")
            enemy.give_items(player)
            time.sleep(1)
            self.print_leveling(player, enemy)
            return "won"
    
        # If enemy is alive, let enemy do damage and show roll
        print(f"{enemy.get_name()} is still alive!")
        time.sleep(2)

        return p_roll
                                       
    def enemy_turn(self, q, player: Player, enemy: Enemy, p_roll: list):
        """
        Inputs:
            player: The player object in the battle
            enemy: The enemy object in the battle
            p_roll: The player's roll in the battle
            e_roll: The enemy's roll in the battle
        Purpose: Plays out a enemy's turn in battle
        q is left empty after this function
        """
        if not enemy.is_alive():
            return "won"

        e_roll = self.enemy.roll()
        add_list_to_queue(q, self.get_fight_screen(player, enemy, p_roll, e_roll))
        print_queue(q)
        
        time.sleep(1)
        print(f"{enemy.get_name()} rolled a {sum(e_roll)}")
        
        player.damage(sum(e_roll))
        
        time.sleep(2)
        if not player.is_alive():
            return "lost"
        return "ongoing"
        
    def turn(self):
        """
        Purpose: To simulate a turn in the battle
        """
        q = []
        while True:
            # Display the fighting screen and wait for action input
            add_list_to_queue(q, self.get_fight_screen(self.player, self.enemy))
            action = self.prompt_fight_action(q)

            # If exiting or running, return 'ran' to end game
            if action in ["exit", "e", "run", "r"]:
                add_list_to_queue(q, self.get_fight_screen(self.player, self.enemy))
                print_queue(q)
                return "ran"

            # If viewing items, give interactive inventory prompt.
            elif action in ["items", "i"]:
                # Check if the battle ended with the use of an item
                result = self.prompt_item_menu(self.player, self.enemy)
                if result in ["won", "lost"]:
                    return result

            # If fighting, calculate rolls and show fighting screen
            elif action in ["fight", "f"]:
                # Simulate the player's turn when action is to fight
                p_roll = self.player_fight(q, self.player, self.enemy)

                # Simulate the enemy's turn and get the result of the end of turn
                return self.enemy_turn(q, self.player, self.enemy, p_roll)


    def battle(self):
        """
        Purpose: To simulate the entire battle between a player and enemy
        """
        # Start battle one turn at a time
        while True:
            result = self.turn()
            
            if result == "won":
                while True:           #Another while loop, only break when player leaves floor or dies somehow
                    action = self.prompt_resting_screen_action(self.player)
                    if action in ["proceed", "p"]:
                        return "proceed"
                    
                    elif action in ["run", "r"]:
                        return "ran"
    
                    elif action in ["items", "i"]:
                        self.prompt_item_menu(self.player)
            
            if result == "lost" or result == "ran":
                return result