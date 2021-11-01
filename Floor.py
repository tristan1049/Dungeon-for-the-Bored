import Enemy as E
from Util import choose_one


class Floor(object):
    """Creates a Floor object, containing an enemy"""
    def __init__(self, level: int=1):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an enemy
        """
        self.level = level
        self.enemy = None
        
    def get_floor(self):
        """
        Purpose: To get the floor number of the dungeon
        Output: Integer value of floor level
        """
        return self.level
    
    def get_enemy(self):
        """
        Purpose: To get the enemy on the floor
        Output: An enemy object
        """
        return self.enemy
    
    def __str__(self):
        return "Dungeon: Floor {}\nThere's a {}! Get ready to fight!".format(self.level, self.enemy.get_name())
    
    
class Floor_Easy(Floor):
    """Creates a Floor object for floors from 1 to 5"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(Floor_Easy, self).__init__(level)
        
        poss_enemy = [E.Rabid_Rabbit(), E.Wolf(), E.Goblin()]
        weights = [0.4, 0.35, 0.25]
        
        self.enemy = choose_one(poss_enemy, weights)


class Floor_Medium(Floor):
    """Creates a Floor object for floors from 6 to 10"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(Floor_Medium, self).__init__(level)
        
        poss_enemy = [E.Venom_Spider(), E.Lost_Spirit(), E.Assassin()]
        weights = [0.4, 0.35, 0.25]
        
        self.enemy = choose_one(poss_enemy, weights)
    
    
class Floor_Hard(Floor):
    """Creates a Floor object for floors from 6 to 10"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(Floor_Hard, self).__init__(level)
        
        poss_enemy = []
        weights = []
        
        self.enemy = choose_one(poss_enemy, weights)
    
    
class Boss_Floor(Floor):
    """Creates an instance of a boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(Boss_Floor, self).__init__(level)
        
        
class Boss_Floor_Easy(Boss_Floor):
    """Creates an instance of an easy boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(Boss_Floor_Easy, self).__init__(level)
        
        poss_boss = [E.Wolf_Pack(), E.Goblin_Mob()]
        weights = [0.5, 0.5]
        
        self.enemy = choose_one(poss_boss, weights)
        
        
class Boss_Floor_Medium(Boss_Floor):
    """Creates an instance of a medium boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(Boss_Floor_Medium, self).__init__(level)
        
        poss_boss = [E.Head_Assassin(), E.Spider_Queen()]
        weights = [0.5, 0.5]
        
        self.enemy = choose_one(poss_boss, weights)
        
def get_floor(level: int, num_floors: int):
    """
    Inputs:
        level: An integer of the floor level
    Purpose: To pick a floor instance to create based on the level given
    Output: A floor object
    """
    if level >= 1 and level < 5:
        return Floor_Easy(level)
    
    elif level == 5:
        return Boss_Floor_Easy(level)
    
    elif level > 5 and level < 10:
        return Floor_Medium(level)
    
    elif level == 10:
        return Boss_Floor_Medium(level)
