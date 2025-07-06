from Dice import Dice
import time

class Player(object):
    """Creates a player object for someone to play a game with"""
    def __init__(self, name: str, HP: int=40):
        """
        Inputs:
            name: The name of the player
            HP: The number of health points for a player, default at 40
        Purpose: To create a player with a number of HP, for a game
        """
        self.name = name
        self.maxHP = HP
        self.HP = HP
        self.Dice = []
        self.status = 'alive'
        self.items = []
        self.status_effects = []
        self.level = 1
        self.exp = 0

    def get_name(self):
        """
        Purpose: To get the name of the player
        Output: Name of the player
        """
        return self.name

    def get_maxHP(self):
        """
        Purpose: To get the max health of the player
        Output: Max health points of the player
        """
        return self.maxHP
    
    def get_HP(self):
        """
        Purpose: To get the health of the player
        Output: Current health points of the player
        """
        return self.HP

    def get_status(self):
        """
        Purpose: To get the status of the game
        Output: String representation of the status of the game
        """
        return self.status
        
    def get_status_effects(self):
        """
        Purpose: To get the status effects of the player
        Output: List of objects that are effecting the player
        """
        return [i for i in self.status_effects]
    
    def get_items(self):
        """
        Purpose: To get the items in the player's inventory
        Output: Dictonary of item names to list of item objects that the player holds
        """
        rv = {}
        for item in self.items:
            if item.get_name() in rv:
                rv[item.get_name()].append(item)
            else:
                rv[item.get_name()] = [item]
        return rv

    def get_level(self):
        """
        Purpose: To get the integer level of the player
        Output: Current level of the player
        """
        return self.level

    def level_up(self):
        """
        Purpose: To level up the player and add improvements to stats
        """
        self.maxHP += 3
        self.HP += 3
        self.level += 1

    def get_exp(self):
        """
        Purpose: To get the integer level exp of the player for current level
        Output: Current exp for current level of the player
        """
        return self.exp

    def get_exp_next_level(self):
        """
        Output: The integer amount of experience required at the player's current 
            level to get to the next level
        """
        return 20 * self.get_level()

    def add_exp(self, exp: int):
        """
        Purpose: Add experience to the character's level
        Output: Current level of the player after experience is added
        """
        # Determine experience needed for level and current experience with exp
        level_exp = self.get_exp_next_level()
        self.exp += exp

        # If have enough exp to level, level up and add_exp again
        if self.exp >= level_exp:
            self.exp -= level_exp
            self.level_up()
            return self.add_exp(0)

        # Once done leveling, just return the current level of the player
        return self.get_level()

    def remove_item(self, item):
        """
        Purpose: Remove item object from player inventory
        Output: Boolean of whether item was successfully removed
        """
        self.items.remove(item)

    def add_item(self, item):
        """
        Purpose: Add item object to player inventory
        """
        self.items.append(item)
     
    def is_alive(self):
        """
        Purpose: To check that the player still has HP
        Output: Boolean of whether player's HP is > 0
        """
        return self.HP > 0

    def add_dice(self, num: int):
        """
        Inputs:
            num: Nonnegative integer number of Dice objects to add to player
        Purpose: To add dice to the player's inventory
        """
        for _ in range(num):
            self.Dice.append(Dice())
    
    def remove_dice(self, num: int):
        """
        Inputs:
            num: Nonnegative integer number of Dice objects to remove from player
        Purpose: To remove dice from the player's inventory
        """
        self.Dice = self.Dice[:max(0, len(self.Dice)-num)]

    def roll(self):
        """
        Purpose: To roll all of the player's dice for one turn
        Output: List of all Dice rolls
        """
        return [d.toss() for d in self.Dice]
    
    def damage(self, change: int):
        """
        Inputs:
            change: An integer to decrease HP by
        Purpose: To change the HP of a player object for damage
        """
        self.HP -= change
        if self.HP <= 0:
            self.HP = 0
            self.status = 'dead'
            
    def healing(self, change: int):
        """
        Inputs:
            change: An integer to increase HP by
        Purpose: To change the HP of a player object for healing
        """
        self.HP += change
        if self.HP > self.maxHP:
            self.HP = self.maxHP

    def change_maxHP(self, change: int):
        """
        Inputs:
            change: An integer to change maxHP by, + for gain and - for loss
        Purpose: To change the maxHP of a player object for damage or healing
        """
        self.maxHP += change
        if self.maxHP < 1:
            self.maxHP = 1
            
    def update_statuses(self, enemy):
        """
        Purpose: Activate all the status effects of the player for a turn,
        and remove any statuses that expire
        """
        # Update each status effect object
        for stat in self.get_status_effects():                                          
            stat.status_use(self, enemy)
            time.sleep(.4)
            
    def remove_status(self, status):
        """
        Inputs:
            status: A consumable item that currently has a status effect on the player
        Purpose: Remove status from the current player status effects
        """
        self.status_effects.remove(status)
                
    def restart(self):
        """
        Purpose: To restart all the stat's in the player object
        """
        self.items = []
        self.status_effects = []
        self.HP = self.maxHP
        
    def __str__(self):
        """
        Purpose: A representation of the player's current status
        Output: A string representation of player's stats
        """
        print('player:{}'.format(self.name))
        print('HP:{}/{}'.format(self.HP, self.maxHP))
