class Player(object):
    """Creates a player object for someone to play a game with"""

    def __init__(self, name, HP=40):
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
        return self.status_effects
    
    
    
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
    
    
    
    
    def is_alive(self):
        """
        Purpose: To check that the player still has HP
        Output: Boolean of whether player's HP is > 0
        """
        return self.HP > 0


    def add_dice(self, Dice):
        """
        Inputs:
            Dice: A Dice object from Dice.py
        Purpose: To add a die to the player's inventory
        """
        self.Dice.append(Dice)
    
    
    def roll(self):
        """
        Purpose: To roll all of the player's dice for one turn
        Output: List of all Dice rolls
        """
        rv = []
        
        for d in self.Dice:
            rv.append(d.toss())
        
        return rv
    
        
    def damage(self, change):
        """
        Inputs:
            change: An integer to decrease HP by
        Purpose: To change the HP of a player object for damage
        """
        self.HP -= change
            
        if self.HP <= 0:
            self.HP = 0
            self.status = 'dead'
            
            
    def healing(self, change):
        """
        Inputs:
            change: An integer to increase HP by
        Purpose: To change the HP of a player object for healing
        """
        self.HP += change
            
        if self.HP > self.maxHP:
            self.HP = self.maxHP
            

    def change_maxHP(self, change):
        """
        Inputs:
            change: An integer to change maxHP by, + for gain and - for loss
        Purpose: To change the maxHP of a player object for damage or healing
        """
        self.maxHP += change
            
        if self.maxHP < 1:
            self.maxHP = 1
            
            
            
    def statuses(self):
        """
        Purpose: Activate all the status effects of the player for a turn,
        and remove any statuses that expire
        """
        for stat in self.status_effects:                                            #Where each stat is an object
            stat.status_use(self)
            
            if stat.get_turns() == 0:    
                self.status_effects.remove(stat)
                
                
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
