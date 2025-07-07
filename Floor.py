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
        return "Dungeon: Floor {}".format(self.level)
    
    
class FloorEasy(Floor):
    """Creates a Floor object for floors from 1 to 5"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(FloorEasy, self).__init__(level)
        
        poss_enemy = [E.RabidRabbit(floor=level), E.Wolf(floor=level), E.Goblin(floor=level)]
        weights = [0.4, 0.35, 0.25]

        self.enemy = choose_one(poss_enemy, weights)


class FloorMedium(Floor):
    """Creates a Floor object for floors from 6 to 10"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(FloorMedium, self).__init__(level)
        
        poss_enemy = [E.VenomSpider(floor=level), E.LostSpirit(floor=level), E.Assassin(floor=level)]
        weights = [0.4, 0.35, 0.25]
        
        self.enemy = choose_one(poss_enemy, weights)
    
    
class FloorHard(Floor):
    """Creates a Floor object for floors from 6 to 10"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and an appropriate enemy
        """
        super(FloorHard, self).__init__(level)
        
        poss_enemy = []
        weights = []
        
        self.enemy = choose_one(poss_enemy, weights)
    
    
class BossFloor(Floor):
    """Creates an instance of a boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(BossFloor, self).__init__(level)
        
        
class BossFloorEasy(BossFloor):
    """Creates an instance of an easy boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(BossFloorEasy, self).__init__(level)
        
        poss_boss = [E.WolfPack(floor=level), E.GoblinMob(floor=level)]
        weights = [0.5, 0.5]
        
        self.enemy = choose_one(poss_boss, weights)
        
        
class BossFloorMedium(BossFloor):
    """Creates an instance of a medium boss floor in the game"""
    def __init__(self, level: int):
        """
        Inputs:
            level: An integer representing the level number
        Purpose: Create a floor with the given level number and a boss
        """
        super(BossFloorMedium, self).__init__(level)
        
        poss_boss = [E.HeadAssassin(floor=level), E.SpiderQueen(floor=level)]
        weights = [0.5, 0.5]
        
        self.enemy = choose_one(poss_boss, weights)
        
def get_floor(level: int):
    """
    Inputs:
        level: An integer of the floor level
    Purpose: To pick a floor instance to create based on the level given
    Output: A floor object
    """
    if level >= 1 and level < 5:
        return FloorEasy(level)
    
    elif level == 5:
        return BossFloorEasy(level)
    
    elif level > 5 and level < 10:
        return FloorMedium(level)
    
    elif level == 10:
        return BossFloorMedium(level)
